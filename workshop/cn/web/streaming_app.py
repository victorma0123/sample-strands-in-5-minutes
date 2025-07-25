import os
import streamlit as st
from dotenv import load_dotenv
from strands import Agent, tool
import time
import warnings
import json
from typing import Dict, List, Any
import logging
from strands.models import BedrockModel

# 全局数组存储工具调用
global_tool_calls = []


# # 加载环境变量
load_dotenv()
# 忽略特定的 Streamlit 警告
warnings.filterwarnings("ignore", message=".*missing ScriptRunContext.*")
# 打开debug 日志 
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)



# 设置页面配置
st.set_page_config(
    page_title="多智能体助手",
    page_icon="🔍",
    layout="wide",
)

# 自定义CSS样式
st.markdown("""
<style>
    .tool-call-box {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
        border-left: 3px solid #4c8bf5;
    }
    .tool-name {
        font-weight: bold;
        color: #0068c9;
    }
    .tool-params {
        font-family: monospace;
        background-color: #f8f9fa;
        padding: 5px;
        border-radius: 3px;
    }
    .main-content {
        margin-bottom: 80px; /* 为固定底部留出空间 */
    }
</style>
""", unsafe_allow_html=True)

# 为不同智能体定义系统提示
RESEARCH_ASSISTANT_PROMPT = """你是一个专业的研究助手。专注于提供对研究问题的事实性、来源可靠的信息。
尽可能引用你的信息来源。请用中文回答用户的问题。"""

PRODUCT_RECOMMENDATION_PROMPT = """你是一个专业的产品推荐助手。
根据用户偏好提供个性化的产品建议。尽可能引用你的信息来源。请用中文回答用户的问题。"""

TRIP_PLANNING_PROMPT = """你是一个专业的旅行规划助手。
根据用户偏好创建的旅行行程。请用中文回答用户的问题。"""

# 定义协调器系统提示
MAIN_SYSTEM_PROMPT = """
你是一个将查询路由到专业智能体的助手：
- 对于研究问题和事实信息 → 使用 research_assistant 工具
- 对于产品推荐和购物建议 → 使用 product_recommendation_assistant 工具
- 对于旅行规划和行程 → 使用 trip_planning_assistant 工具
- 对于不需要专业知识的简单问题 → 直接回答

始终根据用户的查询选择最合适的工具。请用中文回答用户的问题。
"""

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []
if "tool_calls" not in st.session_state:
    st.session_state.tool_calls = []
    # 同步全局数组
    global_tool_calls.clear()
if "tool_calls_container" not in st.session_state:
    st.session_state.tool_calls_container = None

