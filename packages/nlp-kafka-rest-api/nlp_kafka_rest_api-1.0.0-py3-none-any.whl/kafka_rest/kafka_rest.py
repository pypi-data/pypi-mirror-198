import base64
import json
import os
from pathlib import Path
import time
from typing import Any, Collection, Dict, List, Optional, Set, Tuple, Union
from uuid import uuid4

import requests


class Client:
    def __init__(self, **kwargs):
        """
        create a client instance.
        :param kwargs:
            - kafka_rest_api_url: API Endpoint URL. Required if "KAFKA_REST_API_URL" is not an environment variable.
            - topic_id: target topic_id. required if "TOPIC_ID" is not an environment variable.
            - auth_headers: Authentication headers as a Dict[str, str].
        """

        self.kafka_rest_api_url = os.environ.get('KAFKA_REST_API_URL', kwargs.get("kafka_rest_api_url"))
        if not self.kafka_rest_api_url:
            raise Exception("Invalid value assigned to 'kafka_rest_api_url' or 'KAFKA_REST_API_URL' env var.")

        self.topic_id = os.environ.get('TOPIC_ID', kwargs.get("topic_id"))
        if not self.topic_id:
            raise Exception("Invalid value assigned to 'topic_id' or 'TOPIC_ID' env var.")

        self.auth_headers = kwargs.get("auth_headers", dict())

        x_api_key = os.environ.get("X_API_KEY")

        if x_api_key and "x-api-key" not in self.auth_headers:
            self.auth_headers.update({"x-api-key": x_api_key})

    def request(self, **kwargs):
        kwargs["url"] = f"{self.kafka_rest_api_url}{kwargs['url']}"
        if self.auth_headers:
            kwargs.get("headers", {}).update(self.auth_headers)

        response = requests.request(**kwargs)

        if not response.ok:
            response.raise_for_status()

        return response


class Producer(Client):
    def __init__(self, producer_data_max_size: int = 67_108_864, **kwargs):
        """
        Create a producer instance.
        :param producer_data_max_size: Maximum size of each request payload in bytes.
        :param kwargs:
            - kafka_rest_api_url: API Endpoint URL. Required if "KAFKA_REST_API_URL" is not an environment variable.
            - topic_id: target topic_id. required if "TOPIC_ID" is not an environment variable.
            - auth_headers: Authentication headers as a Dict[str, str].
        """
        super().__init__(**kwargs)

        self.max_data_bytes = os.environ.get('PRODUCER_DATA_MAX_SIZE', producer_data_max_size)
        self.key_history, self.key_last_request = [], []

    @staticmethod
    def __manage_keys(len_messages: int, keys: Optional[List[str]] = None):
        if not keys:
            return [str(uuid4()) for _ in range(len_messages)]

        elif len(keys) != len_messages:
            raise ValueError("List of keys must have the same size as list of messages.")

        return keys

    def produce(self, messages: Collection, endpoint: str, keys: Optional[List[str]] = None) -> List[str]:
        """
        Produce messages to a given topic.
        :param messages: JSON serializable Collection of messages.
        :param endpoint: Target endpoint.
        :param keys: Optional list of customized keys. Number of keys must match the number of messages.
        :return: List of generated UUID keys.
        """
        headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}
        keys = self.__manage_keys(len(messages), keys)
        records = {"records": [
            {"key": k, "value": {"endpoint": endpoint, "payload": v}} for k, v in zip(keys, messages)]}
        record_data = json.dumps(records)

        self._check_data_size(record_data.encode("utf-8"))

        self.request(method="POST", url=f"/topics/{self.topic_id}", headers=headers, data=record_data)

        self.key_history.extend(keys)
        self.key_last_request = keys
        return self.key_last_request

    def _check_data_size(self, data: bytes):
        if self.max_data_bytes < len(data):
            raise RuntimeError(f"Producer request data exceeded allowed number bytes: {self.max_data_bytes} bytes")

    def produce_files(self, files: List[str],
                      endpoint: str,
                      keys: Optional[List[str]] = None) -> List[str]:
        """
        Produce files to a given topic.
        :param files: List of paths to input files.
        :param endpoint: Target API endpoint.
        :param keys: Optional list of customized keys. Number of keys must match the number of messages.
        :return: List of generated UUID keys.
        """

        messages = []
        for path in files:
            with open(f"{path}", "rb") as f:
                messages.append(
                    {
                        "name": Path(path).name,
                        "bytes":  base64.b64encode(f.read()).decode(),
                        "type": f"application/{'pdf' if path.endswith('.pdf') else 'octet-stream'}"
                    }
                )

        return self.produce(messages, endpoint, keys=keys)


