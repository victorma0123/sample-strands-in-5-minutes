# Strands 融合 MCP - 5分钟教程

大家好，欢迎来到5分钟上手Strands系列！今天我们将学习如何使用Strands Agents集成MCP（模型上下文协议）。

## MCP 简介

模型上下文协议（MCP）是一种开放协议，标准化了AI Agent如何连接到外部服务，比如数据库、API、系统服务或第三方工具。MCP提供了一个统一的标准接口。

手动实现MCP需要处理大量工作：管理握手、连接状态、消息解析、模式验证等。而使用Strands，只需几行代码即可完成：

```python
mcp_client = MCPClient(lambda: streamablehttp_client("http://example-service.com/mcp"))
with mcp_client:
    tools = mcp_client.list_tools_sync()
    agent = Agent(tools=tools)
```

Strands SDK处理了所有协议的复杂细节，让你可以专注于代理的功能开发，而无需担心集成的繁琐过程。

## 构建MCP服务器

为了演示MCP集成，我们将创建一个中华美食菜谱服务MCP服务器。创建文件 `strands_mcp_server.py`：

```python
# Strands 已经包含了 MCP，无需额外安装
from mcp.server import FastMCP

# 创建 MCP 服务器
mcp = FastMCP(
    name="Chinese Cuisine Recipe Service",
    host="0.0.0.0",
    port=8080
)

# 菜谱数据库
RECIPE_CATALOG = {
    "sichuan": {
        "title": "川菜",
        "recipes": [
            {
                "name": "麻婆豆腐",
                "ingredients": ["嫩豆腐", "牛肉末", "豆瓣酱", "花椒", "蒜苗", "生抽", "料酒"],
                "difficulty": "简单",
                "time": "20分钟",
                "steps": ["豆腐切块焯水", "炒牛肉末至变色", "下豆瓣酱炒香", "加豆腐轻炒", "撒花椒粉和蒜苗"]
            },
            {
                "name": "宫保鸡丁",
                "ingredients": ["鸡胸肉", "花生米", "干辣椒", "花椒", "蒜", "姜", "生抽", "老抽", "糖", "醋"],
                "difficulty": "中等",
                "time": "25分钟",
                "steps": ["鸡肉切丁腌制", "花生米炸至金黄", "爆炒鸡丁", "下调料炒匀", "最后加花生米"]
            }
        ]
    },
    "cantonese": {
        "title": "粤菜",
        "recipes": [
            {
                "name": "白切鸡",
                "ingredients": ["土鸡", "姜", "葱", "盐", "料酒", "生抽", "香油"],
                "difficulty": "简单",
                "time": "45分钟",
                "steps": ["整鸡洗净", "冷水下锅煮开", "转小火煮20分钟", "捞起过冰水", "配姜葱蘸料"]
            }
        ]
    },
    "jiangsu": {
        "title": "苏菜",
        "recipes": [
            {
                "name": "红烧狮子头",
                "ingredients": ["猪肉馅", "马蹄", "鸡蛋", "淀粉", "生抽", "老抽", "糖", "料酒", "青菜"],
                "difficulty": "中等",
                "time": "40分钟",
                "steps": ["肉馅调味搅拌", "做成大肉丸", "油炸定型", "红烧入味", "配青菜装盘"]
            }
        ]
    }
}

@mcp.tool()
def list_cuisines() -> dict:
    """列出所有可用的中餐菜系。"""
    cuisines = {}
    for cuisine_id, cuisine_data in RECIPE_CATALOG.items():
        cuisines[cuisine_id] = {
            "title": cuisine_data["title"],
            "recipe_count": len(cuisine_data["recipes"])
        }
    return {"available_cuisines": cuisines}

@mcp.tool()
def get_recipes_by_cuisine(cuisine: str) -> dict:
    """获取指定菜系的菜谱。"""
    if cuisine.lower() not in RECIPE_CATALOG:
        return {
            "error": f"未找到菜系 '{cuisine}'",
            "available_cuisines": list(RECIPE_CATALOG.keys())
        }
    
    return RECIPE_CATALOG[cuisine.lower()]

@mcp.tool()
def search_recipes_by_ingredient(ingredient: str) -> dict:
    """根据食材搜索相关菜谱。"""
    matching_recipes = []
    for cuisine_id, cuisine_data in RECIPE_CATALOG.items():
        for recipe in cuisine_data["recipes"]:
            if any(ingredient in ing for ing in recipe["ingredients"]):
                matching_recipes.append({
                    "name": recipe["name"],
                    "cuisine": cuisine_data["title"],
                    "difficulty": recipe["difficulty"],
                    "time": recipe["time"]
                })
    
    return {"matching_recipes": matching_recipes}

# 启动 MCP 服务器
if __name__ == "__main__":
    mcp.run(transport="streamable-http")
```

