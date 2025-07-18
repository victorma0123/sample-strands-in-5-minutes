# Strands Agents 动手实验（亚马逊云科技中国区）

本目录包含两个 Jupyter Notebook，用于快速学习如何使用 Strands Agents SDK 构建 AI 智能体。这些教程专为中国区用户设计，提供了从基础到进阶的 Strands Agents 开发指南。这些教程中的 Agent 应用部署在**亚马逊云科技北京、宁夏区域**，并使用 **SiliconFlow（硅基流动）** 提供的模型作为Agent的推理引擎。

## 教程内容

### 1. [first-agent-cn.ipynb](./first-agent-cn.ipynb)

**5分钟构建你的第一个 AI 智能体**

这个入门级教程涵盖：
- Strands Agents SDK 的核心概念（模型、工具、提示词）
- 如何配置和初始化 AI 智能体
- 使用 SiliconFlow（硅基流动）提供的模型作为智能体的推理引擎
- 基本工具的使用和自定义
- 与智能体进行简单交互

适合对象：初次接触 AI 智能体开发的开发者，希望快速了解 Strands Agents 基础功能的用户。

### 2. [agent-as-tools-cn.ipynb](./agent-as-tools-cn.ipynb)

**智能体作为工具的多智能体架构模式**

这个进阶教程探讨：
- "Agents as Tools"（工具型智能体）架构模式
- 如何构建专业化智能体并将其作为工具提供给其他智能体
- 层次化智能体协作系统的实现
- 多智能体协作解决复杂问题的方法
- 实际案例：构建一个徒步旅行装备推荐系统

适合对象：已掌握基础智能体开发，希望探索多智能体协作模式的开发者。

## 环境要求

运行这些教程需要：
- Python 3.12+
- Jupyter Notebook 或 JupyterLab
- AWS 账户和硅基流动的APIkey（用于访问DeepSeek 模型）
- 必要的依赖包：
  ```
  strands-agents
  strands-agents-tools
  ```

## 快速开始

1. 确保已安装所需依赖：
   ```bash
   pip install strands-agents strands-agents-tools
   ```

2. 启动 Jupyter Notebook 并打开相应的教程文件

3. 按照教程中的说明逐步执行代码单元

## 学习路径建议

1. 首先完成 `first-agent-cn.ipynb` 掌握基础概念
2. 然后学习 `agent-as-tools-cn.ipynb` 了解高级架构模式

通过这两个教程，你将能够从零开始构建功能强大的 AI 智能体系统，并了解如何设计多智能体协作架构。