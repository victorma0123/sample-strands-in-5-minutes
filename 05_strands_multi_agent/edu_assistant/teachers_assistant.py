#!/usr/bin/env python3
"""
# 📁 教学助手 Strands Agent

一个专门的Strands agent，作为协调器利用其可用的子agents和工具来回答用户查询。

## 这个示例展示了什么

"""

from strands import Agent
from strands_tools import file_read, file_write, editor
from english_assistant import english_assistant
from language_assistant import language_assistant
from math_assistant import math_assistant
from computer_science_assistant import computer_science_assistant
from no_expertise import general_assistant


# Define a focused system prompt for file operations
TEACHER_SYSTEM_PROMPT = """
你是教学助手，一个复杂的教育协调器，旨在协调多个学科的教育支持。你的角色是：

1. 分析传入的学生查询并确定最合适的专业agent来处理它们：
   - 数学Agent：用于数学计算、问题和概念
   - 英语Agent：用于写作、语法、文学和作文
   - 语言Agent：用于翻译和语言相关查询
   - 计算机科学Agent：用于编程、算法、数据结构和代码执行
   - 通用助手：用于这些专业领域之外的所有其他主题

2. 主要职责：
   - 准确按学科领域分类学生查询
   - 将请求路由到适当的专业agent
   - 维护上下文并协调多步骤问题
   - 当需要多个agent时确保回应的连贯性

3. 决策协议：
   - 如果查询涉及计算/数字 → 数学Agent
   - 如果查询涉及写作/文学/语法 → 英语Agent
   - 如果查询涉及翻译 → 语言Agent
   - 如果查询涉及编程/编码/算法/计算机科学 → 计算机科学Agent
   - 如果查询在这些专业领域之外 → 通用助手
   - 对于复杂查询，根据需要协调多个agent

在路由之前始终确认你的理解，以确保准确的协助。
用中文交流
"""

# Create a file-focused agent with selected tools
teacher_agent = Agent(
    system_prompt=TEACHER_SYSTEM_PROMPT,
    callback_handler=None,
    tools=[math_assistant, language_assistant, english_assistant, computer_science_assistant, general_assistant],
)


# Example usage
if __name__ == "__main__":
    print("\n📁 教学助手 Strands Agent 📁\n")
    print("在任何学科领域提出问题，我会将其路由到适当的专家。")
    print("输入'exit'退出。")

    # Interactive loop
    while True:
        try:
            user_input = input("\n> ")
            if user_input.lower() == "exit":
                print("\n再见！👋")
                break

            response = teacher_agent(
                user_input, 
            )
            
            # Extract and print only the relevant content from the specialized agent's response
            content = str(response)
            print(content)
            
        except KeyboardInterrupt:
            print("\n\n执行被中断。正在退出...")
            break
        except Exception as e:
            print(f"\n发生错误：{str(e)}")
            print("请尝试提出不同的问题。")