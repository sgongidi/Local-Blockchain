from datetime import datetime
from hashlib import sha512


class Block:
    def __init__(self, data, prev_hash):
        self.timestamp = datetime.now()
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.proof = ""
        self.hash = self.generate_hash()

    # Produces hash from block contents
    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.data) + str(self.prev_hash) + str(self.nonce)
        block_hash = sha512(block_contents.encode()).hexdigest()
        return block_hash

    def print_contents(self):
        print("timestamp: ", self.timestamp)
        print("data: ", self.data)
        print("current hash: ", self.generate_hash())
        print("previous hash: ", self.prev_hash)
        if self.proof != "":
            print(f"proof: {self.proof}\n")
