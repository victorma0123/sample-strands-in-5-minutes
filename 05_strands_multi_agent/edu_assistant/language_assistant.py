from strands import Agent, tool
from strands_tools import http_request
import json

LANGUAGE_ASSISTANT_SYSTEM_PROMPT = """
你是语言助手，一个专门的语言翻译和学习助手。你的角色包括：

1. 翻译服务：
   - 语言间的准确翻译
   - 符合上下文的翻译
   - 习惯用语处理
   - 文化背景考虑

2. 语言学习支持：
   - 解释翻译选择
   - 突出语言模式
   - 提供发音指导
   - 文化背景解释

3. 教学方法：
   - 逐步分解翻译过程
   - 解释语法差异
   - 提供相关例子
   - 提供学习技巧

保持准确性的同时确保翻译自然且符合上下文。
"""


@tool
def language_assistant(query: str) -> str:
    """
    处理和响应语言翻译和外语学习查询。
    
    参数:
        query: 翻译或语言学习帮助的请求
        
    返回:
        带有解释的翻译文本或语言学习指导
    """
    # 为语言助手格式化查询，提供具体指导
    formatted_query = f"请处理这个翻译或语言学习请求，在有帮助的地方提供文化背景和解释：{query}"
    
    try:
        print("已路由至语言助手")
        language_agent = Agent(
            system_prompt=LANGUAGE_ASSISTANT_SYSTEM_PROMPT,
            tools=[http_request],
        )
        agent_response = language_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response

        return "很抱歉，我无法处理您的语言请求。请确保您已指定涉及的语言和具体的翻译或学习需求。"
    except Exception as e:
        # 返回语言处理的特定错误消息
        return f"处理您的语言查询时出错：{str(e)}"