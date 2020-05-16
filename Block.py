from time import time
from hashlib import sha512


class Block:
    def __init__(self, data, prev_hash, difficulty):
        self.timestamp = time()
        self.data = data
        self.prev_hash = prev_hash
        self.nonce = 0
        self.hash = self.proof_of_work(difficulty)

    # Generates proof of work for block.
    def proof_of_work(self, difficulty):
        proof = self.generate_hash()
        while proof[:difficulty] != "0" * difficulty:
            self.nonce += 1
            proof = self.generate_hash()
        return proof

    # Produces hash from block contents
    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.data) + str(self.prev_hash) + str(self.nonce)
        return sha512(block_contents.encode()).hexdigest()

    def print_contents(self):
        print(f"timestamp: {self.timestamp}")
        print(f"data: {self.data}")
        print(f"nonce: {self.nonce}")
        print(f"current hash: {self.generate_hash()}")
        print(f"previous hash: {self.prev_hash}\n")
