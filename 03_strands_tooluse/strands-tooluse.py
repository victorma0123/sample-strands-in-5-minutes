from strands import Agent, tool
from strands_tools import calculator
from strands.models.ollama import OllamaModel
model = OllamaModel(
    host="http://127.0.0.1:11434",
    model_id="qwen3:1.7b"   # 换成你机器上实际有的模型（ollama list）
)
@tool
def weather(city: str) -> str:
    """Get weather information for a city

    Args:
        city: City or location name
    """

    # Implement weather lookup logic here
    return f"Weather for {city}: Sunny, 35°C"

# Initialize your agent
agent = Agent(
    model=model,
    tools=[weather, calculator],
    system_prompt="You are a helpful assistant that provides concise responses.",
    callback_handler=None
)

print("\nTool Config:\n")
#print(agent.tool)

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




