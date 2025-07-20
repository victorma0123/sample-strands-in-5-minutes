from strands import Agent, tool
from strands_tools import python_repl, shell, file_read, file_write, editor
import json

COMPUTER_SCIENCE_ASSISTANT_SYSTEM_PROMPT = """
你是计算机科学专家，一个专门用于计算机科学教育和编程的助手。你的能力包括：

1. 编程支持：
   - 代码解释和调试
   - 算法开发和优化
   - 软件设计模式实现
   - 编程语言语法指导

2. 计算机科学教育：
   - 理论概念解释
   - 数据结构和算法教学
   - 计算机架构基础
   - 网络和安全原则

3. 技术支持：
   - 实时代码执行和测试
   - Shell命令指导和执行
   - 文件系统操作和管理
   - 代码编辑和改进建议

4. 教学方法：
   - 带有示例的逐步解释
   - 渐进式概念构建
   - 通过代码执行进行互动学习
   - 实际应用演示

专注于提供清晰、实用的解释，通过可执行示例演示概念。尽可能使用代码执行工具来说明概念。
"""


@tool
def computer_science_assistant(query: str) -> str:
    """
    使用具有代码执行能力的专业agent处理和响应计算机科学和编程相关问题。
    
    参数:
        query: 用户的计算机科学或编程问题
        
    返回:
        解决计算机科学概念或代码执行结果的详细回应
    """
    # 为计算机科学agent格式化查询，提供明确的指令
    formatted_query = f"请解答这个计算机科学或编程问题。在适当的情况下，提供可执行的代码示例并彻底解释概念：{query}"
    
    try:
        print("已路由至计算机科学助手")
        # 创建具有相关工具的计算机科学agent
        cs_agent = Agent(
            system_prompt=COMPUTER_SCIENCE_ASSISTANT_SYSTEM_PROMPT,
            tools=[python_repl, shell, file_read, file_write, editor],
        )
        agent_response = cs_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response
        
        return "很抱歉，我无法处理您的计算机科学问题。请尝试重新表述或提供更多关于您想学习或完成的内容的具体细节。"
    except Exception as e:
        # 返回计算机科学处理的特定错误消息
        return f"处理您的计算机科学查询时出错：{str(e)}"