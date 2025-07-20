# Multi-Agent 示例

本目录包含 Multi-Agent 示例架构的实现文件，其中专业化的 agents 在中央协调器的协调下共同工作。

## 实现文件

- [teachers_assistant.py](teachers_assistant.py) - 主要的协调 agent，负责将查询路由到专业化 agents
- [math_assistant.py](math_assistant.py) - 处理数学查询的专业化 agent
- [language_assistant.py](language_assistant.py) - 负责语言翻译任务的专业化 agent
- [english_assistant.py](english_assistant.py) - 负责英语语法和理解的专业化 agent
- [computer_science_assistant.py](computer_science_assistant.py) - 负责计算机科学和编程任务的专业化 agent
- [no_expertise.py](no_expertise.py) - 处理特定领域之外查询的通用 assistant

## 文档

有关此 multi-agent 架构工作原理的详细信息，请参阅 [multi_agent_example.md](multi_agent_example.md) 文档文件。