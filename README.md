26.6.23学习切换本地的新分支
# Atlas AI Agent Tutorial

[![Python 3.11+](https://img.shields.io/badge/python-3.11+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

从零开始的AI Agent开发教程配套代码。

## 安装

pip install atlas-tutorial


## 用法

from atlas_tutorial import AtlasChatAgent

agent = AtlasChatAgent(name="我的Atlas") print(agent.chat("你好"))


## CLI

atlas chat --name "我的Atlas"


## 开发

git clone https://github.com/user/atlas-tutorial.git cd atlas-tutorial python -m venv venv source venv/bin/activate pip install -e ".[dev]" pytest


## 许可证
MIT
Step 6: .gitignore

# Python
__pycache__/
*.py[cod]
*$py.class
*.so
.Python
venv/
.venv/
ENV/
.pytest_cache/
.coverage
htmlcov/
*.egg-info/
dist/
build/

# IDE
.vscode/
.idea/
*.swp
.DS_Store

# 项目
.env
memory/
*.log
chapters/
site/