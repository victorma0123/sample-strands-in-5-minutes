from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client
from strands.models import BedrockModel
import sys
import logging


#打开debug 日志 
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# Ensure UTF-8 encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')


#model_id="us.amazon.nova-premier-v1:0",
model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="us-west-2",
    temperature=0.7
)


def main():
    
    # Connect to the recipe MCP server
    print("\nConnecting to MCP Server...")
    mcp_recipe_server = MCPClient(lambda: streamablehttp_client("http://localhost:8080/mcp"))

    try:
        with mcp_recipe_server:

            # Create the cooking expert agent with a system prompt and DeepSeek model
            cooking_expert = Agent(
                model=model,
                system_prompt="""你是一位中华美食专家，拥有丰富的中国菜谱知识。你可以：
                1. 介绍各大菜系的特色和代表菜品
                2. 根据用户需求推荐合适的菜谱
                3. 根据现有食材搜索可制作的菜品
                4. 提供详细的烹饪步骤和技巧

                当用户询问菜谱时：
                - 先了解他们的口味偏好和烹饪水平
                - 推荐合适难度的菜品
                - 详细介绍食材和制作步骤
                - 给出实用的烹饪小贴士

                规则：
                - 必须使用MCP Server 提供的tool获取菜谱信息
                - 不要编造菜谱，只使用数据库中的真实菜谱
                - 用温馨友好的语气与用户交流
                """
            )

            # List the tools available on the MCP server...
            mcp_tools = mcp_recipe_server.list_tools_sync()
            print(f"Available tools: {[tool.tool_name for tool in mcp_tools]}")

            # ... and add them to the agent
            cooking_expert.tool_registry.process_tools(mcp_tools)

            # Start an interactive cooking session
            print("\n 中华美食专家 - MCP 集成版")
            print("=" * 50)
            print("\n🥢 试试问: '有哪些菜系？' 或 '推荐一道淮扬菜' 或 '用猪肉能做什么菜？'")

            while True:
                user_input = input("\n您的需求: ")
                
                if user_input.lower() in ["exit", "quit", "bye", "退出", "再见"]:
                    print("祝您烹饪愉快！")
                    break
                
                print("\n 正在为您查找...\n")
                cooking_expert(user_input)
               
    except Exception as e:
        print(f" 查询失败: {e}")
        print("请确保美食服务正在运行: python strands_mcp_server.py")

if __name__ == "__main__":
    main()