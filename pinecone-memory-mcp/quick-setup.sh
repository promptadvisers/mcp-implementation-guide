#!/bin/bash

# Pinecone Memory MCP - Quick Setup for Claude Desktop
# Run this script to set everything up automatically

echo "╔══════════════════════════════════════════╗"
echo "║   🧠 Pinecone Memory MCP Quick Setup     ║"
echo "╚══════════════════════════════════════════╝"
echo ""

# Check if running on Mac
if [[ "$OSTYPE" != "darwin"* ]]; then
    echo "❌ This script is designed for macOS"
    exit 1
fi

# Check Python
if ! command -v python3 &> /dev/null; then
    echo "❌ Python 3 is required. Please install it first."
    exit 1
fi

echo "✅ Python 3 found"

# Get script directory
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

# Install dependencies
echo ""
echo "📦 Installing dependencies..."
pip3 install -q mcp pinecone-client python-dotenv openai aiofiles 2>/dev/null || {
    echo "⚠️  Some dependencies may need to be installed manually"
}

# Check for .env file
if [ ! -f "$SCRIPT_DIR/.env" ]; then
    echo ""
    echo "🔑 Setting up API keys..."
    
    # Copy example env
    cp "$SCRIPT_DIR/.env.example" "$SCRIPT_DIR/.env"
    
    echo "Please enter your API keys (press Enter to skip):"
    
    read -p "Pinecone API Key: " PINECONE_KEY
    if [ ! -z "$PINECONE_KEY" ]; then
        sed -i '' "s/your-pinecone-api-key/$PINECONE_KEY/" "$SCRIPT_DIR/.env"
    fi
    
    read -p "OpenAI API Key: " OPENAI_KEY
    if [ ! -z "$OPENAI_KEY" ]; then
        sed -i '' "s/your-openai-api-key/$OPENAI_KEY/" "$SCRIPT_DIR/.env"
    fi
fi

# Configure Claude Desktop
echo ""
echo "🖥️  Configuring Claude Desktop..."

CONFIG_PATH="$HOME/Library/Application Support/Claude/claude_desktop_config.json"
CONFIG_DIR="$(dirname "$CONFIG_PATH")"

# Create config directory if it doesn't exist
mkdir -p "$CONFIG_DIR"

# Check if config exists
if [ -f "$CONFIG_PATH" ]; then
    echo "📋 Existing config found. Backing up..."
    cp "$CONFIG_PATH" "$CONFIG_PATH.backup"
fi

# Add to Claude Desktop using Python script
python3 "$SCRIPT_DIR/mcp-add.py" install

echo ""
echo "✅ Setup complete!"
echo ""
echo "🎯 Next steps:"
echo "   1. Restart Claude Desktop"
echo "   2. Look for the memory tools in Claude"
echo ""
echo "📚 Available commands:"
echo "   • remember_this - Store a memory"
echo "   • show_my_memories - View all memories"
echo "   • recall_memory - Search memories"
echo ""
echo "Need help? Check the README.md"