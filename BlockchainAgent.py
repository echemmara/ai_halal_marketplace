from spade import agent, message, behaviour
from spade.behaviour import CyclicBehaviour
from web3 import Web3

class BlockchainAgent(agent.Agent):
    def __init__(self, jid, password, contract_address, contract_abi):
        super().__init__(jid, password)
        self.w3 = Web3(Web3.HTTPProvider('https://rinkeby.infura.io/v3/YOUR_INFURA_PROJECT_ID'))
        self.contract_address = contract_address
        self.contract_abi = contract_abi
        self.contract = self.w3.eth.contract(address=self.contract_address, abi=self.contract_abi)

    async def setup(self):
        print(f"Blockchain Agent {self.name} is online!")

        # Define behavior to listen for Halal checks and transactions
        class BlockchainInteractionBehaviour(CyclicBehaviour):
            async def run(self):
                # Example logic: Check if product needs Halal certification
                message_to_check = Message(to="halal@localhost")
                message_to_check.body = "Product ID: 0"  # Example product ID for Halal compliance check
                await self.send(message_to_check)

        self.add_behaviour(BlockchainInteractionBehaviour())

    # Function to interact with blockchain
    async def interact_with_blockchain(self, product_id):
        # Example call to blockchain smart contract to check product Halal certification
        product = self.contract.functions.products(product_id).call()
        is_halal = self.contract.functions.halalCertified(product_id).call()
        return {"product_id": product_id, "name": product[1], "price": product[2], "is_halal": is_halal}
