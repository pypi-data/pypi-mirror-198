from kafka_rest import Producer, Consumer

# Target endpoint and messages
target_endpoint = "pke"
messages = [{"text": "Genome engineering is a powerful tool.", "algorithm": "TopicRank", "n_best": 10},
            {"text": "Diagnosing, treating, and preventing disease or injury.", "algorithm": "TopicRank", "n_best": 10}]

# Producer
print("Producing messages...")
producer = Producer()
new_keys = producer.produce(messages, target_endpoint)

# Consumer
print("Consuming messages...")
with Consumer() as consumer:
    for data, remaining_keys in consumer.consume(new_keys, interval_sec=1):
        if data:
            print(f"Data: {data}")
            print(f"Remaining keys: {remaining_keys}")