#model_id="us.amazon.nova-premier-v1:0",
model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="us-west-2",
    temperature=0.7
)

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
        # 确保tool_calls已初始化
        if "tool_calls" not in st.session_state:
            st.session_state.tool_calls = []
            global global_tool_calls
            global_tool_calls = []
            print (f"session 初始化了")

        # 记录工具调用
        tool_call = {
            "name": "研究助手",
            "input": query,
            "time": time.strftime("%H:%M:%S")
        }
        st.session_state.tool_calls.append(tool_call)
        # 同步到全局数组
        global_tool_calls.append(tool_call)
        # 在页面上显示使用的智能体
        st.toast(f"🔍 正在使用研究助手智能体...", icon="🔍")
        print(f"研究助手专家")

        research_agent = Agent(
            system_prompt=RESEARCH_ASSISTANT_PROMPT,
            model=model
        )
        response = research_agent(query)
        
        return str(response)
    except Exception as e:
        error_msg = f"研究助手出错: {str(e)}"
        return error_msg

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
        # 确保tool_calls已初始化
        if "tool_calls" not in st.session_state:
            st.session_state.tool_calls = []
            global global_tool_calls
            global_tool_calls = []
            print (f"session 初始化了")

        # 记录工具调用
        tool_call = {
            "name": "产品推荐助手",
            "input": query,
            "time": time.strftime("%H:%M:%S")
        }
        st.session_state.tool_calls.append(tool_call)
        # 同步到全局数组
        global_tool_calls.append(tool_call)
        
        # 在页面上显示使用的智能体
        st.toast(f"🛒 正在使用产品推荐助手智能体...", icon="🛒")
        print(f"产品推荐专家")
        
        product_agent = Agent(
            system_prompt=PRODUCT_RECOMMENDATION_PROMPT,
            model=model
        )
        response = product_agent(query)
        
        return str(response)
    except Exception as e:
        error_msg = f"产品推荐出错: {str(e)}"
        return error_msg

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
        # 确保tool_calls已初始化
        if "tool_calls" not in st.session_state:
            st.session_state.tool_calls = []
            global global_tool_calls
            global_tool_calls = []
            print (f"session 初始化了")

        # 记录工具调用
        tool_call = {
            "name": "旅行规划助手",
            "input": query,
            "time": time.strftime("%H:%M:%S")
        }
        st.session_state.tool_calls.append(tool_call)
        # 同步到全局数组
        global_tool_calls.append(tool_call)
        
        print(f"----------trip------------")
        print(st.session_state.tool_calls)
        print(f"-----------trip-----------")

        # 在页面上显示使用的智能体
        st.toast(f"✈️ 正在使用旅行规划助手智能体...", icon="✈️")
        print(f"行程规划专家")
        travel_agent = Agent(
            system_prompt=TRIP_PLANNING_PROMPT,
            model=model
        )
        response = travel_agent(query)
        
        return str(response)
    except Exception as e:
        error_msg = f"旅行规划出错: {str(e)}"
        return error_msg

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
        # 确保tool_calls已初始化
        if "tool_calls" not in st.session_state:
            st.session_state.tool_calls = []
            global global_tool_calls
            global_tool_calls = []
            print (f"session 初始化了")
            
        # 记录工具调用
        tool_call = {
            "name": "内容总结助手",
            "input": content[:100] + "...",
            "time": time.strftime("%H:%M:%S")
        }
        st.session_state.tool_calls.append(tool_call)
        # 同步到全局数组
        global_tool_calls.append(tool_call)
        
        # 在页面上显示使用的智能体
        st.toast(f"📝 正在使用内容总结助手智能体...", icon="📝")
        print(f"总结专家")

        summary_agent = Agent(
            system_prompt="""
            你是一个总结专家，专注于将复杂信息提炼为清晰、简洁的摘要。
            你的主要目标是提取关键点、主要论点和重要数据。
            你应该保持原始内容的准确性，同时使其更易于理解。
            注重清晰度、简洁性，并突出信息的最重要方面。
            请用中文回答用户的问题。
            """,
            model=model
        )
        response = summary_agent(f"请为以下内容创建简洁摘要: {content[:1000]}...")
        return str(response)
    except Exception as e:
        error_msg = f"总结出错: {str(e)}"
        return error_msg

# 创建协调器智能体
def get_orchestrator():
    return Agent(
        system_prompt=MAIN_SYSTEM_PROMPT,
        model=model,
        callback_handler=None,
        tools=[
            research_assistant,
            product_recommendation_assistant,
            trip_planning_assistant,
            summarize_content,
        ],
    )

# 模拟流式输出文本
def simulate_stream_output(text: str, message_placeholder, speed=0.2):
    # 将文本分成段落
    paragraphs = text.split('\n\n')
    full_text = ""
    
    # 逐段显示文本，模拟流式输出
    for paragraph in paragraphs:
        if not paragraph.strip():
            continue
        full_text += paragraph + "\n\n"
        message_placeholder.markdown(full_text + "▌")
        time.sleep(speed)  # 调整这个值可以改变流式输出的速度
    
    # 最终显示完整文本
    message_placeholder.markdown(full_text)
    return full_text

# Streamlit UI
st.title("🔍 多智能体助手")
st.markdown("""
本应用展示了使用Strands Agents的"智能体即工具"模式。
专业AI智能体协同工作，帮助您进行研究、产品推荐和旅行规划。
""")

