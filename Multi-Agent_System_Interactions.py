from spade import agent, message
from spade.behaviour import CyclicBehaviour

class VendorAgent(agent.Agent):
    async def setup(self):
        print(f"Vendor Agent {self.name} is online!")

        # Define a cyclic behavior to send messages to HalalComplianceAgent
        class HalalRequestBehaviour(CyclicBehaviour):
            async def run(self):
                message_to_halal = Message(to="halal@localhost")
                message_to_halal.body = "Product ID: 0"  # Example product ID
                await self.send(message_to_halal)

        self.add_behaviour(HalalRequestBehaviour())

# Instantiate and run the vendor agent
vendor_agent = VendorAgent("vendor@localhost", "vendorpassword")
vendor_agent.start()
