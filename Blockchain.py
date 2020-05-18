from Block import Block


class Blockchain:
    def __init__(self):
        self.difficulty = 4  # number of leading 0's needed for proofed hash
        genesis_block = Block(["Genesis Block"], "0", self.difficulty)
        self.chain = [genesis_block]
        print(f"Genesis Block created!\nHash: {genesis_block.generate_hash()}\n")

    # Creates block with data and appends to chain
    def add_block(self, data):
        if self.validate_chain() == -1:
            prev_hash = (self.chain[-1]).generate_hash()
            new_block = Block(data, prev_hash, self.difficulty)
            self.chain.append(new_block)
            print(f"Block {len(self.chain)-1} added!\n"
                  f"Data: {data}\n"
                  f"Hash: {new_block.generate_hash()}\n")
        else:
            print(f"Block not added. Invalid chain at Block {self.validate_chain()}!\n")

    # Prints full contents of the blockchain and verifies links
    def print_chain(self):
        print("Printing Blockchain...")
        for i in range(len(self.chain)):
            print(f"Block {i}")
            self.chain[i].print_contents()
        if self.validate_chain() == -1:
            print("Chain is valid!\n")
        else:
            print(f"Chain is invalid at Block {self.validate_chain()}!\n")

    # Validates linked hashes in chain.
    # Returns index of invalid block or -1 for valid chain
    def validate_chain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i - 1]
            if current.hash != current.generate_hash() or current.prev_hash != previous.generate_hash():
                return i
        return -1
