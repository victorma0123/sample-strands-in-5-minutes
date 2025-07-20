# Strands AI助手 Web应用 

**难度级别：** ⭐⭐☆☆☆ (初级到中级)

## Workshop 简介

本Workshop将指导您构建一个基于Strands Agents SDK的AI助手Web应用。您将学习如何将强大的AI模型与实用工具结合，并通过直观的Web界面呈现给用户。

在这个Workshop中，您将：
- 了解Strands Agents SDK的核心概念和工作原理
- 学习如何使用工具增强AI助手的能力
- 掌握如何使用Streamlit构建交互式Web界面
- 实现流式输出和工具调用可视化
- 配置多种Amazon Bedrock模型并进行切换

无论您是AI开发新手还是有经验的开发者，这个Workshop都将帮助您快速上手构建实用的AI应用。完成后，您将拥有一个功能完整的AI助手Web应用，可以回答问题、获取实时信息，并通过浏览器与用户交互。

这个Web应用是基于Strands Agents SDK构建的AI助手，提供了一个友好的用户界面，让您可以通过浏览器与AI助手进行交互。

## 功能特点

- 💬 实时对话界面
- 🔄 流式输出（打字效果）
- 🛠️ 工具调用显示
- 🔄 多模型支持（Amazon Bedrock）
- 📱 响应式设计

## 运行环境要求

- Python 3.10 或更高版本
- AWS账户（已启用Bedrock模型访问权限）
- AWS凭证配置

## 安装步骤

1. **安装uv（如果尚未安装）**

   ```bash
   # 使用pip安装uv
   pip install uv
   
   # 或使用curl安装（Linux/macOS）
   curl -sSf https://install.astral.sh | sh
   ```

2. **使用uv创建虚拟环境并安装依赖**

   ```bash
   # 创建并激活虚拟环境
   uv venv
   source .venv/bin/activate  # Linux/Mac
   # 或
   .venv\Scripts\activate     # Windows
   
   # 安装依赖
   uv pip install -r requirements.txt
   ```

3. **配置AWS凭证**

   创建`.env`文件并添加以下内容：
   ```
   AWS_ACCESS_KEY_ID=你的访问密钥ID
   AWS_SECRET_ACCESS_KEY=你的秘密访问密钥
   AWS_DEFAULT_REGION=你的默认区域（如us-east-1）
   ```

   或者使用AWS CLI配置：
   ```bash
   aws configure
   ```

## 运行应用

确保您在虚拟环境中，然后运行：

```bash
# 方法1：使用Streamlit直接运行
streamlit run ../web_interface.py

# 方法2：使用启动脚本
python run_web.py
```

> **注意**：如果您在workshop目录中运行，请确保使用正确的路径指向web_interface.py文件。

启动后，在浏览器中访问：http://localhost:8501

## 使用指南

1. **选择模型**：在侧边栏中选择要使用的AI模型
2. **输入问题**：在底部输入框中输入您的问题
3. **查看回复**：AI助手会实时生成回复
4. **工具调用**：右侧会显示AI使用的工具
5. **清空历史**：使用侧边栏中的"清空对话历史"按钮

## 示例问题

- "现在几点了？"
- "帮我查询一下北京今天的天气情况"
- "什么是梅雨？请详细解释一下"

## 故障排除

- **模型访问错误**：确保您的AWS账户已启用相应的Bedrock模型访问权限
- **凭证问题**：检查AWS凭证配置是否正确
- **依赖问题**：确保所有依赖已正确安装
- **uv相关问题**：如果遇到uv安装或使用问题，请参考[uv官方文档](https://github.com/astral-sh/uv)

## 自定义开发

如需修改或扩展此应用：

- `web_interface.py` - 主应用文件
- `run_web.py` - 启动脚本
- `requirements.txt` - 依赖列表

可以修改系统提示、添加新工具或调整UI布局来满足您的需求。

## 学习目标

完成本Workshop后，您将能够：

1. ✅ 使用Strands Agents SDK创建智能AI助手
2. ✅ 集成和使用工具扩展AI能力
3. ✅ 构建响应式Streamlit Web界面
4. ✅ 实现流式输出和实时工具调用显示
5. ✅ 配置和切换不同的大语言模型
6. ✅ 部署一个完整的AI助手应用

## 进阶挑战

如果您已完成基本实现，可以尝试以下进阶任务：

- 🚀 添加更多自定义工具（如文件处理、数据分析等）
- 🚀 实现对话历史保存和加载功能
- 🚀 添加用户认证和多用户支持
- 🚀 优化UI/UX设计，添加主题切换
- 🚀 部署到云服务（如AWS App Runner或EC2）

---

祝您使用愉快！如有问题，请参考[Strands Agents SDK文档](https://github.com/aws/strands-agents)。