## 运行MCP服务器

创建好 `strands_mcp_server.py` 文件后，在独立终端启动它：

```bash
# 使用 uv 运行 MCP 服务器
uv run python strands_mcp_server.py
```

启动后，你会看到类似下面的日志：

``` bash
INFO:     Started server process
INFO:     Waiting for application startup.
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8080 (Press CTRL+C to quit)
```

**重要提示：** 请保持该终端窗口运行状态！MCP Server 需要保持活跃，Agent 才能连接。

## 连接MCP Server

接下来，我们将把中华美食专家Agent与菜谱的MCP Server集成。创建文件 `subject_expert_with_mcp.py`：

```python
from strands import Agent
from strands.tools.mcp import MCPClient
from mcp.client.streamable_http import streamablehttp_client
from strands.models import BedrockModel
import sys
    
# Ensure UTF-8 encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# Configure AWS Bedrock Claude model
model = BedrockModel(
    model_id="us.anthropic.claude-sonnet-4-20250514-v1:0",
    region_name="us-west-2",
    temperature=0.7
)

def main():
    # Connect to the recipe MCP server
    print("\nConnecting to MCP Server...")
    mcp_recipe_server = MCPClient(lambda: streamablehttp_client("http://localhost:8080/mcp"))

    try:
        with mcp_recipe_server:

            # Create the cooking expert agent with AWS Bedrock Claude model
            cooking_expert = Agent(
                model=model,
                system_prompt="""你是一位中华美食专家，拥有丰富的中国菜谱知识。你可以：
                1. 介绍各大菜系的特色和代表菜品
                2. 根据用户需求推荐合适的菜谱
                3. 根据现有食材搜索可制作的菜品
                4. 提供详细的烹饪步骤和技巧

                当用户询问菜谱时：
                - 先了解他们的口味偏好和烹饪水平
                - 推荐合适难度的菜品
                - 详细介绍食材和制作步骤
                - 给出实用的烹饪小贴士

                规则：
                - 必须使用MCP Server 提供的tool获取菜谱信息
                - 不要编造菜谱，只使用数据库中的真实菜谱
                - 用温馨友好的语气与用户交流
                """
            )

            # List the tools available on the MCP server...
            mcp_tools = mcp_recipe_server.list_tools_sync()
            print(f"Available tools: {[tool.tool_name for tool in mcp_tools]}")

            # ... and add them to the agent
            cooking_expert.tool_registry.process_tools(mcp_tools)

            # Start an interactive cooking session
            print("\n🍳 中华美食专家 - MCP集成版")
            print("=" * 50)
            print("\n🥢 试试问: '有哪些菜系？' 或 '推荐一道川菜' 或 '用鸡肉能做什么菜？'")

            while True:
                user_input = input("\n您的需求: ")
                
                if user_input.lower() in ["exit", "quit", "bye", "退出", "再见"]:
                    print("祝您烹饪愉快！")
                    break
                
                print("\n 正在为您查找...\n")
                cooking_expert(user_input)
               
    except Exception as e:
        print(f" 查询失败: {e}")
        print("请确保美食服务正在运行: python strands_mcp_server.py")

if __name__ == "__main__":
    main()
```

## 运行 Agent

打开第二个终端窗口，激活您的虚拟环境：

```bash
# 在新的终端窗口/标签页中，使用 uv 运行代理
# （确保第一个终端中的服务器仍在运行）
uv run python subject_expert_with_mcp.py
```

你应该会看到如下输出：

```
Connecting to MCP Server...
Available tools: ['list_cuisines', 'get_recipes_by_cuisine', 'search_recipes_by_ingredient']

🍳 中华美食专家 - MCP集成版
==================================================

🥢 试试问: '有哪些菜系？' 或 '推荐一道川菜' 或 '用鸡肉能做什么菜？'
## 测试集成效果

现在你可以与代理互动，它能无缝结合本地工具与外部服务：

### 查询可用菜系

```
🍽️ 您的需求: 有哪些菜系？

🤔 正在为您查找...

我来为您查询一下可用的中华菜系！

工具调用：list_cuisines

目前我们的菜谱库包含以下菜系：

🌶️ **川菜** - 2道菜谱
   特色：麻辣鲜香，口味浓郁