# 主内容区域 - 单列布局
st.markdown('<div class="main-content">', unsafe_allow_html=True)
# 显示聊天历史
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])
st.markdown('</div>', unsafe_allow_html=True)

# 侧边栏选项
with st.sidebar:
    st.title("多智能体选项")
    agent_mode = st.radio(
        "选择交互模式:",
        ["直接查询", "顺序处理", "显示工具使用"]
    )
    
    # stream_speed = st.slider("流式输出速度", min_value=0.05, max_value=0.5, value=0.2, step=0.05, 
    #                        help="调整流式输出的速度（数值越小越快）")
    stream_speed = 0.2
    # 侧边栏信息
    st.markdown("## 智能体能力")
    st.markdown("""
    - **研究助手**: 提供有事实依据、来源可靠的信息
    - **产品推荐**: 根据用户偏好推荐产品
    - **旅行规划**: 创建旅行行程并提供建议
    - **内容总结**: 将复杂信息提炼为简洁摘要
    """)

    st.markdown("## 示例查询")
    st.markdown("""
    - 量子计算的最新进展是什么？
    - 推荐适合初学者的登山鞋
    - 帮我规划一个5天的东京之旅
    - 研究气候变化并总结关键发现
    """)
    
    # 添加清除按钮以重置聊天
    if st.button("清除聊天历史"):
        st.session_state.messages = []
        st.session_state.tool_calls = []
        st.rerun()

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
                st.toast("🤖 正在使用协调器智能体...", icon="🤖")
                # 清空之前的工具调用记录
                st.session_state.tool_calls = []
                print(f"session 初始化了")
                response = orchestrator(query)
                # print(response)

                result = str(response)
                
                # 从session_state.tool_calls中获取工具使用信息
                tool_info = "\n\n### 使用的智能体:\n"
                used_agents = []
                print(f"----------99------------")
                print(st.session_state.tool_calls)
                print(f"---------99-------------")
                print(global_tool_calls)
                print(f"---------88-------------")


                # 检查是否有工具调用记录
                if global_tool_calls:
                    for tool_call in global_tool_calls:
                        tool_name = tool_call["name"]
                        if tool_name == "研究助手" and "🔍 研究助手" not in used_agents:
                            used_agents.append("🔍 研究助手")
                        elif tool_name == "产品推荐助手" and "🛒 产品推荐助手" not in used_agents:
                            used_agents.append("🛒 产品推荐助手")
                        elif tool_name == "旅行规划助手" and "✈️ 旅行规划助手" not in used_agents:
                            used_agents.append("✈️ 旅行规划助手")
                        elif tool_name == "内容总结助手" and "📝 内容总结助手" not in used_agents:
                            used_agents.append("📝 内容总结助手")
                
                if used_agents:
                    for agent in used_agents:
                        tool_info += f"- {agent}\n"
                else:
                    tool_info += "- 🤖 协调器智能体 (直接回答)\n"
                
                result += tool_info
                
            elif agent_mode == "顺序处理":
                # 首先进行研究
                st.toast("🔄 正在执行顺序处理...", icon="🔄")
                research_response = research_assistant(query)
                
                # 然后总结研究结果
                result = summarize_content(research_response)
                result = f"**研究摘要:**\n\n{result}\n\n**详细研究:**\n\n{research_response}"
                
                # 添加工具使用信息
                result += "\n\n### 使用的智能体:\n- 🔍 研究助手\n- 📝 内容总结助手"
                
            elif agent_mode == "显示工具使用":
                # 处理查询并显示使用的工具
                st.toast("🤖 正在使用协调器智能体（显示工具使用模式）...", icon="🤖")
                # 清空之前的工具调用记录
                st.session_state.tool_calls = []
                
                response = orchestrator(query)
                result = str(response)
                
                # 从session_state.tool_calls中获取工具使用信息
                tool_info = "\n\n### 使用的智能体:\n"
                used_agents = []
                
                # 检查是否有工具调用记录
                if st.session_state.tool_calls:
                    for tool_call in st.session_state.tool_calls:
                        tool_name = tool_call["name"]
                        if tool_name == "研究助手" and "🔍 研究助手" not in used_agents:
                            used_agents.append("🔍 研究助手")
                        elif tool_name == "产品推荐助手" and "🛒 产品推荐助手" not in used_agents:
                            used_agents.append("🛒 产品推荐助手")
                        elif tool_name == "旅行规划助手" and "✈️ 旅行规划助手" not in used_agents:
                            used_agents.append("✈️ 旅行规划助手")
                        elif tool_name == "内容总结助手" and "📝 内容总结助手" not in used_agents:
                            used_agents.append("📝 内容总结助手")
                
                if used_agents:
                    for agent in used_agents:
                        tool_info += f"- {agent}\n"
                else:
                    tool_info += "- 🤖 协调器智能体 (直接回答)\n"
                
                result += tool_info
            
            end_time = time.time()
            processing_time = round(end_time - start_time, 2)
            
            # 在流式输出前先确保结果中包含智能体信息
            if "使用的智能体" not in result:
                # 从session_state.tool_calls中获取工具使用信息
                used_agents = []
                
                # 检查是否有工具调用记录
                if st.session_state.tool_calls:
                    for tool_call in st.session_state.tool_calls:
                        tool_name = tool_call["name"]
                        if tool_name == "研究助手" and "🔍 研究助手" not in used_agents:
                            used_agents.append("🔍 研究助手")
                        elif tool_name == "产品推荐助手" and "🛒 产品推荐助手" not in used_agents:
                            used_agents.append("🛒 产品推荐助手")
                        elif tool_name == "旅行规划助手" and "✈️ 旅行规划助手" not in used_agents:
                            used_agents.append("✈️ 旅行规划助手")
                        elif tool_name == "内容总结助手" and "📝 内容总结助手" not in used_agents:
                            used_agents.append("📝 内容总结助手")
                
                if used_agents:
                    agent_info = "\n\n### 使用的智能体:\n"
                    for agent in used_agents:
                        agent_info += f"- {agent}\n"
                    result += agent_info
                else:
                    result += "\n\n### 使用的智能体:\n- 🤖 协调器智能体 (直接回答)"
            
            # 模拟流式输出最终结果
            full_result = simulate_stream_output(result, message_placeholder, stream_speed)
            
            # 添加处理时间
            final_result = f"{full_result}\n\n"
            
            # 确保最终结果中包含智能体信息
            if "使用的智能体" not in final_result:
                # 从session_state.tool_calls中获取工具使用信息
                used_agents = []
                
                # 检查是否有工具调用记录
                if st.session_state.tool_calls:
                    for tool_call in st.session_state.tool_calls:
                        tool_name = tool_call["name"]
                        if tool_name == "研究助手" and "🔍 研究助手" not in used_agents:
                            used_agents.append("🔍 研究助手")
                        elif tool_name == "产品推荐助手" and "🛒 产品推荐助手" not in used_agents:
                            used_agents.append("🛒 产品推荐助手")
                        elif tool_name == "旅行规划助手" and "✈️ 旅行规划助手" not in used_agents:
                            used_agents.append("✈️ 旅行规划助手")
                        elif tool_name == "内容总结助手" and "📝 内容总结助手" not in used_agents:
                            used_agents.append("📝 内容总结助手")
                
                if used_agents:
                    agent_info = "\n\n### 使用的智能体:\n"
                    for agent in used_agents:
                        agent_info += f"- {agent}\n"
                else:
                    agent_info = "\n\n### 使用的智能体:\n- 🤖 协调器智能体 (直接回答)"
                
                final_result = f"{full_result}{agent_info}\n\n*处理用时: {processing_time} 秒*"
            
            message_placeholder.markdown(final_result)
            
            # 添加助手回应到聊天历史
            st.session_state.messages.append({"role": "assistant", "content": final_result})
            
        except Exception as e:
            error_message = f"错误: {str(e)}"
            message_placeholder.markdown(error_message)
            st.session_state.messages.append({"role": "assistant", "content": error_message})