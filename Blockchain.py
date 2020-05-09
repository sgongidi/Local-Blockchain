from Block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.genesis_block()

    # Creates genesis block and appends to chain
    def genesis_block(self):
        genesis_block = Block(["This is the genesis block"], "0")
        genesis_block.generate_hash()
        genesis_block.proof = self.proof_of_work(genesis_block)
        self.chain.append(genesis_block)

    # Creates block with data and appends to chain
    def add_block(self, data):
        prev_hash = (self.chain[-1]).hash
        new_block = Block(data, prev_hash)
        new_block.generate_hash()
        new_block.proof = self.proof_of_work(new_block)
        self.chain.append(new_block)

    # Prints full contents of the blockchain
    def print_chain(self):
        for i in range(len(self.chain)):
            current_block = self.chain[i]
            print(f"Block {i}")
            current_block.print_contents()

    # Verifies linked hashes in chain
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print("Invalid chain: Current hash not equal to generated hash\n")
                return False
            if current.prev_hash != previous.generate_hash():
                print("Invalid chain: Previous hash was changed\n")
                return False
            if current.proof == "":
                print(f"\nInvalid block {i}: Proof not generated")
                return False
        print("Chain is valid!\n")
        return True

    # Generates proof of work for block
    @staticmethod
    def proof_of_work(block, difficulty=2):  # difficulty: number of leading 0's needed for proof
        proof = block.generate_hash()
        while proof[:difficulty] != "0" * difficulty:
            block.nonce += 1
            proof = block.generate_hash()
        block.nonce = 0
        return proof
