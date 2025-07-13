# web_interface.py
import streamlit as st
import logging
from strands import Agent
from strands_tools import current_time, http_request
import time

# 设置页面配置
st.set_page_config(
    page_title="Strands AI助手",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 设置日志
logging.getLogger("strands").setLevel(logging.DEBUG)
logging.basicConfig(
    format="%(levelname)s | %(name)s | %(message)s",
    handlers=[logging.StreamHandler()]
)

# 初始化Agent
@st.cache_resource
def init_agent():
    return Agent(
        system_prompt="""你是一个智能生活助手，能够帮助用户解答各种问题。
        你可以：
        1. 获取当前时间信息
        2. 通过网络搜索获取最新信息
        3. 提供科学、准确的知识解答
        4. 用友好、专业的语气与用户交流
        
        请始终保持礼貌和专业，提供有用的信息。
        """,
        tools=[current_time, http_request]
    )

# 初始化会话状态
if "messages" not in st.session_state:
    st.session_state.messages = []

if "agent" not in st.session_state:
    st.session_state.agent = init_agent()

# 主界面
def main():
    st.title("🤖 Strands AI助手")
    st.markdown("---")
    
    # 侧边栏
    with st.sidebar:
        st.header("📋 功能介绍")
        st.markdown("""
        **AI助手功能：**
        - 🕐 获取当前时间
        - 🌐 网络信息搜索
        - 📚 知识问答
        - 💡 生活建议
        
        **使用方法：**
        在下方输入框中输入您的问题，AI助手将为您提供帮助。
        """)
        
        if st.button("🗑️ 清空对话历史"):
            st.session_state.messages = []
            st.rerun()
    
    # 显示对话历史
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    
    # 用户输入
    if prompt := st.chat_input("请输入您的问题..."):
        # 添加用户消息到历史
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        
        # 生成AI回复
        with st.chat_message("assistant"):
            with st.spinner("AI正在思考中..."):
                try:
                    response = st.session_state.agent(prompt)
                    st.markdown(response)
                    # 添加AI回复到历史
                    st.session_state.messages.append({"role": "assistant", "content": response})
                except Exception as e:
                    error_msg = f"抱歉，处理您的请求时出现了错误：{str(e)}"
                    st.error(error_msg)
                    st.session_state.messages.append({"role": "assistant", "content": error_msg})

# 示例问题区域
def show_examples():
    st.markdown("### 💡 试试这些问题：")
    
    col1, col2, col3 = st.columns(3)
    
    with col1:
        if st.button("🕐 现在几点了？"):
            st.session_state.messages.append({"role": "user", "content": "现在几点了？"})
            st.rerun()
    
    with col2:
        if st.button("🌤️ 今天天气怎么样？"):
            st.session_state.messages.append({"role": "user", "content": "帮我查询一下北京今天的天气情况"})
            st.rerun()
    
    with col3:
        if st.button("📚 什么是人工智能？"):
            st.session_state.messages.append({"role": "user", "content": "什么是人工智能？请详细解释一下"})
            st.rerun()

if __name__ == "__main__":
    main()
    
    # 如果没有对话历史，显示示例问题
    if not st.session_state.messages:
        show_examples()