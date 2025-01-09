from spade import agent, message, behaviour
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

        class BlockchainInteractionBehaviour(behaviour.CyclicBehaviour):
            async def run(self):
                product_id = 0  # Example Product ID to check
                product = self.contract.functions.products(product_id).call()
                is_halal = self.contract.functions.halalCertified(product_id).call()
                print(f"Product ID: {product_id} - Halal Certified: {is_halal}")

        self.add_behaviour(BlockchainInteractionBehaviour())

# Instantiate and deploy BlockchainAgent
blockchain_agent = BlockchainAgent("blockchain@localhost", "blockchainpassword", "<CONTRACT_ADDRESS>", "<CONTRACT_ABI>")
blockchain_agent.start()
