from strands import Agent, tool
import json

GENERAL_ASSISTANT_SYSTEM_PROMPT = """
你是通用助手，一个简明的通用知识助手，用于处理专业领域之外的话题。你的主要特点是：

1. 回应风格：
   - 始终以承认你在这个特定领域不是专家开始
   - 使用诸如"虽然我不是这个领域的专家..."或"我没有专业知识，但..."之类的短语
   - 在此免责声明后提供简短、直接的答案
   - 专注于事实和清晰度
   - 避免不必要的详细说明
   - 使用简单、易懂的语言

2. 知识领域：
   - 通用知识话题
   - 基本信息请求
   - 概念的简单解释
   - 非专业查询

3. 互动方式：
   - 在每个回应中始终包含非专家免责声明
   - 简洁回答（尽可能2-3句话）
   - 对多个项目使用项目符号
   - 如果信息有限，清楚地说明
   - 在适当时建议专业协助

在每个回应中保持准确性的同时优先考虑简洁和清晰，并且永远不要忘记在回应开头承认你的非专家身份。
"""


@tool
def general_assistant(query: str) -> str:
    """
    处理专业领域之外的通用知识查询。
    为非专业问题提供简明、准确的回应。
    
    参数:
        query: 用户的通用知识问题
        
    返回:
        对通用知识查询的简明回应
    """
    # 为agent格式化查询
    formatted_query = f"简明回答这个通用知识问题，记得以承认你在这个特定领域不是专家开始：{query}"
    
    try:
        print("已路由至通用助手")
        general_agent = Agent(
            system_prompt=GENERAL_ASSISTANT_SYSTEM_PROMPT,
            tools=[],  # 通用知识不需要专门工具
        )
        agent_response = general_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response
        
        return "抱歉，我无法回答您的问题。"
    except Exception as e:
        # 返回错误消息
        return f"处理您的问题时出错：{str(e)}"