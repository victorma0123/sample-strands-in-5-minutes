# Strands Agents in 5 Minutes / 5分钟上手Strands系列

[English](README_EN.md) | 中文

## 项目介绍
欢迎来到"5分钟上手Strands系列"教程！这是一个专注于提升用户和开发者构建AI Agent能力的系列教程。通过简洁的5分钟教程形式，帮助您快速掌握Strands Agent的设计、开发、集成和部署流程。

## 教程目标
- 通过系列教程提升用户/开发者的Agent构建能力，确保学习的连续性
- 掌握Strands Agent应用的设计、开发、集成和部署的基础流程
- 使用户能够独立开发和部署自己的Agent Demo

## 课程体系
按照L100-L400级别划分，循序渐进地介绍：

### L100 - 基础概念
- Strands Agent的核心组件
- 基本工作流程
- 快速启动示例

### L200 - 进阶应用
- 会话管理
- 工具集成
- Web服务对接

### L300 - 高级特性
- 状态持久化
- 安全与监控
- 性能优化

### L400 - 扩展开发
- MCP协议扩展
- 自定义工具开发
- 最佳实践

## 教程特点
- **简洁高效**: 每节课程控制在5分钟内，突出重点
- **理论结合实践**: 每个概念都配有实际的示例代码
- **循序渐进**: 从基础到进阶，层层递进
- **动手实践**: 每节课程都包含可运行的Demo

## 快速开始

### 环境要求
- Python 3.10或更高版本
- AWS账户（用于访问Amazon Bedrock中的Claude 3.7模型）

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
- [第一课：构建你的第一个Agent](01_first_agent/first_agent.md)
- 更多课程陆续添加中...

## 参与贡献
欢迎提交Pull Request来帮助改进这个教程系列！

## 安全
更多信息请参见 [CONTRIBUTING](CONTRIBUTING.md) 文件。

## 许可证
本库采用 MIT-0 许可证。详见 [LICENSE](LICENSE) 文件。
