#!/usr/bin/env python3
"""
MCP Add - Easy installation tool for Pinecone Memory MCP Server
Similar to 'claude add' but for this specific MCP server

Usage:
    python mcp-add.py install    # Install to Claude Desktop
    python mcp-add.py remove     # Remove from Claude Desktop
    python mcp-add.py status     # Check installation status
"""

import os
import sys
import json
import platform
from pathlib import Path
import argparse


def get_claude_config_path():
    """Get the Claude Desktop configuration file path."""
    system = platform.system()
    
    if system == "Darwin":  # macOS
        config_path = Path.home() / "Library" / "Application Support" / "Claude" / "claude_desktop_config.json"
    elif system == "Windows":
        config_path = Path(os.environ["APPDATA"]) / "Claude" / "claude_desktop_config.json"
    elif system == "Linux":
        config_path = Path.home() / ".config" / "Claude" / "claude_desktop_config.json"
    else:
        return None
    
    return config_path


def install_to_claude():
    """Install the MCP server to Claude Desktop."""
    print("🔧 Installing Pinecone Memory MCP to Claude Desktop...")
    
    config_path = get_claude_config_path()
    
    if not config_path:
        print("❌ Could not determine Claude Desktop config location")
        return False
    
    # Ensure config directory exists
    config_path.parent.mkdir(parents=True, exist_ok=True)
    
    # Load or create config
    if config_path.exists():
        with open(config_path, 'r') as f:
            config = json.load(f)
    else:
        config = {"mcpServers": {}}
    
    # Ensure mcpServers exists
    if "mcpServers" not in config:
        config["mcpServers"] = {}
    
    # Get the absolute path to index.py
    index_path = str(Path(__file__).parent / "src" / "index.py")
    
    # Check if Python is available
    python_cmd = sys.executable
    
    # Create server configuration
    server_config = {
        "command": python_cmd,
        "args": [index_path]
    }
    
    # Check for .env file
    env_file = Path(__file__).parent / ".env"
    if env_file.exists():
        print("📋 Found .env file")
        use_env = input("   Add API keys from .env to Claude config? (y/N): ").lower()
        
        if use_env == 'y':
            env_vars = {}
            with open(env_file, 'r') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        if value and not value.startswith("your-"):
                            env_vars[key] = value
            
            if env_vars:
                server_config["env"] = env_vars
                print("   ✅ API keys added to config")
    else:
        print("⚠️  No .env file found. You'll need to add API keys manually.")
        print("   Create .env from .env.example and add your keys")
    
    # Add to config
    config["mcpServers"]["pinecone-memory"] = server_config
    
    # Write the config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Installed to: {config_path}")
    print("\n🎯 Next steps:")
    print("   1. Restart Claude Desktop")
    print("   2. Look for the memory tools in Claude")
    print("\n📚 Available commands:")
    print("   • remember_this - Store a memory")
    print("   • show_my_memories - View memories")
    print("   • recall_memory - Search memories")
    
    return True


def remove_from_claude():
    """Remove the MCP server from Claude Desktop."""
    print("🗑️  Removing Pinecone Memory MCP from Claude Desktop...")
    
    config_path = get_claude_config_path()
    
    if not config_path or not config_path.exists():
        print("❌ Claude Desktop config not found")
        return False
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    if "mcpServers" in config and "pinecone-memory" in config["mcpServers"]:
        del config["mcpServers"]["pinecone-memory"]
        
        with open(config_path, 'w') as f:
            json.dump(config, f, indent=2)
        
        print("✅ Removed from Claude Desktop")
        print("   Restart Claude Desktop for changes to take effect")
        return True
    else:
        print("⚠️  Pinecone Memory MCP not found in Claude config")
        return False


def check_status():
    """Check if the MCP server is installed."""
    print("🔍 Checking installation status...")
    
    config_path = get_claude_config_path()
    
    if not config_path:
        print("❌ Could not determine Claude Desktop config location")
        return False
    
    if not config_path.exists():
        print("❌ Claude Desktop config not found")
        print(f"   Expected at: {config_path}")
        return False
    
    with open(config_path, 'r') as f:
        config = json.load(f)
    
    if "mcpServers" in config and "pinecone-memory" in config["mcpServers"]:
        print("✅ Pinecone Memory MCP is installed")
        
        server_config = config["mcpServers"]["pinecone-memory"]
        print(f"\n📋 Configuration:")
        print(f"   Command: {server_config.get('command', 'Not set')}")
        
        if "env" in server_config:
            print(f"   Environment variables:")
            for key in server_config["env"]:
                if "KEY" in key or "TOKEN" in key:
                    print(f"     • {key}: ****** (hidden)")
                else:
                    print(f"     • {key}: {server_config['env'][key]}")
        
        # Check if files exist
        if "args" in server_config and server_config["args"]:
            script_path = Path(server_config["args"][0])
            if script_path.exists():
                print(f"   ✅ Script exists: {script_path}")
            else:
                print(f"   ❌ Script not found: {script_path}")
        
        return True
    else:
        print("❌ Pinecone Memory MCP is not installed")
        print("   Run 'python mcp-add.py install' to install")
        return False


def main():
    """Main CLI entry point."""
    parser = argparse.ArgumentParser(
        description="Pinecone Memory MCP - Installation Manager",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python mcp-add.py install    # Install to Claude Desktop
  python mcp-add.py remove     # Remove from Claude Desktop  
  python mcp-add.py status     # Check installation status
        """
    )
    
    parser.add_argument(
        'command',
        choices=['install', 'remove', 'status'],
        help='Command to execute'
    )
    
    parser.add_argument(
        '--force',
        action='store_true',
        help='Force installation without prompts'
    )
    
    args = parser.parse_args()
    
    print("""
╔══════════════════════════════════════════╗
║   🧠 Pinecone Memory MCP Manager         ║
╚══════════════════════════════════════════╝
    """)
    
    if args.command == 'install':
        success = install_to_claude()
    elif args.command == 'remove':
        success = remove_from_claude()
    elif args.command == 'status':
        success = check_status()
    else:
        print(f"❌ Unknown command: {args.command}")
        success = False
    
    sys.exit(0 if success else 1)


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️  Operation cancelled")
        sys.exit(1)
    except Exception as e:
        print(f"❌ Error: {e}")
        sys.exit(1)