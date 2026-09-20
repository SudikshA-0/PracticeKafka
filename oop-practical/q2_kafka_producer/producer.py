from kafka import KafkaProducer
import json
import time

# Connect to Kafka
producer = KafkaProducer(
    bootstrap_servers="localhost:9092",
    value_serializer=lambda v: json.dumps(v).encode("utf-8")
)

# Send 10 server metric messages
for i in range(1, 11):
    data = {
        "server_id": f"server{i}",
        "cpu_usage": 50 + i,
        "memory_usage": 60 + i
    }

    producer.send("server_metrics", value=data)

    print("Message sent:", data)

    time.sleep(1)

producer.flush()
producer.close()

print("All messages sent successfully.")