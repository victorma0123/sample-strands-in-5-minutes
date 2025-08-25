# web_interface.py
import streamlit as st
import asyncio
import logging
from strands import Agent
from strands.models import BedrockModel
from strands_tools import current_time, http_request
from strands.models.ollama import OllamaModel

logging.basicConfig(
    level=logging.INFO,
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)
logging.getLogger("strands").setLevel(logging.DEBUG)

# 设置页面配置
st.set_page_config(
    page_title="Strands Agents 小助手",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 自定义CSS样式
st.markdown("""
<style>
    .tool-call-box {
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
        margin-bottom: 10px;
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
</style>
""", unsafe_allow_html=True)

# 可用的模型配置


# 初始化Agent
def init_agent(model_id="qwen3:1.7b"):
    try:
        model = OllamaModel(
            host="http://127.0.0.1:11434",
            model_id=model_id
        )
        return Agent(
            system_prompt="""
            你是一个中国国内的生活助手，运用科学的知识回答各种问题。
            如果用户问问题，请尽量调用 http_request 工具查询中国国内的百科网站。
            """,
            model=model,
            tools=[current_time, http_request],
            callback_handler=None
        )
    except Exception as e:
        # 这里抛给上层，由界面展示友好提示
        raise RuntimeError(
            f"初始化本地模型失败：{e}\n"
            "请确认已安装并启动 Ollama（`ollama serve`），且已 pull 对应模型（如 `ollama pull qwen3:1.7b`）。"
        )


# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []

if "selected_model" not in st.session_state:
    st.session_state.selected_model = "qwen3:1.7b"  # 默认模型

if "agent" not in st.session_state:
    st.session_state.agent = init_agent(st.session_state.selected_model)

async def process_user_input_streaming(prompt):
    """使用异步流式处理用户输入"""
    try:
        # 使用异步流式输出
        full_response = ""
        async for event in st.session_state.agent.stream_async(prompt):
            if "data" in event:
                # 累积文本
                full_response += event["data"]
        
        # 返回完整响应
        return full_response
        
    except Exception as e:
        return f"抱歉，处理您的请求时出现了错误：{str(e)}"

def process_user_input(prompt):
    """处理用户输入（用于示例按钮）"""
    try:
        # 添加用户消息到历史
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        logging.info("prompt 是：" +prompt) 
        response = st.session_state.agent(prompt)

        # 添加AI回复到历史
        st.session_state.messages.append({"role": "assistant", "content": response})
        
        return True
        
    except Exception as e:
        error_msg = f"抱歉，处理您的请求时出现了错误：{str(e)}"
        st.session_state.messages.append({"role": "assistant", "content": error_msg})
        return False

def main():
    st.title("Strands AI助手")
    st.markdown("---")
    
    # 侧边栏
    with st.sidebar:
        st.header("功能介绍")
        st.markdown("""
        **AI助手功能：**
        - 获取当前时间
        - 网络信息搜索
        - 知识问答
        - 生活建议
        
        **使用方法：**
        在下方输入框中输入您的问题，AI助手将为您提供帮助。
        """)
        
        # 示例问题放在侧边栏（只展示，不能点击）
        st.markdown("---")
        st.markdown("**试试这些问题：**")
        
        # 使用普通文本显示示例问题，确保每个问题单独一行
        st.markdown("• 现在几点了？")
        st.markdown("• 帮我查询一下北京今天的天气情况")
        st.markdown("• 什么是梅雨？请详细解释一下")
        
        # 添加提示
        st.caption("在输入框中输入上述问题来获取回答")
        
        st.markdown("---")
        
        # 模型选择下拉框
        st.subheader("模型选择")
        OLLAMA_MODELS = ["qwen3:1.7b"]  # 以后可扩展，如 ["qwen3:1.7b", "mistral", "gemma:2b"]
        selected_model = st.selectbox(
            "选择模型",
            options=OLLAMA_MODELS,
            index=OLLAMA_MODELS.index(st.session_state.get("selected_model", "qwen3:1.7b"))
        )

        # 如果模型选择改变，重新初始化Agent
        if selected_model != st.session_state.get("selected_model"):
            st.session_state.selected_model = selected_model
            try:
                st.session_state.agent = init_agent(selected_model)
                st.success(f"已切换到 {selected_model} 模型")
                st.rerun()  # 触发重绘，避免旧会话与新模型混用
            except Exception as e:
                st.error(str(e))
        
        st.markdown("---")
        if st.button("清空对话历史"):
            st.session_state.messages = []
            st.rerun()
    
    # 显示对话历史
    st.subheader("对话区域")
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

# 输入框处理
def render_chat_input():
    """渲染聊天输入框"""
    if prompt := st.chat_input("请输入您的问题..."):
        # 先添加用户消息到历史
        st.session_state.messages.append({"role": "user", "content": prompt})
        
        # 显示用户消息
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 创建两列布局
        col1, col2 = st.columns([3, 1])
        
        # 创建AI回复的占位符
        with col1, st.chat_message("assistant"):
            message_placeholder = st.empty()
            
            # 创建工具调用显示区域
            with col2:
                tool_placeholder = st.empty()
                tool_calls = []
            
            # 异步获取流式响应
            async def get_streaming_response():
                full_response = ""
                try:
                    async for event in st.session_state.agent.stream_async(prompt):
                        # 处理文本事件
                        if "data" in event:
                            full_response += event["data"]
                            message_placeholder.markdown(full_response + "▌")
                        
                        # 处理工具调用事件
                        if "current_tool_use" in event:
                            tool_info = event["current_tool_use"]
                            tool_name = tool_info.get("name", "未知工具")
                            tool_input = tool_info.get("input", {})
                            
                            # 记录工具调用
                            if tool_name not in [t["name"] for t in tool_calls]:
                                tool_calls.append({
                                    "name": tool_name,
                                    "input": tool_input
                                })
                            
                            # 更新工具调用显示
                            tool_html = "<div style='background-color:#f0f2f6;padding:10px;border-radius:5px;'>"
                            tool_html += "<h4>工具调用:</h4>"
                            for i, tool in enumerate(tool_calls):
                                tool_html += f"<p><b>{i+1}. {tool['name']}</b></p>"
                            tool_html += "</div>"
                            tool_placeholder.markdown(tool_html, unsafe_allow_html=True)
                    
                    # 移除光标
                    message_placeholder.markdown(full_response)
                    return full_response
                except Exception as e:
                    error_msg = f"抱歉，处理您的请求时出现了错误：{str(e)}"
                    message_placeholder.markdown(error_msg)
                    return error_msg
            
            # 运行异步函数并获取结果
            response = asyncio.run(get_streaming_response())
            
            # 添加AI回复到历史
            st.session_state.messages.append({"role": "assistant", "content": response})

if __name__ == "__main__":
    main()
    render_chat_input()