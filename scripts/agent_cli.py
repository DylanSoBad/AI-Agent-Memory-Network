import os
from shelby_memory_client import ShelbyMemoryClient

client = ShelbyMemoryClient(
    agent_address="0xAgent",
    shelby_api="https://testnet.shelby.serves/v1",
    aptos_node="https://fullnode.testnet.aptoslabs.com/v1"
)

import sys

cmd = sys.argv[1]

if cmd == "store":

    user = sys.argv[2]
    ai = sys.argv[3]

    client.store(user, ai)

elif cmd == "test":

    client.store(
        "How to build on Shelby?",
        "Use hot storage layer for low latency."
    )
