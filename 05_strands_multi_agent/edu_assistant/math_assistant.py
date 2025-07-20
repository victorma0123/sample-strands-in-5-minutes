from strands import Agent, tool
from strands_tools import calculator
import json

MATH_ASSISTANT_SYSTEM_PROMPT = """
你是数学向导，一个专门的数学教育助手。你的能力包括：

1. 数学运算：
   - 算术计算
   - 代数问题解决
   - 几何分析
   - 统计计算

2. 教学工具：
   - 逐步问题解决
   - 视觉解释创建
   - 公式应用指导
   - 概念分解

3. 教育方法：
   - 展示详细的解题过程
   - 解释数学推理
   - 提供替代解决方案
   - 将概念与现实世界应用联系起来

专注于清晰和系统的问题解决，同时确保学生理解基本概念。
"""


@tool
def math_assistant(query: str) -> str:
    """
    使用专业数学agent处理和响应与数学相关的查询。
    
    参数:
        query: 用户的数学问题或问题
        
    返回:
        带有解释和步骤的详细数学答案
    """
    # 为数学agent格式化查询，提供明确的指令
    formatted_query = f"请解决以下数学问题，显示所有步骤并清晰解释概念：{query}"
    
    try:
        print("已路由至数学助手")
        # 创建具有计算器功能的数学agent
        math_agent = Agent(
            system_prompt=MATH_ASSISTANT_SYSTEM_PROMPT,
            tools=[calculator],
        )
        agent_response = math_agent(formatted_query)
        text_response = str(agent_response)

        if len(text_response) > 0:
            return text_response

        return "很抱歉，我无法解决这个数学问题。请检查您的问题是否表述清晰或尝试重新表述。"
    except Exception as e:
        # 返回数学处理的特定错误消息
        return f"处理您的数学查询时出错：{str(e)}"