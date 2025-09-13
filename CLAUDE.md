# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

This repository contains comprehensive documentation for the Model Context Protocol (MCP), including:
- A complete implementation guide for building production-ready MCP servers
- MCP 101 documentation covering the protocol fundamentals
- Templates and best practices for both Python and TypeScript implementations

## Key Files

- `mcp-complete-implementation-guide.md`: Step-by-step guide for implementing MCP servers with production-ready templates
- `mcps-101.md`: Overview and introduction to the Model Context Protocol ecosystem

## MCP Server Development

When implementing MCP servers in this codebase, follow these critical principles:

### Core Components Required
1. **Lifespan Management**: Always use proper resource initialization and cleanup with asynccontextmanager
2. **Tool Definitions**: Include clear, specific docstrings that become the LLM's understanding of when/how to use each tool
3. **Transport Protocol**: Support both SSE (for remote deployments) and stdio (for local processes)
4. **Error Handling**: Always return errors gracefully, never let exceptions crash the server

### Python Implementation Pattern
```python
from mcp.server.fastmcp import FastMCP, Context
from contextlib import asynccontextmanager

@asynccontextmanager
async def lifespan(server):
    # Initialize resources once
    client = initialize_client()
    try:
        yield {"client": client}
    finally:
        await client.close()

mcp = FastMCP("server-name", lifespan=lifespan)

@mcp.tool()
async def tool_name(ctx: Context, param: str) -> str:
    """Clear description of what this tool does"""
    # Implementation
```

### The Three Pillars of MCP
- **Tools**: Functions that LLMs can invoke to perform actions
- **Resources**: Data sources that LLMs can access  
- **Prompts**: Template prompts that LLMs can use

### Transport Protocols
- Use SSE for cloud/remote deployments
- Use stdio for local client-managed processes