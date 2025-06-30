# Strands Agents in 5 Minutes

[中文](README.md) | English

## Introduction
Welcome to the "Strands Agents in 5 Minutes" tutorial series! This series focuses on enhancing users' and developers' ability to build AI Agents. Through concise 5-minute tutorials, you'll quickly master the design, development, integration, and deployment processes of Strands Agents.

## Learning Objectives
- Enhance users'/developers' Agent building capabilities through a series of tutorials ensuring learning continuity
- Master the basic processes of designing, developing, integrating, and deploying Strands Agent applications
- Enable users to independently develop and deploy their own Agent demos

## Curriculum
Organized by L100-L400 levels, covering:

### L100 - Basic Concepts
- Core components of Strands Agent
- Basic workflows
- Quick start examples

### L200 - Advanced Applications
- Session management
- Tool integration
- Web service integration

### L300 - Advanced Features
- State persistence
- Security and monitoring
- Performance optimization

### L400 - Extension Development
- MCP protocol extensions
- Custom tool development
- Best practices

## Tutorial Features
- **Concise and Efficient**: Each lesson controlled within 5 minutes, highlighting key points
- **Theory with Practice**: Every concept comes with practical code examples
- **Progressive Learning**: From basics to advanced, step by step
- **Hands-on Experience**: Each lesson includes runnable demos

## Quick Start

### Prerequisites
- Python 3.10 or higher
- AWS account (for accessing Claude 3.7 model in Amazon Bedrock)

### Environment Setup
1. Create and activate Python virtual environment:
```bash
python -m venv venv
source .venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Install dependencies:
```bash
uv pip install strands-agents strands-agents-tools
```

### Configuration
Create a `.env` file with your AWS credentials:
```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_DEFAULT_REGION=your_region (e.g., us-east-1)
```

### Run the Example
```bash
python3 first_agent.py
```

## Course Navigation
- [Lesson 1: Build Your First Agent](01_first_agent/first_agent.md)
- More lessons coming soon...

## Contributing
Contributions are welcome! Please feel free to submit a Pull Request.

## License
This project is licensed under the [MIT License](LICENSE).
