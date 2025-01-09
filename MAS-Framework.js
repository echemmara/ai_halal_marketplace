from spade import agent, quit_gracefully
from spade.message import Message

class HalalAgent(agent.Agent):
    async def setup(self):
        print(f"Agent {self.name} is online!")

    async def on_message(self, message):
        print(f"Received message from {message.sender}: {message.body}")
        # Logic to handle compliance verification
        response = f"Compliance check complete for product {message.body}"
        await self.send_reply(message, response)

# Instantiate and run the agent
my_agent = HalalAgent("halal@localhost", "password")
my_agent.start()
quit_gracefully(my_agent)
