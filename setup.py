"""
阿垣记忆系统 - 安装配置
"""

from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as f:
    long_description = f.read()

setup(
    name="ayuan-memory",
    version="0.1.0",
    author="阿垣 (Ayuan) & 帝君",
    author_email="",
    description="AI Agent Memory System with Chinese Philosophy - 融合九宫哲学的AI记忆管理系统",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/ayuan-ai/ayuan-memory",
    packages=find_packages(),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Topic :: Scientific/Engineering :: Artificial Intelligence",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
    python_requires=">=3.8",
    install_requires=[
        # 无外部依赖，纯Python实现
    ],
    extras_require={
        "dev": [
            "pytest>=7.0",
            "black>=22.0",
            "flake8>=4.0",
        ],
    },
)
