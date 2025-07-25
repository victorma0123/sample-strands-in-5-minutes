#!/bin/bash

# 检查Python是否已安装
if ! command -v python3 &> /dev/null; then
    echo "错误: 未找到Python3。请安装Python3后再试。"
    exit 1
fi

# 检查pip是否已安装
if ! command -v pip3 &> /dev/null; then
    echo "错误: 未找到pip3。请安装pip后再试。"
    exit 1
fi

# 检查是否存在虚拟环境，如果不存在则创建
if [ ! -d "venv" ]; then
    echo "创建虚拟环境..."
    python3 -m venv venv
fi

# 激活虚拟环境
echo "激活虚拟环境..."
source venv/bin/activate

# 安装依赖
echo "安装依赖..."
pip install -r requirements.txt

# 启动应用
echo "启动Strands Swarm Agent演示应用..."
streamlit run app.py