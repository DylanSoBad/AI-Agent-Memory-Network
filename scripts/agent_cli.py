import sys
from shelby_memory_client import ShelbyMemoryClient

client = ShelbyMemoryClient(
    agent_address="0xAgent",
    shelby_api="",
    aptos_node=""
)

cmd = sys.argv[1]

if cmd == "store":

    user = sys.argv[2]
    ai = sys.argv[3]

    client.store(user, ai)

elif cmd == "demo":

    import ai_agent_demo

elif cmd == "benchmark":

    import storage_benchmark

else:

    print("Commands:")
    print("store <user> <ai>")
    print("demo")
    print("benchmark")
