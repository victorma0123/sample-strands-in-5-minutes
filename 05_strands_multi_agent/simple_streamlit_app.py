import os
import streamlit as st
from dotenv import load_dotenv
from strands import Agent, tool
import time
import warnings

# 忽略特定的 Streamlit 警告
warnings.filterwarnings("ignore", message=".*missing ScriptRunContext.*")

# 加载环境变量
load_dotenv()

# 设置页面配置
st.set_page_config(
    page_title="多智能体助手",
    page_icon="🔍",
    layout="wide",
)

# 为不同智能体定义系统提示
RESEARCH_ASSISTANT_PROMPT = """你是一个专业的研究助手。专注于提供对研究问题的事实性、来源可靠的信息。
尽可能引用你的信息来源。请用中文回答用户的问题。"""

PRODUCT_RECOMMENDATION_PROMPT = """你是一个专业的产品推荐助手。
根据用户偏好提供个性化的产品建议。尽可能引用你的信息来源。请用中文回答用户的问题。"""

TRIP_PLANNING_PROMPT = """你是一个专业的旅行规划助手。
根据用户偏好创建详细的旅行行程。请用中文回答用户的问题。"""

# 定义协调器系统提示
MAIN_SYSTEM_PROMPT = """
你是一个将查询路由到专业智能体的助手：
- 对于研究问题和事实信息 → 使用 research_assistant 工具
- 对于产品推荐和购物建议 → 使用 product_recommendation_assistant 工具
- 对于旅行规划和行程 → 使用 trip_planning_assistant 工具
- 对于不需要专业知识的简单问题 → 直接回答

始终根据用户的查询选择最合适的工具。请用中文回答用户的问题。
"""

# 定义智能体工具
@tool
def research_assistant(query: str) -> str:
    """
    处理研究相关的查询并提供回应。

    Args:
        query: 需要事实信息的研究问题

    Returns:
        带有引用的详细研究回答
    """
    try:
        research_agent = Agent(
            system_prompt=RESEARCH_ASSISTANT_PROMPT,
        )
        response = research_agent(query)
        return str(response)
    except Exception as e:
        return f"研究助手出错: {str(e)}"

@tool
def product_recommendation_assistant(query: str) -> str:
    """
    处理产品推荐查询，提供合适的产品建议。

    Args:
        query: 包含用户偏好的产品查询

    Returns:
        个性化产品推荐及理由
    """
    try:
        product_agent = Agent(
            system_prompt=PRODUCT_RECOMMENDATION_PROMPT,
        )
        response = product_agent(query)
        return str(response)
    except Exception as e:
        return f"产品推荐出错: {str(e)}"

@tool
def trip_planning_assistant(query: str) -> str:
    """
    创建旅行行程并提供旅行建议。

    Args:
        query: 包含目的地和偏好的旅行规划请求

    Returns:
        详细的旅行行程或旅行建议
    """
    try:
        travel_agent = Agent(
            system_prompt=TRIP_PLANNING_PROMPT,
        )
        response = travel_agent(query)
        return str(response)
    except Exception as e:
        return f"旅行规划出错: {str(e)}"

@tool
def summarize_content(content: str) -> str:
    """
    将提供的内容总结为简洁格式。

    Args:
        content: 要总结的文本内容

    Returns:
        内容的简洁摘要
    """
    try:
        summary_agent = Agent(
            system_prompt="""
            你是一个总结专家，专注于将复杂信息提炼为清晰、简洁的摘要。
            你的主要目标是提取关键点、主要论点和重要数据。
            你应该保持原始内容的准确性，同时使其更易于理解。
            注重清晰度、简洁性，并突出信息的最重要方面。
            请用中文回答用户的问题。
            """,
        )
        response = summary_agent(f"请为以下内容创建简洁摘要: {content}")
        return str(response)
    except Exception as e:
        return f"总结出错: {str(e)}"

# 创建协调器智能体
# 使用普通函数而不是缓存资源，避免可能的上下文问题
def get_orchestrator():
    return Agent(
        system_prompt=MAIN_SYSTEM_PROMPT,
        tools=[
            research_assistant,
            product_recommendation_assistant,
            trip_planning_assistant,
            summarize_content,
        ],
    )

# Streamlit UI
st.title("🔍 多智能体助手")
st.markdown("""
本应用展示了使用Strands Agents的"智能体即工具"模式。
专业AI智能体协同工作，帮助您进行研究、产品推荐和旅行规划。
""")

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []

# 显示聊天历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# 侧边栏选项
st.sidebar.title("多智能体选项")
agent_mode = st.sidebar.radio(
    "选择交互模式:",
    ["直接查询", "顺序处理", "显示工具使用"]
)

# 侧边栏信息
st.sidebar.markdown("## 智能体能力")
st.sidebar.markdown("""
- **研究助手**: 提供有事实依据、来源可靠的信息
- **产品推荐**: 根据用户偏好推荐产品
- **旅行规划**: 创建旅行行程并提供建议
- **内容总结**: 将复杂信息提炼为简洁摘要
""")

st.sidebar.markdown("## 示例查询")
st.sidebar.markdown("""
- 量子计算的最新进展是什么？
- 推荐适合初学者的登山鞋
- 帮我规划一个5天的东京之旅
- 研究气候变化并总结关键发现
""")

# 获取用户输入
query = st.chat_input("请输入您的问题...")

if query:
    # 添加用户消息到聊天历史
    st.session_state.messages.append({"role": "user", "content": query})
    
    # 显示用户消息
    with st.chat_message("user"):
        st.markdown(query)
    
    # 显示助手回应
    with st.chat_message("assistant"):
        message_placeholder = st.empty()
        message_placeholder.markdown("思考中...")
        
        orchestrator = get_orchestrator()
        
        try:
            # 设置环境变量以绕过工具同意
            os.environ["BYPASS_TOOL_CONSENT"] = "true"
            
            start_time = time.time()
            
            if agent_mode == "直接查询":
                # 使用协调器处理查询
                response = orchestrator(query)
                result = str(response)
                
            elif agent_mode == "顺序处理":
                # 首先进行研究
                research_response = research_assistant(query)
                
                # 然后总结研究结果
                result = summarize_content(research_response)
                result = f"**研究摘要:**\n\n{result}\n\n**详细研究:**\n\n{research_response}"
                
            elif agent_mode == "显示工具使用":
                # 处理查询并显示使用的工具
                response = orchestrator(query)
                result = str(response)
                
                # 添加工具使用信息
                tool_info = ""
                for message in orchestrator.messages:
                    if message["role"] == "assistant" and "tool_calls" in message:
                        for tool_call in message["tool_calls"]:
                            tool_info += f"\n\n*使用了工具: {tool_call['function']['name']}*"
                
                result += tool_info
            
            end_time = time.time()
            processing_time = round(end_time - start_time, 2)
            
            # 更新占位符显示结果
            message_placeholder.markdown(f"{result}\n\n*处理用时: {processing_time} 秒*")
            
            # 添加助手回应到聊天历史
            st.session_state.messages.append({"role": "assistant", "content": f"{result}\n\n*处理用时: {processing_time} 秒*"})
            
        except Exception as e:
            error_message = f"错误: {str(e)}"
            message_placeholder.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})

# 添加清除按钮以重置聊天
if st.sidebar.button("清除聊天历史"):
    st.session_state.messages = []
    st.rerun()  # 使用 st.rerun() 替代已弃用的 st.experimental_rerun()