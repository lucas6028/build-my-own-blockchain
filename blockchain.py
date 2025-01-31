import hashlib
import json
from textwrap import dedent
from time import time
from uuid import uuid4

from flask import Flask, jsonify, request

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

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        Validates the Proof: does hash(last_proof, proof) contain 4 leading zeros?
        :param last_proof: <int> previous proof
        :param proof: <int> current proof
        :return: <bool> true if correct, false if not.
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"

# instantiate out node
app = Flask(__name__)

# generate a globally unique address for this node
node_identifier = str(uuid4()).replace('-', '')

# instantiate the blockchain
blockchain = Blockchain()


@app.route('/mine', methods=['GET'])
def mine():
    # we run the proof of work algorithm to get the next proof
    last_block = blockchain.last_block
    last_proof = last_block['proof']
    proof = blockchain.proof_of_work(last_proof)

    # we must receive a reward for finding the proof
    # the sender is "0" to signify that this node has mined a new coin
    blockchain.create_new_transaction(
        sender="0",
        recipient=node_identifier,
        amount=1,
    )

    # forge the new block by adding it to the chain
    previous_hash = blockchain.hash(last_block)
    block = blockchain.create_new_block(proof, previous_hash)

    response = {
        'message': "New Block Forged",
        'index': block['index'],
        'transactions': block['transactions'],
        'proof': block['proof'],
        'previous_hash': block['previous_hash'],
    }
    return jsonify(response), 200

@app.route('/transactions/new', methods=['POST'])
def new_transaction():
    values = request.get_json()

    # check that the required fields are in the POST'ed data
    required = ['sender', 'recipient', 'amout']
    if not all(k in values for k in required):
        return 'Misssing Values!', 400

    # create a new transaction
    index = blockchain.create_new_transaction(values['sender'], values['recipient'], values['amount'])

    response = {'message': f'Transaction will be added to the block {index}'}
    return jsonify(response), 201

@app.route('/chain', methods=['GET'])
def full_chain():
    response = {
        'chain': blockchain.chain,
        'length': len(blockchain.chain),
    }
    return jsonify(response), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
