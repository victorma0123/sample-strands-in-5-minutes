from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client
from strands.models import BedrockModel
import sys
import logging


# #打开debug 日志 
# logging.getLogger("strands").setLevel(logging.DEBUG)
# logging.basicConfig(
#     format="%(levelname)s | %(name)s | %(message)s",
#     handlers=[logging.StreamHandler()]
# )

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
            print("🔍 正在发现 MCP 服务器上的工具...")
            mcp_tools = mcp_recipe_server.list_tools_sync()
            
            print(f"✅ 发现 {len(mcp_tools)} 个可用工具:")
            for i, tool in enumerate(mcp_tools, 1):
                print(f"   {i}. {tool.tool_name}")
            
            # print("\n🔧 正在注册工具到 Agent...")
            # # ... and add them to the agent
            cooking_expert.tool_registry.process_tools(mcp_tools)
            # print("✅ 工具注册完成！")

            # Start an interactive cooking session
            print("\n 中华美食专家Agent - 集成 MCP ")
            print("=" * 50)
            print("\n🥢 试试问: '有哪些菜系？' 或 '推荐一道淮扬菜' 或 '用猪肉能做什么菜？'")

            while True:
                user_input = input("\n您的需求: ")
                
                if user_input.lower() in ["exit", "quit", "bye", "退出", "再见"]:
                    print("祝您烹饪愉快！")
                    break
                
                print("\n 正在为您查找...\n")
                
                # 监控工具使用情况
                print("🤖 Agent 开始处理您的请求...")
                
                # 捕获 Agent 的输出来检测工具调用
                import io
                import contextlib
                
                # 创建一个字符串缓冲区来捕获输出
                captured_output = io.StringIO()
                
                # 执行用户请求并捕获输出
                with contextlib.redirect_stdout(captured_output):
                    cooking_expert(user_input)
                
                # 获取捕获的输出
                output = captured_output.getvalue()
                
                # 分析输出中的工具调用
                tool_calls = []
                lines = output.split('\n')
                for line in lines:
                    if line.startswith('Tool #'):
                        # 提取工具名称
                        parts = line.split(': ')
                        if len(parts) > 1:
                            tool_name = parts[1].strip()
                            tool_calls.append(tool_name)
                            print(f"🛠️  检测到工具调用: {tool_name}")
                
                # 显示 Agent 的实际输出
                if output.strip():
                    print(output)
                
                # 显示工具调用统计
                if tool_calls:
                    print(f"\n📊 本次共调用了 {len(tool_calls)} 个工具: {', '.join(tool_calls)}")
                else:
                    print("\n💭 本次没有检测到工具调用")
               
    except Exception as e:
        print(f" 查询失败: {e}")
        print("请确保美食服务正在运行: python strands_mcp_server.py")

if __name__ == "__main__":
    main()