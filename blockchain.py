import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # create the genesis block
        self.create_new_block(previous_hash=1, proof=100)

    def create_new_block(self, proof, previous_hash=None):
        """
        Create a new block in the Blockchain
        :param proof: <int> the proof given by the Proof of Word algorithm
        :param previous_hash: (Optional) <str> Hash of previous block
        :return: <dict> new block
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transaction': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }

        # reset the current list of transactions
        self.current_transactions = []

        self.chain.append(block)
        return block

    def create_new_transaction(self, sender, recipient, amout):
        """
        Creates a new transaction to go into the next mined Block
        :param sender: <str> Address of the sender
        :param recipient: <str> Addess of the recipient
        :param amout: <int> amout
        :return: <int> the index of the block that will hold this transaction
        """

        self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amout': amout,
        })
        
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        """
        Create a SHA-256 hash of block
        :param block: <dict> block
        :return: <str>
        """

        # we must make sure that the dictionary is ordered,
        # or we'll have inconsistent hashes
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()

    @property
    def last_block(self):
        return self.chain[-1]

    def proof_of_work(self, last_proof):
        """
        Simple Proof of Work Algorithm 
        - Find a number p' such that hash(pp') contains leading 4 zeros, where p is the previous p'
        - p is the previous proof, and p' is the new proof 
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1 

        return proof 


