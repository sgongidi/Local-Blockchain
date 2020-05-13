from Blockchain import Blockchain


def main():
    my_chain = Blockchain()
    data_1 = [{"sender": "Sai", "receiver": "Ty", "amount": "100"},
              {"sender": "Ty", "receiver": "Sai", "amount": "50"}]
    data_2 = ["my data", "some other data"]

    # Blocks are immutable once added to the blockchain
    my_chain.add_block(data_1)
    my_chain.add_block(data_2)
    my_chain.print_chain()

    # Attempting to change the contents results in a broken chain
    my_chain.chain[1].data = ["Fake Data"]
    my_chain.print_chain()


if __name__ == "__main__":
    main()
