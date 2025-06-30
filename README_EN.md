# Strands Agents in 5 Minutes / 5分钟上手Strands系列

[中文](README.md) | English

## Project Introduction
Welcome to the "Strands Agents in 5 Minutes" tutorial series! This is a series focused on enhancing users' and developers' ability to build AI Agents. Through concise 5-minute tutorials, you'll quickly master the design, development, integration, and deployment processes of Strands Agents.

## Tutorial Objectives
- Enhance users'/developers' Agent building capabilities through a series of tutorials, ensuring learning continuity
- Master the basic processes of designing, developing, integrating, and deploying Strands Agent applications
- Enable users to independently develop and deploy their own Agent demos

## Curriculum
| No. | Session | Description | Demo | Duration | Level |
|-----|---------|-------------|------|----------|-------|
| 1 | Strands SDK First Agent | Strands core architecture Model/Tool/Prompt, Install Strands SDK, Create and run first Strands Agent | Use Python code to output Strands Agent core components description, install SDK, run a Strands Agent | 5 min | L100 |
| 2 | Strands Session Management and State Maintenance | Strands Loop introduction, session history, session window, multi-turn dialogue implementation | Use Strands to implement multi-turn dialogue, save and print session history | 5 min | L200 |
| 3 | Strands Build Custom Tools and Usage | Strands built-in tool calling, custom tool definition and registration | Develop a custom tool (like weather query) and integrate into Strands Agent, register and call built-in tools in Strands Agent | 5 min | L200 |
| 4 | Strands Integration with MCP | Strands discovery, integration and usage of MCP Server | Register multiple MCP Servers to Agentic through MCP and implement calling | 5 min | L200 |
| 5 | Strands Multi-Agent Collaboration | Implement multi-model calling based on Strands built-in Multi frameworks | Implement multi-model collaborative content creation through Strands multi-model calling | 5 min | L200 |
| 6 | Strands Integration with Guardrails | Use Strands to integrate Guardrails, protect Agent behavior, enhance security capabilities | Configure Guardrails rules, trigger and observe Strands Agent protection behavior | 5 min | L200 |
| 6 | Strands and A2A Protocol | Use A2A protocol to encapsulate Strands Agents for remote Agent collaboration | Use Strands and A2A SDK to develop remote agents and client agent, implement multi agents remote collaboration | 5 min | L300 |

[1] https://pplx-res.cloudinary.com/image/private/user_uploads/52003953/42b4107b-92f4-4c5d-bc40-cfd967e543d0/Screenshot-2025-06-30-at-15.06.50.jpg

## Tutorial Features
- **Concise and Efficient**: Each session controlled within 5 minutes
- **Theory with Practice**: Every concept comes with practical demos
- **Progressive Learning**: From basics to advanced, step by step
- **Hands-on Experience**: Each lesson includes runnable code

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
Create a `.env` file and add the following content:
```
AWS_ACCESS_KEY_ID=your_access_key_id
AWS_SECRET_ACCESS_KEY=your_secret_access_key
AWS_DEFAULT_REGION=your_default_region (e.g., us-east-1)
```

### Run Example
```bash
python3 first_agent.py
```

## Course Navigation
- [Lesson 1: Build Your First Agent](01_first_agent/first_agent.md)
- More lessons coming soon...

## Contributing
Welcome to submit Pull Requests to help improve this tutorial series!

## Security
See [CONTRIBUTING](CONTRIBUTING.md) for more information.

## License
This library is licensed under the MIT-0 License. See the [LICENSE](LICENSE) file.