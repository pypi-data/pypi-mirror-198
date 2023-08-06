from kafka_rest import Producer, Consumer

# Target endpoint and messages
target_endpoint = "pke"
messages = [{"text": "Genome engineering is a powerful tool.", "algorithm": "TopicRank", "n_best": 10},
            {"text": "Diagnosing, treating, and preventing disease or injury.", "algorithm": "TopicRank", "n_best": 10}]

# Producer
print("Producing messages...")
producer = Producer()
new_keys = producer.produce(messages, target_endpoint)

# Step-by-step consumer instantiation
print("Create consumer...")
consumer = Consumer()
consumer.create()
consumer.subscribe()
# or consumer.create().subscribe()

# Consume data
data = consumer.consume_all(keys=new_keys, interval_sec=1)
print(f"Data: {data}")

# Delete consumer (good practice to release resources)
consumer.delete()
