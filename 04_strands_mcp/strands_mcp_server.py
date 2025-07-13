from mcp.server import FastMCP
import sys
import locale
import logging

# Ensure UTF-8 encoding
if sys.stdout.encoding != 'utf-8':
    sys.stdout.reconfigure(encoding='utf-8')

# #打开debug 日志 
# logging.getLogger("strands").setLevel(logging.DEBUG)
# logging.basicConfig(
#     format="%(levelname)s | %(name)s | %(message)s",
#     handlers=[logging.StreamHandler()]
# )

# Create an MCP server
mcp = FastMCP(
    name="Chinese Cuisine Recipe Service",
    host="0.0.0.0",
    port=8080
)

# Recipe database
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
        "title": "淮扬菜",
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
    """List all available Chinese cuisines."""
    cuisines = {}
    for cuisine_id, cuisine_data in RECIPE_CATALOG.items():
        cuisines[cuisine_id] = {
            "title": cuisine_data["title"],
            "recipe_count": len(cuisine_data["recipes"])
        }
    return {"available_cuisines": cuisines}

@mcp.tool()
def get_recipes_by_cuisine(cuisine: str) -> dict:
    """Get recipes for a specific Chinese cuisine."""
    if cuisine.lower() not in RECIPE_CATALOG:
        return {
            "error": f"Cuisine '{cuisine}' not found",
            "available_cuisines": list(RECIPE_CATALOG.keys())
        }
    
    return RECIPE_CATALOG[cuisine.lower()]

@mcp.tool()
def search_recipes_by_ingredient(ingredient: str) -> dict:
    """Search recipes that contain a specific ingredient."""
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

# Start the MCP server
if __name__ == "__main__":
    
    print("Starting Chinese Cuisine MCP Server...")
    mcp.run(transport="streamable-http")