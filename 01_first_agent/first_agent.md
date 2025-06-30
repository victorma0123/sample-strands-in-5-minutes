
# Strands in 5 minutes  
大家好，欢迎来到5分钟上手Strands系列！
今天我们将使用Strands Agents 5分钟内带你完成，第一个AI Agent。

## 核心概念

![Agentic Loop](../images/01_first_agent/agentic-loop.png)
Strands Agents SDK 是亚马逊云科技推出的基于模型驱动的AI Agent SDK，几行代码就可以快速构建和运行Agentic AI 应用。它包含以下核心组件：
- **模型（Model）**
  - 作为Agent的推理引擎，支持多个模型平台，包括Amazon Bedrock, Anthropic, LiteLLM, Llama API, Ollama以及OpenAI等等
  - 示例模型配置：
    ```
    from strands.models import BedrockModel
    model = BedrockModel(model_id="us.anthropic.claude-3-7-sonnet-20250219-v1:0", region_name='us-east-1')
    ```

- **工具（Tools）**
  - 预置20+工具（计算器、HTTP请求、记忆以及多模型协作等）
  - 使用`@tool`装饰器快速集成自定义函数：
    ```
    from strands import tool
    @tool
    def file_analyzer(path: str) -> dict:
        """文件分析工具"""
        # 实现文件解析逻辑
        return analysis_result
    ```

- **提示词（Prompt）**
  - 系统提示定义Agent行为准则：
    ```
    SYSTEM_PROMPT = """你是一个数据分析专家，使用工具处理数据并生成可视化报告：
    1. 优先使用pandas进行数据清洗
    2. 使用matplotlib创建交互式图表
    3. 输出Markdown格式报告"""
    ```

***

## 1. 准备工作
- **拥有 AWS 账户,并在Amazon Bedrock 中启用 Claude 3.7 模型访问权限**

## 2. 环境搭建
### 2.1 Python环境配置

**Python 3.10 或更高版本**
**创建并激活 Python 虚拟环境**
```bash
python -m venv venv
source .venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```
查看python版本
```
python -v
```

**安装必要的依赖**

```bash
uv pip install strands-agents strands-agents-tools
```

### 2.2 环境变量配置
1. 创建`.env`文件并添加以下内容：
```
AWS_ACCESS_KEY_ID=你的访问密钥ID
AWS_SECRET_ACCESS_KEY=你的秘密访问密钥
AWS_DEFAULT_REGION=你的默认区域（如us-east-1）
```
### 2.2 环境变量配置
运行代码
```
python3 first_agent.py
```

## 总结
- **易于上手**：只需几行代码即可创建功能强大的 Agent。
- **广泛的工具**：超过20个内置工具可以轻松的集成。
- **模型友好**：支持多个模型平台。

这样，你就成功创建了第一个基于 Strands Agents SDK 的 AI Agent！

