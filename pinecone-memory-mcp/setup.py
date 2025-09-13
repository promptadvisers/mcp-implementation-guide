"""
Setup script for Pinecone Memory MCP Server
Allows installation via pip: pip install pinecone-memory-mcp
"""

from setuptools import setup, find_packages
from pathlib import Path

# Read the README file
readme_path = Path(__file__).parent / "README.md"
long_description = readme_path.read_text() if readme_path.exists() else ""

setup(
    name="pinecone-memory-mcp",
    version="1.0.0",
    author="Your Name",
    description="An MCP server for intelligent memory storage and retrieval using Pinecone",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/promptadvisers/mcp-implementation-guide",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    python_requires=">=3.8",
    install_requires=[
        "mcp",
        "pinecone-client>=3.0.0",
        "python-dotenv>=1.0.0",
        "openai>=1.0.0",
        "aiofiles>=23.0.0",
    ],
    extras_require={
        "sse": ["aiohttp>=3.8.0"],
        "dev": ["pytest", "pytest-asyncio", "black", "flake8"],
    },
    entry_points={
        "console_scripts": [
            "pinecone-memory=index:main",
            "pinecone-memory-mcp=index:main",
        ],
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
    ],
    keywords="mcp ai memory pinecone vector-database claude anthropic",
    project_urls={
        "Bug Reports": "https://github.com/promptadvisers/mcp-implementation-guide/issues",
        "Source": "https://github.com/promptadvisers/mcp-implementation-guide",
    },
)