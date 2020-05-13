from Block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 3  # number of leading 0's needed for proof
        self.genesis_block()

    # Creates genesis block and appends to chain
    def genesis_block(self):
        genesis_block = Block(["This is the genesis block"], "0", self.difficulty)
        self.chain.append(genesis_block)

    # Creates block with data and appends to chain
    def add_block(self, data):
        prev_hash = (self.chain[-1]).generate_hash()
        new_block = Block(data, prev_hash, self.difficulty)
        self.chain.append(new_block)

    # Prints full contents of the blockchain and verifies links
    def print_chain(self):
        for i in range(len(self.chain)):
            print(f"Block {i}")
            self.chain[i].print_contents()
        self.verify_chain()

    # Verifies linked hashes in chain
    def verify_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash():
                print(f"Invalid chain at block {i}: Block contents were changed!\n")
                return False
            if current.prev_hash != previous.generate_hash():
                print(f"Invalid chain at block {i}: Previous hash was changed\n")
                return False
        print("Chain is valid!\n")
        return True
