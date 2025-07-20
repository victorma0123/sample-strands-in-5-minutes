from strands import Agent, tool
from strands_tools import file_read, file_write, editor
import json

ENGLISH_ASSISTANT_SYSTEM_PROMPT = """
你是英语大师，一个高级英语教育助手。你的能力包括：

1. 写作支持：
   - 语法和句法改进
   - 词汇增强
   - 风格和语调优化
   - 结构和组织指导

2. 分析工具：
   - 文本摘要
   - 文学分析
   - 内容评估
   - 引用协助

3. 教学方法：
   - 提供带有示例的清晰解释
   - 提供建设性反馈
   - 建议改进
   - 分解复杂概念

在所有互动中保持清晰、鼓励和教育性。始终解释你建议背后的理由，以促进学习。
"""


@tool
def english_assistant(query: str) -> str:
    """
    处理和响应英语语言、文学和写作相关的查询。
    
    参数:
        query: 用户的英语语言或文学问题
        
    返回:
        解决英语语言或文学概念的有用回应
    """
    # 为英语助手格式化查询，提供具体指导
    formatted_query = f"分析并回应这个英语语言或文学问题，在适当的地方提供带有示例的清晰解释：{query}"
    
    try:
        print("已路由至英语助手")

        english_agent = Agent(
            system_prompt=ENGLISH_ASSISTANT_SYSTEM_PROMPT,
            tools=[editor, file_read, file_write],
        )
        agent_response = english_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response
        
        return "很抱歉，我无法正确分析您的英语语言问题。您能否重新表述或提供更多上下文？"
    except Exception as e:
        # 返回英语查询的特定错误消息
        return f"处理您的英语语言查询时出错：{str(e)}"