class Consumer(Client):
    def __init__(self, **kwargs):
        """
        Create a consumer instance.
        :param kwargs:
            - kafka_rest_api_url: API Endpoint URL. Required if "KAFKA_REST_API_URL" is not an environment variable.
            - topic_id: target topic_id. required if "TOPIC_ID" is not an environment variable.
            - auth_headers: Authentication headers as a Dict[str, str].
            - consumer_group: Assign a given consumer group name. Defaults to a randomly generated UUID is assigned.
            - instance: Assign a given instance name. Defaults to a randomly generated UUID.
        """
        super().__init__(**kwargs)

        self.created = False
        self.consumer_group = kwargs.get("consumer_group", str(uuid4()).replace("-", ""))
        self.instance = kwargs.get("instance", str(uuid4()).replace("-", ""))
        self.remaining_keys = set()

    def __enter__(self):
        return self.create().subscribe()

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.delete()

    def create(self):
        """
        Create a Consumer instance in binary format.
        :return: self.
        """

        if not self.created:
            url = f"/consumers/{self.consumer_group}"
            headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}
            config = json.dumps({"name": self.instance, "format": "binary", "auto.offset.reset": "earliest"})

            self.request(method="POST", url=url, headers=headers, data=config)
            self.created = True

        return self

    def subscribe(self):
        """
        Subscribe to the given topics.
        :return: self.
        """

        url = f"/consumers/{self.consumer_group}/instances/{self.instance}/subscription"
        headers = {"Content-Type": "application/vnd.kafka.json.v2+json"}
        topics_data = json.dumps({"topics": [f"{self.topic_id}-response"]})

        self.request(method="POST", url=url, headers=headers, data=topics_data)
        return self

    def consume_earliest(self) -> List[Dict[str, Any]]:
        """
        Consume the earliest messages in the assigned topics.
        :return: List of dictionaries where the "value" key contains the message and the "key" key contains its key.
        """
        url = f'/consumers/{self.consumer_group}/instances/{self.instance}/records'
        headers = {'Accept': 'application/vnd.kafka.binary.v2+json'}

        response = self.request(method="GET", url=url, headers=headers, data="")
        response_decoded = [self.parse_record(r) for r in response.json()]

        return response_decoded

    def delete(self):
        """
        Delete the current client instance from the kafka cluster.
        """
        url = f'/consumers/{self.consumer_group}/instances/{self.instance}'
        headers = {'Content-Type': 'application/vnd.kafka.v2+json'}

        self.request(method="DELETE", url=url, headers=headers, data="")
        self.created = False

    def consume(self, keys: List[str], interval_sec: Union[int, float] = 5) -> Tuple[List[dict], Set[str]]:
        """
        Consume messages from the assigned topics as iterator.
        :param keys: List of keys to choose from the topics.
        :param interval_sec: Minimum interval in seconds between polling requests.
        :return: List of dictionaries where the "value" key contains the message and the "key" key contains its key.
        """

        if interval_sec < 0:
            raise ValueError("'interval_sec' should be an 'int' or 'float' greater or equal to 0.")

        self.remaining_keys = set(keys)

        while self.remaining_keys:
            time.sleep(interval_sec)
            data = {d['key']: d for d in self.consume_earliest() if d['key'] in self.remaining_keys}
            self.remaining_keys = self.remaining_keys - set(data)
            yield [d for _, d in data.items()], self.remaining_keys

    def consume_all(self, keys: List[str], interval_sec: Union[int, float] = 5) -> List[Dict[str, Any]]:
        """
        Consume all messages from all keys.
        :param keys: List of keys to choose from the topics.
        :param interval_sec: Minimum interval in seconds between polling requests.
        :return: List of dictionaries where the "value" key contains the message and the "key" key contains its key.
        """

        return [data for data, _ in self.consume(keys, interval_sec)]

    @staticmethod
    def decode_base64(string: str):
        if string:
            try:
                return json.loads(base64.b64decode(string))
            except json.decoder.JSONDecodeError:
                return base64.b64decode(string)
        return string

    @staticmethod
    def parse_record(record: dict):
        return {
            "key": Consumer.decode_base64(record["key"]),
            "value": Consumer.decode_base64(record["value"])
        }
