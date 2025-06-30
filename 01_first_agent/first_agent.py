# first_agent.py
import sys
import logging
from strands import Agent
from strands_tools import current_time, http_request


#打开debug 日志 
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)


agent = Agent(
    system_prompt = """你是一个生活助手，运用科学的知识回答各种问题。
    """,
    tools=[current_time, http_request]
)


query = """
请回答以下问题:
1. 现在北京时间是几点?
2. 根据百科网站, 梅雨是什么意思?
"""


if __name__ == "__main__":
    # interactive_session()
    response = agent(query)
