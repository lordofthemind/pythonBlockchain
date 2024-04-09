import hashlib
import datetime

def hash_generator(data):
    sha = hashlib.sha256(data.encode())
    return sha.hexdigest()

class Block:
    def __init__(self, data, timestamp, prev_hash):
        self.data = data
        self.timestamp = timestamp
        self.prev_hash = prev_hash
        self.hash = self.generate_hash()

    def generate_hash(self):
        data = str(self.data) + str(self.timestamp) + str(self.prev_hash)
        return hash_generator(data)

class Blockchain:
    def __init__(self):
        self.chain = [self.create_genesis_block()]

    def create_genesis_block(self):
        return Block("Genesis Block", datetime.datetime.now(), "0")

    def add_block(self, data):
        prev_hash = self.chain[-1].hash
        timestamp = datetime.datetime.now()
        new_block = Block(data, timestamp, prev_hash)
        self.chain.append(new_block)

    def is_valid(self):
        for i in range(1, len(self.chain)):
            current_block = self.chain[i]
            previous_block = self.chain[i - 1]

            if current_block.hash != current_block.generate_hash():
                return False

            if current_block.prev_hash != previous_block.hash:
                return False

        return True

if __name__ == "__main__":
    my_chain = Blockchain()

    my_chain.add_block("Second Block")
    my_chain.add_block("Third Block")
    my_chain.add_block("Fourth Block")

    for block in my_chain.chain:
        print(block.__dict__)

    print("Is the blockchain valid?", my_chain.is_valid())
