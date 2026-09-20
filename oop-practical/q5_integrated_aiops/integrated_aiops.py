from kafka import KafkaConsumer
import json

# Connect to Kafka and subscribe to server_metrics topic
consumer = KafkaConsumer(
    "server_metrics",
    bootstrap_servers="localhost:9092",
    auto_offset_reset="latest",
    enable_auto_commit=True,
    value_deserializer=lambda x: json.loads(x.decode("utf-8"))
)

anomaly_count = 0

print("AIOps Monitoring Started...")
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

    # Detect high CPU anomaly
    if cpu > 80:
        anomaly_count += 1

        print(f"ALERT: High CPU detected on {server_id}")
        print(f"Total anomalies detected: {anomaly_count}\n")