#!/usr/bin/env python3
# run_web.py
"""
Strands AI助手 Web界面启动脚本
"""

import subprocess
import sys
import os

def check_requirements():
    """检查必要的依赖是否已安装"""
    try:
        import streamlit
        import strands
        import strands_tools
        print("✅ 所有依赖已安装")
        return True
    except ImportError as e:
        print(f"❌ 缺少依赖: {e}")
        print("请运行: pip install -r requirements.txt")
        return False

def main():
    print("🚀 启动Strands AI助手 Web界面...")
    
    # 检查依赖
    if not check_requirements():
        sys.exit(1)
    
    # 检查环境变量
    required_env_vars = ['AWS_ACCESS_KEY_ID', 'AWS_SECRET_ACCESS_KEY', 'AWS_DEFAULT_REGION']
    missing_vars = [var for var in required_env_vars if not os.getenv(var)]
    
    if missing_vars:
        print("⚠️  警告: 以下环境变量未设置:")
        for var in missing_vars:
            print(f"   - {var}")
        print("请确保已正确配置AWS凭证")
    
    # 启动Streamlit应用
    try:
        print("📱 启动Web界面...")
        print("🌐 访问地址: http://localhost:8501")
        subprocess.run([
            sys.executable, "-m", "streamlit", "run", 
            "web_interface.py",
            "--server.port=8501",
            "--server.address=0.0.0.0"
        ])
    except KeyboardInterrupt:
        print("\n👋 感谢使用Strands AI助手!")
    except Exception as e:
        print(f"❌ 启动失败: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()