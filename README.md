# Strands Agents in 5 Minutes / 5分钟上手Strands系列

[English](README_EN.md) | 中文

## 项目介绍
欢迎来到"5分钟上手Strands系列"教程！这是一个专注于提升用户和开发者构建AI Agent能力的系列教程。通过简洁的5分钟教程形式，帮助您快速掌握Strands Agent的设计、开发、集成和部署流程。

🚀 **从零到一**: 从基础概念到复杂多智能体系统的完整学习路径  
🛠️ **实战导向**: 每个教程都包含可运行的Demo和实际应用场景  
🌐 **现代化界面**: 提供命令行和Web界面两种交互方式  
🔧 **模块化设计**: 支持MCP协议、A2A远程协作、Dify工作流等扩展能力  

## 教程目标
- **能力提升**: 通过系列教程提升用户/开发者的Agent构建能力，确保学习的连续性
- **全流程掌握**: 掌握Strands Agent应用的设计、开发、集成和部署的基础流程
- **独立开发**: 使用户能够独立开发和部署自己的Agent Demo
- **企业级应用**: 学会构建可扩展、可维护的多智能体协作系统

## 课程体系
| No. | Session | Description | Demo | Duration | Level | 目录 |
|-----|---------|-------------|------|----------|-------|------|
| 1 | Strands SDK 第一个 Agent | Strands 核心架构 模型/工具/提示、安装 Strands SDK、创建并运行第一个 Strands Agent | 用 Python 代码输出 Strands Agent 的核心组件说明，安装 SDK，运行一个 Strands Agent，包含命令行和Web界面两种运行方式 | 5 min | L100 | [01_first_agent](01_first_agent/) |
| 2 | Strands 会话管理与状态维护 | Strands Loop 简介、会话历史、会话窗口、多轮对话实现 | 用 Strands 实现多轮对话，保存并打印会话历史，演示滑动窗口会话管理 | 5 min | L200 | [02_strands_session](02_strands_session/) |
| 3 | Strands 构建自定义的 tool和使用 | Strands 内置工具调用，工具自定义定义与注册 | 开发一个自定义工具（如天气查询）并集成到 Strands Agent，在 Strands Agent 中注册并调用内置工具（如计算器） | 5 min | L200 | [03_strands_tooluse](03_strands_tooluse/) |
| 4 | Strands 融合 MCP | Strands 中对于MCP Server的发现，集成和使用 | 通过MCP方式注册多个MCP Server 到Agent 并实现调用，构建美食菜谱智能Agent | 5 min | L200 | [04_strands_mcp](04_strands_mcp/) |
| 5 | Strands 多智能体系统 | Multi-Agent系统的四种实现方式：Agents as Tools、Agent Swarms、Agent Graphs、Agent Workflows | 实现多智能体协作系统，包含研究助手、产品推荐、旅行规划等专业Agent，支持Streamlit Web界面 | 10 min | L300 | [05_strands_multi_agent](05_strands_multi_agent/) |
| 6 | Strands 与A2A 协议 | 使用A2A协议封装 Strands Agents 实现 Agents 远程协作 | 用Strands 和 A2A SDK开发 remote agents和client agent，实现multi agents 远程协作 | 5 min | L300 | [06_a2a_agents](06_a2a_agents/) |

## 实际应用演示 (Demo)
| No. | Demo Name | Description | Application Scenario | Duration | 目录 |
|-----|-----------|-------------|---------------------|----------|------|
| 1 | Strands 与 Dify 工作流集成 | Strands 中接入作为 MCP 服务的 dify 工作流 | 将dify工作流作为mcp接入strands agent，构建一个患者接收分诊agent。基于Strands Web UI开发，使用Python MCP SDK 实现 Dify workflow mcp | 5 min | [demo/difymcp_strandsagent_demo](demo/difymcp_strandsagent_demo/) |
| 2 | Unity Strands Agent 插件 | 基于 Strands SDK 的 Unity 编辑器 AI 插件，通过 Python.NET 集成，支持 MCP 协议扩展 | 在 Unity 编辑器中直接与 AI 对话，获得 Unity 开发问题解答、学习指导和项目分析建议 | 5 min | [demo/unity-strands-agent](demo/unity-strands-agent/) |

## 教程特点
- **简洁高效**: 每节控制在5分钟内，快速上手
- **理论结合实践**: 每个概念都配有实际的Demo和应用场景
- **循序渐进**: 从基础到进阶，层层递进的学习路径
- **动手实践**: 每节课程都包含可运行的代码和详细说明
- **现代化体验**: 支持Web界面交互，提供流式输出和实时反馈
- **企业级架构**: 涵盖多智能体协作、远程通信、工作流集成等高级特性

