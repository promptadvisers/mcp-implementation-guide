#!/usr/bin/env python3
"""
Pinecone Memory MCP Server
An MCP server that provides memory storage and retrieval using Pinecone vector database.

Tools:
1. remember_this - Store a new memory with automatic embedding and metadata
2. show_my_memories - Display all stored memories
3. recall_memory - Find contextually relevant memories using semantic search
"""

import asyncio
import os
import json
from datetime import datetime
from typing import Dict, Any, Optional
from contextlib import asynccontextmanager
from collections.abc import AsyncIterator

from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp.types import Tool, TextContent

from dotenv import load_dotenv

# Import our modules
from pinecone_client import PineconeMemoryClient
from memory_store import MemoryStore
from utils import (
    generate_embedding,
    generate_memory_id,
    extract_keywords,
    categorize_memory,
    format_memory_for_display,
    extract_context_from_query
)

# Load environment variables
load_dotenv()


class MemoryContext:
    """Application context holding persistent resources."""
    def __init__(self):
        self.pinecone_client: Optional[PineconeMemoryClient] = None
        self.memory_store: Optional[MemoryStore] = None
        self.initialized: bool = False


# Global context
context = MemoryContext()


async def initialize_context():
    """Initialize the application context."""
    if not context.initialized:
        try:
            context.pinecone_client = PineconeMemoryClient()
            context.memory_store = MemoryStore()
            context.initialized = True
            print("✅ Memory system initialized successfully")
        except Exception as e:
            print(f"❌ Error initializing context: {str(e)}")
            raise


# Create the MCP server
server = Server("pinecone-memory-server")


@server.list_tools()
async def list_tools() -> list[Tool]:
    """List available tools for the MCP server."""
    return [
        Tool(
            name="remember_this",
            description="Store a new memory in the vector database with automatic categorization and keyword extraction",
            inputSchema={
                "type": "object",
                "properties": {
                    "memory": {
                        "type": "string",
                        "description": "The memory or information to store"
                    },
                    "context": {
                        "type": "string",
                        "description": "Optional additional context about this memory",
                        "optional": True
                    }
                },
                "required": ["memory"]
            }
        ),
        Tool(
            name="show_my_memories",
            description="Display all stored memories with their metadata and categories",
            inputSchema={
                "type": "object",
                "properties": {
                    "category": {
                        "type": "string",
                        "description": "Optional category filter (technical, work, personal, learning, idea, reminder, reference)",
                        "optional": True
                    },
                    "limit": {
                        "type": "integer",
                        "description": "Maximum number of memories to show (default: 10)",
                        "optional": True
                    }
                }
            }
        ),
        Tool(
            name="recall_memory",
            description="Find memories contextually related to your query using semantic search",
            inputSchema={
                "type": "object",
                "properties": {
                    "query": {
                        "type": "string",
                        "description": "What you're trying to remember or find"
                    },
                    "top_k": {
                        "type": "integer",
                        "description": "Number of relevant memories to return (default: 5)",
                        "optional": True
                    }
                },
                "required": ["query"]
            }
        )
    ]


@server.call_tool()
async def call_tool(name: str, arguments: Dict[str, Any]) -> list[TextContent]:
    """Handle tool calls from the MCP client."""
    
    # Ensure context is initialized
    await initialize_context()
    
    try:
        if name == "remember_this":
            result = await remember_this(
                memory=arguments.get("memory"),
                context=arguments.get("context")
            )
        elif name == "show_my_memories":
            result = await show_my_memories(
                category=arguments.get("category"),
                limit=arguments.get("limit", 10)
            )
        elif name == "recall_memory":
            result = await recall_memory(
                query=arguments.get("query"),
                top_k=arguments.get("top_k", 5)
            )
        else:
            result = f"Unknown tool: {name}"
        
        return [TextContent(type="text", text=result)]
        
    except Exception as e:
        error_msg = f"Error executing {name}: {str(e)}"
        print(f"❌ {error_msg}")
        return [TextContent(type="text", text=error_msg)]


