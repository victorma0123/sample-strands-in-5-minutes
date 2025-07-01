from strands import Agent
from strands.agent.conversation_manager import SlidingWindowConversationManager


# Initialize your agent
agent = Agent(
    conversation_manager=SlidingWindowConversationManager(window_size=2),
    system_prompt="You are a helpful assistant that provides concise responses.",
    callback_handler=None
)

# Send a message to the agent
#response = agent("Hello! What can you do?")
#print(response)

while True:
    try:
        user_input = input("\n🎯 Your request: ")

        print("\n🤔 Processing...\n")
        response = agent(user_input)
        print(response)

        print("\nConversation History:\n")
        print(agent.messages)
        
    except KeyboardInterrupt:
        print("\n\nExecution interrupted. Exiting...")
        break
