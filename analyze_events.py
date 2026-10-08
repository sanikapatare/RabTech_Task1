import json

# Read JSON file
with open("diagnostic-events.json", "r") as file:
    data = json.load(file)

events = data["events"]

# Count errors, warnings and slow requests
errors = 0
warnings = 0
slow_requests = 0
services = {}

for event in events:

    # Error count
    if event["level"] == "ERROR":
        errors += 1

    # Warning count
    if event["level"] == "WARN":
        warnings += 1

    # Slow request: more than 500 ms
    if event["latency_ms"] is not None and event["latency_ms"] > 500:
        slow_requests += 1

    # Service count
    service = event["service"]
    services[service] = services.get(service, 0) + 1


# Display results
print("DIAGNOSTIC EVENT ANALYSIS")
print("-------------------------")

print("Total Events:", len(events))
print("Total Errors:", errors)
print("Total Warnings:", warnings)
print("Slow Requests:", slow_requests)

print("\nService-wise Count:")
for service, count in services.items():
    print(service, ":", count)