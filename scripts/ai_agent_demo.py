import random
from shelby_memory_client import ShelbyMemoryClient

client = ShelbyMemoryClient(
    agent_address="0xAgent",
    shelby_api="https://testnet.shelby.serves/v1",
    aptos_node="https://fullnode.testnet.aptoslabs.com/v1"
)

questions = [
    "What is DeFi?",
    "Explain Web3 storage",
    "How does Aptos work?",
    "What is AI memory?"
]

answers = [
    "DeFi enables financial services on blockchain.",
    "Shelby provides decentralized hot storage.",
    "Aptos is a high-performance Layer 1 blockchain.",
    "AI memory stores context for agents."
]

for i in range(3):

    q = random.choice(questions)
    a = random.choice(answers)

    print("User:", q)
    print("Agent:", a)

    client.store(q, a)
