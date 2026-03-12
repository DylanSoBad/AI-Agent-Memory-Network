import time
from shelby_memory_client import ShelbyMemoryClient

client = ShelbyMemoryClient(
    agent_address="0xAgent",
    shelby_api="",
    aptos_node=""
)

start = time.time()

client.store(
    "benchmark test",
    "testing storage latency"
)

end = time.time()

print("Latency:", round(end - start, 3), "seconds")
