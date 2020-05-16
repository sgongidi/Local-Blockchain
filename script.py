from Blockchain import Blockchain


def main():
    data_1 = [{"sender": "Sai", "receiver": "Ty", "amount": "100"},
              {"sender": "Ty", "receiver": "Sai", "amount": "50"}]
    data_2 = ["my data", "other data"]
    data_3 = "more data"

    # Blocks are immutable once added to the blockchain
    my_chain = Blockchain()
    my_chain.add_block(data_1)
    my_chain.add_block(data_2)
    my_chain.print_chain()

    # Attempting to change the contents results in an invalid chain
    print("Inserting fake data...\n")
    my_chain.chain[1].data = ["Fake Data"]
    my_chain.print_chain()

    # Blocks can't be added to an invalid chain
    my_chain.add_block(data_3)
    my_chain.print_chain()


if __name__ == "__main__":
    main()