async def remember_this(memory: str, context: Optional[str] = None) -> str:
    """
    Store a new memory in Pinecone with automatic metadata extraction.
    
    Args:
        memory: The memory text to store
        context: Optional additional context
    
    Returns:
        Success message with memory ID
    """
    try:
        # Combine memory with context if provided
        full_text = memory
        if context:
            full_text = f"{memory}\n\nContext: {context}"
        
        # Generate unique ID
        memory_id = generate_memory_id(memory)
        
        # Extract metadata
        keywords = extract_keywords(full_text)
        category = categorize_memory(full_text)
        
        # Generate embedding
        embedding = await generate_embedding(full_text)
        
        # Prepare metadata for Pinecone
        metadata = {
            "memory_text": memory,
            "context": context or "",
            "timestamp": datetime.now().isoformat(),
            "category": category,
            "keywords": ", ".join(keywords),
            "char_count": len(memory)
        }
        
        # Store in Pinecone
        success = await context.pinecone_client.upsert_memory(
            memory_id=memory_id,
            embedding=embedding,
            metadata=metadata
        )
        
        if success:
            # Store ID in local storage
            await context.memory_store.add_memory_id(
                memory_id=memory_id,
                memory_text=memory,
                category=category,
                keywords=keywords
            )
            
            return f"""✅ Memory stored successfully!

📝 Memory ID: {memory_id}
🏷️ Category: {category}
🔑 Keywords: {', '.join(keywords)}
📅 Timestamp: {metadata['timestamp']}

Your memory has been securely stored and indexed for future retrieval."""
        else:
            return "❌ Failed to store memory in Pinecone. Please check your configuration."
            
    except Exception as e:
        return f"❌ Error storing memory: {str(e)}"


async def show_my_memories(category: Optional[str] = None, limit: int = 10) -> str:
    """
    Display all stored memories or filter by category.
    
    Args:
        category: Optional category filter
        limit: Maximum number of memories to show
    
    Returns:
        Formatted list of memories
    """
    try:
        # Get all memory IDs from local storage
        all_memory_ids = await context.memory_store.get_all_memory_ids()
        
        if not all_memory_ids:
            return "📭 No memories stored yet. Use 'remember_this' to store your first memory!"
        
        # Filter by category if specified
        if category:
            filtered_memories = await context.memory_store.get_memories_by_category(category)
            memory_ids = [m["id"] for m in filtered_memories][:limit]
        else:
            memory_ids = all_memory_ids[:limit]
        
        if not memory_ids:
            return f"📭 No memories found in category '{category}'"
        
        # Fetch memories from Pinecone
        result = await context.pinecone_client.fetch_memories(memory_ids)
        
        if "error" in result:
            return f"❌ Error fetching memories: {result['error']}"
        
        # Format output
        output = f"📚 Showing {len(result['memories'])} memories"
        if category:
            output += f" (category: {category})"
        output += f" out of {len(all_memory_ids)} total:\n\n"
        
        for memory in result['memories']:
            memory_text = memory['metadata'].get('memory_text', 'No text available')
            output += format_memory_for_display(
                memory_id=memory['id'],
                memory_text=memory_text,
                metadata=memory['metadata']
            )
            output += "\n"
        
        # Add stats
        stats = await context.memory_store.get_stats()
        output += f"\n📊 Memory Statistics:\n"
        output += f"Total memories: {stats['total_memories']}\n"
        if stats.get('categories'):
            output += "Categories: " + ", ".join([f"{cat}: {count}" for cat, count in stats['categories'].items()])
        
        return output
        
    except Exception as e:
        return f"❌ Error showing memories: {str(e)}"


async def recall_memory(query: str, top_k: int = 5) -> str:
    """
    Find memories contextually related to a query using semantic search.
    
    Args:
        query: What the user is trying to remember
        top_k: Number of results to return
    
    Returns:
        Most relevant memories with similarity scores
    """
    try:
        # Extract context from query
        query_context = extract_context_from_query(query)
        
        # Generate query embedding
        query_embedding = await generate_embedding(query)
        
        # Build filter if category is detected
        filter_dict = None
        if query_context.get("filters", {}).get("category"):
            filter_dict = {"category": query_context["filters"]["category"]}
        
        # Query Pinecone for similar memories
        result = await context.pinecone_client.query_memories(
            query_embedding=query_embedding,
            top_k=top_k,
            filter_dict=filter_dict
        )
        
        if "error" in result:
            return f"❌ Error recalling memories: {result['error']}"
        
        if not result['memories']:
            return "🤔 No relevant memories found. Try rephrasing your query or store more memories!"
        
        # Format output
        output = f"🔍 Found {len(result['memories'])} relevant memories for: '{query}'\n\n"
        
        for i, memory in enumerate(result['memories'], 1):
            memory_text = memory['metadata'].get('memory_text', 'No text available')
            output += f"#{i} "
            output += format_memory_for_display(
                memory_id=memory['id'],
                memory_text=memory_text,
                metadata=memory['metadata'],
                score=memory['score']
            )
            output += "\n"
        
        # Add search context if filters were applied
        if filter_dict:
            output += f"\n🔎 Search filters applied: {filter_dict}"
        
        return output
        
    except Exception as e:
        return f"❌ Error recalling memory: {str(e)}"


async def main():
    """Main entry point for the MCP server."""
    # Initialize context at startup
    await initialize_context()
    
    # Run the stdio server
    async with stdio_server() as (read_stream, write_stream):
        await server.run(
            read_stream,
            write_stream,
            server.create_initialization_options()
        )


if __name__ == "__main__":
    asyncio.run(main())