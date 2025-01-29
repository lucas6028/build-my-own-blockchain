import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []

        # create the genesis block
        self.create_new_block(previous_hash=1, proof=100)

    def create_new_block(self):
        # create a new block and adds it to the chain
        pass

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
            'recipient', recipient,
            'amout',: amout,
        })
        
        return self.last_block['index'] + 1

    @staticmethod
    def hash(block):
        # hashes a block
        pass

    @property
    def last_block(self):
        # return the last block in the chain
        pass
