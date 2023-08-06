from kafka_rest import Producer, Consumer

# Target endpoint and messages
target_endpoint = "pdf2text"
files = ["test_files/test_1.pdf", "test_files/test_2.pdf", "test_files/test_3.pdf"]

# Produce files
producer = Producer()
new_keys = producer.produce_files(files, target_endpoint)

# Consume messages
with Consumer() as consumer:
    for data, remaining_keys in consumer.consume(new_keys, interval_sec=1):
        if data:
            for message in data:
                print("-" * 50)
                print("Text:", end=" ")
                print(message['value']['text'])
                print("-" * 50)
            print(f"Remaining keys: {remaining_keys}")
