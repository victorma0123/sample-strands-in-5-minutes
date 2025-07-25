# Multi-Agent 系统

本教程部分探索了使用Strands Agents SDK构建Multi-Agent系统的不同方法。

## Multi-Agent系统的方法

### 1. Agents as Tools 
[文档链接](https://strandsagents.com/latest/user-guide/concepts/multi-agent/agents-as-tools/)

"Agents as Tools"模式创建了一个层次结构，其中专业AI Agent被封装为可调用的函数（工具），可供其他Agent使用：

- **Orchestrator Agent**：处理用户交互并将任务委派给专业Agent
- **Specialized Tool Agents**：当被协调者调用时执行特定领域的任务
- **Key Benefits**：关注点分离、层次委派、模块化架构

实现涉及使用`@tool`装饰器将专业Agent转换为可调用函数：

```python
@tool
def research_assistant(query: str) -> str:
    """Process and respond to research-related queries."""
    research_agent = Agent(system_prompt=RESEARCH_ASSISTANT_PROMPT)
    return str(research_agent(query))
```


### 2. Agent Swarms
[文档链接](https://strandsagents.com/latest/user-guide/concepts/multi-agent/swarm/)

Agent Swarms通过一组共同工作的自主AI Agent利用集体智能：

- **Decentralized Control**：没有单一Agent指导整个系统
- **Shared Memory**：Agent交换见解以构建集体知识
- **Coordination Mechanisms**：协作、竞争或混合方法
- **Communication Patterns**：Agent之间可以相互通信的网状网络

内置的`swarm`工具简化了实现：

```python
from strands import Agent
from strands_tools import swarm

agent = Agent(tools=[swarm])
result = agent.tool.swarm(
    task="Analyze this dataset and identify market trends",
    swarm_size=4,
    coordination_pattern="collaborative"
)
```

### 3. Agent Graphs
[文档链接](https://strandsagents.com/latest/user-guide/concepts/multi-agent/graph/)

Agent Graphs提供了具有明确通信路径的互连AI Agent的结构化网络：

- **Nodes (Agents)**：具有专业角色的单个AI Agent
- **Edges (Connections)**：定义Agent之间的通信路径
- **Topology Patterns**：Star、Mesh或Hierarchical结构

`agent_graph`工具支持创建复杂的Agent网络：

```python
from strands import Agent
from strands_tools import agent_graph

agent = Agent(tools=[agent_graph])
agent.tool.agent_graph(
    action="create",
    graph_id="research_team",
    topology={
        "type": "star",
        "nodes": [
            {"id": "coordinator", "role": "team_lead"},
            {"id": "data_analyst", "role": "analyst"},
            {"id": "domain_expert", "role": "expert"}
        ],
        "edges": [
            {"from": "coordinator", "to": "data_analyst"},
            {"from": "coordinator", "to": "domain_expert"}
        ]
    }
)
```

### 4. Agent Workflows
[文档链接](https://strandsagents.com/latest/user-guide/concepts/multi-agent/workflow/)

Agent Workflows在定义的序列中协调多个AI Agent的任务，具有明确的依赖关系：

- **Task Definition**：清晰描述每个Agent需要完成的内容
- **Dependency Management**：Sequential dependencies、Parallel execution、Join points
- **Information Flow**：将一个Agent的输出连接到另一个Agent的输入

`workflow`工具处理任务创建、依赖解析和执行：

```python
from strands import Agent
from strands_tools import workflow

agent = Agent(tools=[workflow])
agent.tool.workflow(
    action="create",
    workflow_id="data_analysis",
    tasks=[
        {
            "task_id": "data_extraction",
            "description": "Extract key data from the report"
        },
        {
            "task_id": "analysis",
            "description": "Analyze the extracted data",
            "dependencies": ["data_extraction"]
        }
    ]
)
```

## 选择合适的方法

- **Agents as Tools**：最适合具有专业知识的明确层次结构
- **Agent Swarms**：适合具有涌现智能的协作问题解决
- **Agent Graphs**：适合对通信模式进行精确控制
- **Agent Workflows**：适合具有明确依赖关系的顺序流程

每种方法在复杂性、控制和协作模式方面提供不同的权衡。正确的选择取决于您的特定用例和需求。