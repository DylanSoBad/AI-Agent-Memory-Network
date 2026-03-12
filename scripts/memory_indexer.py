import json

def load_memory(file):

    with open(file) as f:
        data = json.load(f)

    print("Agent:", data["agent_id"])

    for chunk in data["memory_chunks"]:
        print("-", chunk["description"])
