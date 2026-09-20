from kafka import KafkaConsumer
import json

# Connect to Kafka and subscribe to the topic
consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="earliest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

print("Listening for server metrics...\n")

# Continuously receive messages
for message in consumer:
    data = message.value

    server_id = data["server_id"]
    cpu = data["cpu_usage"]
    memory = data["memory_usage"]

    print(
        f"Server: {server_id} | "
        f"CPU: {cpu}% | "
        f"Memory: {memory}%"
    )

    # Detect high CPU
    if cpu > 80:
        print(f"ALERT: High CPU detected on {server_id}")