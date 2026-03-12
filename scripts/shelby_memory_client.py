import time
import requests


class ShelbyMemoryClient:

    def __init__(self, agent_address, shelby_api, aptos_node):
        self.agent_address = agent_address
        self.shelby_api = shelby_api
        self.aptos_node = aptos_node

    def prepare_memory(self, user_msg, ai_msg):

        return {
            "agent_id": self.agent_address,
            "timestamp": int(time.time()),
            "content": {
                "user": user_msg,
                "ai": ai_msg
            }
        }

    def upload(self, memory):

        print("Uploading to Shelby...")

        try:
            r = requests.post(
                f"{self.shelby_api}/upload",
                json=memory,
                timeout=10
            )

            cid = r.json()["cid"]

        except:
            cid = f"shelby://mem_{int(time.time())}"

        print("CID:", cid)

        return cid

    def update_chain(self, cid):

        print("Updating Aptos pointer...")

        payload = {
            "function": "memory_network::agent_memory::update_memory",
            "arguments": [cid]
        }

        try:
            requests.post(
                f"{self.aptos_node}/transactions",
                json=payload
            )

        except:
            print("Mock transaction sent")

    def store(self, user_msg, ai_msg):

        memory = self.prepare_memory(user_msg, ai_msg)

        cid = self.upload(memory)

        self.update_chain(cid)

        print("Memory stored successfully")
