#!/usr/bin/env python3
"""
Pinecone Memory MCP Server - Easy Installation Script

This script helps you set up the Pinecone Memory MCP Server with minimal effort.
Usage: python install.py
"""

import os
import sys
import json
import subprocess
import platform
from pathlib import Path
import shutil


def print_header():
    """Print a nice header."""
    print("""
╔══════════════════════════════════════════╗
║   🧠 Pinecone Memory MCP Server Setup    ║
╚══════════════════════════════════════════╝
    """)


def check_requirements():
    """Check if required tools are installed."""
    print("📋 Checking requirements...")
    
    # Check Python version
    python_version = sys.version_info
    if python_version.major < 3 or (python_version.major == 3 and python_version.minor < 8):
        print("❌ Python 3.8+ is required")
        return False
    print(f"✅ Python {python_version.major}.{python_version.minor} detected")
    
    # Check pip
    try:
        subprocess.run(["pip", "--version"], capture_output=True, check=True)
        print("✅ pip is installed")
    except:
        print("❌ pip is not installed")
        return False
    
    return True


def install_dependencies():
    """Install Python dependencies."""
    print("\n📦 Installing dependencies...")
    
    requirements_file = Path(__file__).parent / "requirements.txt"
    
    try:
        subprocess.run(
            [sys.executable, "-m", "pip", "install", "-r", str(requirements_file)],
            check=True
        )
        print("✅ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError:
        print("❌ Failed to install dependencies")
        return False


def setup_env_file():
    """Set up the .env file with API keys."""
    print("\n🔑 Setting up API keys...")
    
    env_example = Path(__file__).parent / ".env.example"
    env_file = Path(__file__).parent / ".env"
    
    if env_file.exists():
        overwrite = input("⚠️  .env file already exists. Overwrite? (y/N): ").lower()
        if overwrite != 'y':
            print("↩️  Keeping existing .env file")
            return True
    
    # Copy the example file
    shutil.copy(env_example, env_file)
    
    print("\nPlease enter your API keys (press Enter to skip):")
    
    # Get Pinecone API key
    pinecone_key = input("🔹 Pinecone API Key: ").strip()
    if pinecone_key:
        update_env_value(env_file, "PINECONE_API_KEY", pinecone_key)
    
    # Get Pinecone index name
    index_name = input("🔹 Pinecone Index Name (default: memory-index): ").strip()
    if index_name:
        update_env_value(env_file, "PINECONE_INDEX_NAME", index_name)
    
    # Get OpenAI API key
    openai_key = input("🔹 OpenAI API Key: ").strip()
    if openai_key:
        update_env_value(env_file, "OPENAI_API_KEY", openai_key)
    
    print("✅ .env file created")
    return True


def update_env_value(env_file, key, value):
    """Update a value in the .env file."""
    with open(env_file, 'r') as f:
        lines = f.readlines()
    
    with open(env_file, 'w') as f:
        for line in lines:
            if line.startswith(f"{key}="):
                f.write(f"{key}={value}\n")
            else:
                f.write(line)


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


def setup_claude_desktop():
    """Set up Claude Desktop configuration."""
    print("\n🖥️  Setting up Claude Desktop integration...")
    
    config_path = get_claude_config_path()
    
    if not config_path:
        print("⚠️  Could not determine Claude Desktop config location")
        print("   Please add the configuration manually")
        return False
    
    if not config_path.exists():
        print(f"⚠️  Claude Desktop config not found at {config_path}")
        create = input("   Create new config file? (y/N): ").lower()
        if create != 'y':
            return False
        
        config_path.parent.mkdir(parents=True, exist_ok=True)
        config = {"mcpServers": {}}
    else:
        with open(config_path, 'r') as f:
            config = json.load(f)
    
    # Get the absolute path to index.py
    index_path = str(Path(__file__).parent / "src" / "index.py")
    
    # Add our server configuration
    server_config = {
        "command": sys.executable,  # Use current Python interpreter
        "args": [index_path]
    }
    
    # Ask if user wants to add environment variables to config
    add_env = input("Add API keys to Claude config? (more convenient but less secure) (y/N): ").lower()
    if add_env == 'y':
        env_file = Path(__file__).parent / ".env"
        if env_file.exists():
            env_vars = {}
            with open(env_file, 'r') as f:
                for line in f:
                    if '=' in line and not line.startswith('#'):
                        key, value = line.strip().split('=', 1)
                        if value and value != f"your-{key.lower().replace('_', '-')}":
                            env_vars[key] = value
            
            if env_vars:
                server_config["env"] = env_vars
    
    # Add to config
    if "mcpServers" not in config:
        config["mcpServers"] = {}
    
    config["mcpServers"]["pinecone-memory"] = server_config
    
    # Write the config
    with open(config_path, 'w') as f:
        json.dump(config, f, indent=2)
    
    print(f"✅ Claude Desktop configured at {config_path}")
    return True


def create_cli_wrapper():
    """Create a CLI wrapper for easy command-line usage."""
    print("\n🔧 Creating CLI wrapper...")
    
    wrapper_content = f"""#!/usr/bin/env python3
# Auto-generated CLI wrapper for Pinecone Memory MCP Server

import sys
import os

# Add the src directory to path
sys.path.insert(0, r'{Path(__file__).parent / "src"}')

# Set up environment
os.environ.setdefault("MCP_TRANSPORT", "stdio")

# Import and run the server
from index import main
import asyncio

if __name__ == "__main__":
    asyncio.run(main())
"""
    
    wrapper_path = Path(__file__).parent / "pinecone-memory"
    
    with open(wrapper_path, 'w') as f:
        f.write(wrapper_content)
    
    # Make it executable on Unix-like systems
    if platform.system() != "Windows":
        os.chmod(wrapper_path, 0o755)
    
    print(f"✅ CLI wrapper created: {wrapper_path}")
    
    # Suggest adding to PATH
    print("\n💡 To use from anywhere, add this to your PATH:")
    print(f"   export PATH=\"$PATH:{Path(__file__).parent}\"")
    
    return True


def test_server():
    """Test if the server can start."""
    print("\n🧪 Testing server startup...")
    
    index_path = Path(__file__).parent / "src" / "index.py"
    
    try:
        # Test with --help flag
        result = subprocess.run(
            [sys.executable, str(index_path), "--help"],
            capture_output=True,
            text=True,
            timeout=5
        )
        
        if result.returncode == 0:
            print("✅ Server test successful")
            return True
        else:
            print("❌ Server test failed")
            print(result.stderr)
            return False
    except Exception as e:
        print(f"❌ Server test error: {e}")
        return False


def print_next_steps():
    """Print next steps for the user."""
    print("""
╔══════════════════════════════════════════╗
║         ✨ Setup Complete! ✨            ║
╚══════════════════════════════════════════╝

🎯 Next Steps:

1. If you haven't already, add your API keys to the .env file:
   • Pinecone API Key (from pinecone.io)
   • OpenAI API Key (from openai.com)

2. For Claude Desktop:
   • Restart Claude Desktop
   • The memory tools should appear automatically

3. For command-line usage:
   • Run: python src/index.py
   • Or use: ./pinecone-memory (if in PATH)

4. For HTTP/SSE mode (for testing):
   • Run: python src/index.py --sse
   • Server will start on http://localhost:8080

📚 Available Commands:
   • remember_this - Store a new memory
   • show_my_memories - View all memories
   • recall_memory - Search memories semantically

Need help? Check the README.md for detailed documentation.
    """)


def main():
    """Main installation flow."""
    print_header()
    
    # Check requirements
    if not check_requirements():
        print("\n❌ Please install the required tools and try again.")
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Failed to install dependencies. Please check your Python environment.")
        sys.exit(1)
    
    # Set up .env file
    setup_env_file()
    
    # Set up Claude Desktop
    setup_claude = input("\n📱 Configure Claude Desktop? (Y/n): ").lower()
    if setup_claude != 'n':
        setup_claude_desktop()
    
    # Create CLI wrapper
    create_cli = input("\n🔨 Create command-line wrapper? (Y/n): ").lower()
    if create_cli != 'n':
        create_cli_wrapper()
    
    # Test the server
    test_server()
    
    # Print next steps
    print_next_steps()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n⚠️  Installation cancelled by user")
        sys.exit(1)
    except Exception as e:
        print(f"\n❌ Installation error: {e}")
        sys.exit(1)