🦆 **粤菜** - 1道菜谱  
   特色：清淡鲜美，注重原味

🦐 **苏菜** - 1道菜谱
   特色：口味清淡，造型精美

您想了解哪个菜系的具体菜谱呢？
```

### 推荐川菜

```
🍽️ 您的需求: 推荐一道川菜

🤔 正在为您查找...

好的！让我为您推荐几道经典川菜。

工具调用：get_recipes_by_cuisine

## 🌶️ 川菜推荐

### 1. 麻婆豆腐 (简单 | 20分钟)
**食材：** 嫩豆腐、牛肉末、豆瓣酱、花椒、蒜苗、生抽、料酒
**制作步骤：**
1. 豆腐切块焯水
2. 炒牛肉末至变色  
3. 下豆瓣酱炒香
4. 加豆腐轻炒
5. 撒花椒粉和蒜苗

### 2. 宫保鸡丁 (中等 | 25分钟)
**食材：** 鸡胸肉、花生米、干辣椒、花椒、蒜、姜、生抽、老抽、糖、醋
**制作步骤：**
1. 鸡肉切丁腌制
2. 花生米炸至金黄
3. 爆炒鸡丁
4. 下调料炒匀
5. 最后加花生米

🔥 **小贴士：** 川菜的精髓在于麻辣平衡，建议先少放花椒，根据个人口味调整！

您想学哪道菜的详细做法呢？
```

### 根据食材搜索

```
🍽️ 您的需求: 用鸡肉能做什么菜？

🤔 正在为您查找...

让我帮您搜索含有鸡肉的菜谱！

工具调用：search_recipes_by_ingredient

## 🐔 鸡肉菜谱推荐

根据您的食材，我找到了以下菜谱：

### 宫保鸡丁 (川菜)
- **难度：** 中等
- **时间：** 25分钟
- **特色：** 麻辣香甜，口感丰富

### 白切鸡 (粤菜)  
- **难度：** 简单
- **时间：** 45分钟
- **特色：** 清淡鲜美，保持原味

两道菜风味完全不同：
- 如果喜欢重口味，推荐宫保鸡丁
- 如果偏爱清淡，推荐白切鸡

您想了解哪道菜的详细做法呢？
```

## 直接调用工具

虽然代理会根据对话自动选择工具，你也可以直接调用MCP工具：

```python
# 直接调用工具示例
with mcp_recipe_server:
    mcp_tools = mcp_recipe_server.list_tools_sync()
    agent = Agent(tools=mcp_tools)
    
    # 通过 MCP 直接调用工具
    cuisines = agent.tool.list_cuisines()
    print(f"可用菜系:\n{cuisines}")
```

这样你可以在需要时直接控制工具，同时仍享受代理的自然语言交互体验。

## MCP 集成的优势

这个集成展示了 MCP 方法的几个关键优势：

### 服务抽象化
你的代理不需要了解菜谱服务的内部实现。它可以是简单的 JSON 文件、复杂的数据库，甚至是另一个 AI 代理 - MCP 接口保持不变。

### 技术独立性
菜谱服务可以用 Java 重写、托管在互联网任何地方，或者完全替换为不同的提供商 - 你的代理代码不需要改变。

### 可扩展性
你可以轻松连接到多个服务，甚至将它们与你自己的自定义工具混合使用：

```python
# 连接到多个外部 MCP 服务器
recipe_service = MCPClient(lambda: streamablehttp_client("http://recipe-provider.com/mcp"))
nutrition_service = MCPClient(lambda: streamablehttp_client("http://nutrition-api.com/mcp"))

with recipe_service, nutrition_service:
    # 组合所有工具 - 它们都以相同的方式工作！
    tools = (
        recipe_service.list_tools_sync() +      # 来自外部菜谱服务器的工具
        nutrition_service.list_tools_sync() +   # 来自外部营养服务器的工具
        [http_request] +                        # Strands SDK 的内置工具
        [cooking_tips, ...]                     # 你的自定义工具
    )
    
    # 使用所有工具创建代理
    agent = Agent(model=model, tools=tools)
```

## 总结

在本教程中，我们已经：

* 构建了一个中华美食菜谱MCP服务器  
* 用最少的代码将代理连接到MCP服务器  
* 通过自然语言实现了无缝的工具集成  
* 理解了Strands Agents SDK如何抽象MCP的复杂性  

通过MCP方式注册多个MCP Server到Agent并实现调用，让你的AI Agent能够轻松集成各种外部服务！