## 技术栈与特性

### 🧠 核心技术
- **Strands Agents SDK**: 亚马逊云科技推出的AI Agent开发框架
- **Amazon Bedrock**: 支持Claude 3.7等先进大语言模型
- **MCP协议**: 模型上下文协议，实现Agent与外部服务的标准化交互
- **A2A协议**: Agent-to-Agent通信协议，支持分布式Agent协作

### 🎨 用户界面
- **简洁的页面**: 现代化Web界面，支持实时交互和流式输出
- **命令行界面**: 轻量级CLI工具，适合开发和调试
- **响应式设计**: 支持桌面和移动端访问

### 🔧 扩展能力
- **自定义工具**: 使用`@tool`装饰器快速集成自定义函数
- **MCP服务器**: 支持构建和连接外部MCP服务，包含FastMCP快速开发
- **多智能体架构**: 四种不同的多Agent实现模式（Tools、Swarms、Graphs、Workflows）
- **工作流集成**: 支持Dify等第三方工作流平台
- **远程协作**: A2A协议支持分布式Agent部署和通信
- **多模型支持**: 兼容Amazon Bedrock、SiliconFlow、OpenAI等多种模型服务

## 快速开始

### 环境要求
- Python 3.10或更高版本
- 亚马逊云科技账户（用于访问Amazon Bedrock中的Claude 3.7模型）

### 环境搭建
1. 创建并激活Python虚拟环境：
```bash
python -m venv venv
source .venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. 安装依赖：
```bash
uv pip install strands-agents strands-agents-tools
```

### 配置
创建`.env`文件并添加以下内容：
```
AWS_ACCESS_KEY_ID=你的访问密钥ID
AWS_SECRET_ACCESS_KEY=你的秘密访问密钥
AWS_DEFAULT_REGION=你的默认区域（如us-east-1）
```

### 运行示例
```bash
python3 first_agent.py
```

## 课程导航

### 基础课程 (L100-L200)
- [第一课：构建你的第一个Agent](01_first_agent/first_agent.md) - 快速入门Strands SDK
- [第二课：Strands 会话管理与状态维护](02_strands_session/) - 实现多轮对话和会话历史
- [第三课：Strands 构建自定义的 tool和使用](03_strands_tooluse/) - 自定义工具开发与集成
- [第四课：Strands 融合 MCP](04_strands_mcp/README.md) - 模型上下文协议集成

### 进阶课程 (L300)
- [第五课：Strands 多智能体系统](05_strands_multi_agent/README.md) - 构建协作式多Agent系统
- [第六课：Strands 与A2A 协议](06_a2a_agents/) - 实现Agent间远程协作

### 实际应用演示 (Demo)
- [Demo1：Strands 与 Dify 工作流集成](demo/difymcp_strandsagent_demo/) - 患者分诊智能Agent系统
- [Demo2：Unity Strands Agent 插件](demo/unity-strands-agent/) - Unity 编辑器 AI 助手插件

### 特色功能
- **Web界面支持**: 第一课和第五课提供基于Streamlit的Web交互界面
- **多种运行方式**: 支持命令行和Web界面两种运行模式
- **实际应用场景**: 涵盖研究助手、产品推荐、旅行规划、美食菜谱、教育辅导、金融分析等实用场景
- **中国区支持**: 提供专门的中国区教程，支持硅基流动等国内模型服务

### 🇨🇳 中国区专属内容
- **[Workshop教程](workshop/cn/)**: 专为中国区用户设计的Jupyter Notebook教程
- **硅基流动集成**: 支持使用SiliconFlow提供的DeepSeek等模型
- **本地化部署**: 适配亚马逊云科技北京、宁夏区域
- **中文文档**: 完整的中文教程和说明文档

### 🌟 应用示例
- **A2A远程协作**: 支持Agent间的远程通信和协作，包含React UI界面
- **Dify工作流集成**: 将Dify工作流作为MCP服务集成到Strands Agent
- **患者分诊系统**: 基于Dify MCP的医疗领域智能分诊应用
- **Unity开发助手**: 基于Strands SDK的Unity编辑器AI插件，支持MCP协议扩展
- **多模态支持**: 支持文本、语音、图像等多种输入输出模式

## 参与贡献
欢迎提交Pull Request来帮助改进这个教程系列！

## 安全
更多信息请参见 [CONTRIBUTING](CONTRIBUTING.md) 文件。

## 许可证
本库采用 MIT-0 许可证。详见 [LICENSE](LICENSE) 文件。

