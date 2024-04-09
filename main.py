import hashlib

def hashGenerator(data):
    sha = hashlib.sha256(data.encode())
    return sha.hexdigest()

class Block:

    def __init__(self, data, hash, prev_hash):
        self.data = data
        self.hash = hash
        self.prev_hash = prev_hash
        

class BlockChain:
    
        def __init__(self):
             hashLastBlock = hashGenerator("Genesis Block")
             hashFirstBlock = hashGenerator("First Block")

             genesisBlock = Block("Genesis Block", hashFirstBlock, hashLastBlock)
             self.chain = [genesisBlock]
    
        def addBlock(self, data):
            prev_hash = self.chain[-1].hash
            hash = hashGenerator(data)
            newBlock = Block(data, hash, prev_hash)
            self.chain.append(newBlock)

myChain = BlockChain()

myChain.addBlock("Second Block")
myChain.addBlock("Third Block")
myChain.addBlock("Fourth Block")

for block in myChain.chain:
     print(block.__dict__)