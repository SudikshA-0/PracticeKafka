# AIOps Log Anomaly Detection

# Sample server log data
logs = [
    {"timestamp": "10:01", "cpu": 45, "memory": 52, "response_time": 120},
    {"timestamp": "10:02", "cpu": 51, "memory": 55, "response_time": 130},
    {"timestamp": "10:03", "cpu": 48, "memory": 51, "response_time": 115},
    {"timestamp": "10:04", "cpu": 60, "memory": 58, "response_time": 140},
    {"timestamp": "10:05", "cpu": 95, "memory": 60, "response_time": 150},
    {"timestamp": "10:06", "cpu": 55, "memory": 57, "response_time": 125},
    {"timestamp": "10:07", "cpu": 62, "memory": 59, "response_time": 145},
    {"timestamp": "10:08", "cpu": 49, "memory": 53, "response_time": 110},
    {"timestamp": "10:09", "cpu": 58, "memory": 56, "response_time": 135},
    {"timestamp": "10:10", "cpu": 65, "memory": 61, "response_time": 160},
    {"timestamp": "10:11", "cpu": 54, "memory": 55, "response_time": 125},
    {"timestamp": "10:12", "cpu": 97, "memory": 63, "response_time": 180},
    {"timestamp": "10:13", "cpu": 52, "memory": 54, "response_time": 120},
    {"timestamp": "10:14", "cpu": 61, "memory": 58, "response_time": 140},
    {"timestamp": "10:15", "cpu": 47, "memory": 52, "response_time": 115},
    {"timestamp": "10:16", "cpu": 59, "memory": 57, "response_time": 135},
    {"timestamp": "10:17", "cpu": 64, "memory": 60, "response_time": 155},
    {"timestamp": "10:18", "cpu": 92, "memory": 61, "response_time": 170},
    {"timestamp": "10:19", "cpu": 50, "memory": 53, "response_time": 118},
    {"timestamp": "10:20", "cpu": 57, "memory": 56, "response_time": 128},
]

print("Total records:", len(logs))

# Extract metric values
cpu_values = [log["cpu"] for log in logs]
memory_values = [log["memory"] for log in logs]
response_values = [log["response_time"] for log in logs]

# Calculate basic statistics
print("\n--- Basic Statistics ---")

print("CPU Average:", sum(cpu_values) / len(cpu_values))
print("CPU Minimum:", min(cpu_values))
print("CPU Maximum:", max(cpu_values))

print("Memory Average:", sum(memory_values) / len(memory_values))
print("Memory Minimum:", min(memory_values))
print("Memory Maximum:", max(memory_values))

print("Response Time Average:", sum(response_values) / len(response_values))
print("Response Time Minimum:", min(response_values))
print("Response Time Maximum:", max(response_values))
# Detect anomalies
CPU_THRESHOLD = 80

anomalies = []

for log in logs:
    if log["cpu"] > CPU_THRESHOLD:
        anomalies.append(log)

print("\n--- Anomalies Detected ---")
print("Anomalies detected:", len(anomalies))

print("\nTimestamp       CPU       Status")

for log in anomalies:
    print(f'{log["timestamp"]:<15}{log["cpu"]}%      ANOMALY')


import matplotlib.pyplot as plt

timestamps = [log["timestamp"] for log in logs]
cpu_values = [log["cpu"] for log in logs]

plt.plot(timestamps, cpu_values, marker="o", label="CPU Usage")

# Mark anomalies
for log in anomalies:
    plt.scatter(log["timestamp"], log["cpu"], color="red", s=100)

plt.axhline(CPU_THRESHOLD, linestyle="--", label="Threshold (80%)")

plt.xlabel("Timestamp")
plt.ylabel("CPU Usage (%)")
plt.title("AIOps CPU Usage and Anomalies")
plt.xticks(rotation=45)
plt.legend()
plt.tight_layout()

plt.show()

