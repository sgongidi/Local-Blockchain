from Block import Block


class Blockchain:
    def __init__(self):
        self.chain = []
        self.difficulty = 4  # number of leading 0's needed for proofed hash
        self.genesis_block()

    # Creates genesis block and appends to chain
    def genesis_block(self):
        genesis_block = Block(["This is the genesis block"], "0", self.difficulty)
        self.chain.append(genesis_block)
        print("Genesis Block added!\n")

    # Creates block with data and appends to chain
    def add_block(self, data):
        if self.validate_chain():
            prev_hash = (self.chain[-1]).generate_hash()
            new_block = Block(data, prev_hash, self.difficulty)
            self.chain.append(new_block)
            print(f"Block {len(self.chain)-1} added!\nData: {data}\n")
        else:
            print("Block not added. Invalid chain!\n")

    # Prints full contents of the blockchain and verifies links
    def print_chain(self):
        print("Printing Blockchain...")
        for i in range(len(self.chain)):
            print(f"Block {i}")
            self.chain[i].print_contents()
        if self.validate_chain():
            print("Chain is valid!\n")
        else:
            print(f"Chain is invalid!\n")

    # Validates linked hashes in chain
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash() or current.prev_hash != previous.generate_hash():
                return False
        return True
