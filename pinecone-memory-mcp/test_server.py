#!/usr/bin/env python3
"""
Test script for Pinecone Memory MCP Server
This simulates the server functionality without requiring MCP installation
"""

import sys
import os
import json
from datetime import datetime

# Add src to path
sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))

# Mock the MCP imports
class MockServer:
    def __init__(self, name):
        self.name = name
        print(f"🚀 Mock MCP Server: {name}")

class MockContext:
    def __init__(self):
        self.pinecone_client = None
        self.memory_store = None

# Create mock context
mock_context = MockContext()

# Import our utilities (these should work without MCP)
try:
    from utils import (
        generate_memory_id,
        extract_keywords,
        categorize_memory,
        format_memory_for_display
    )
    print("✅ Utilities loaded successfully")
except ImportError as e:
    print(f"❌ Failed to load utilities: {e}")
    sys.exit(1)

def test_memory_functions():
    """Test the memory processing functions."""
    print("\n📝 Testing Memory Functions...")
    print("-" * 40)
    
    # Test memory 1
    memory1 = "Remember to run npm build before deploying the application to production"
    print(f"\n1️⃣ Test Memory: '{memory1}'")
    
    # Generate ID
    mem_id = generate_memory_id(memory1)
    print(f"   Generated ID: {mem_id}")
    
    # Extract keywords
    keywords = extract_keywords(memory1)
    print(f"   Keywords: {', '.join(keywords)}")
    
    # Categorize
    category = categorize_memory(memory1)
    print(f"   Category: {category}")
    
    # Test memory 2
    memory2 = "Meeting with Sarah tomorrow at 2pm to discuss the Q4 project roadmap"
    print(f"\n2️⃣ Test Memory: '{memory2}'")
    
    mem_id2 = generate_memory_id(memory2)
    print(f"   Generated ID: {mem_id2}")
    
    keywords2 = extract_keywords(memory2)
    print(f"   Keywords: {', '.join(keywords2)}")
    
    category2 = categorize_memory(memory2)
    print(f"   Category: {category2}")
    
    # Test memory 3
    memory3 = "Interesting idea: What if we used vector embeddings to create a memory palace for AI?"
    print(f"\n3️⃣ Test Memory: '{memory3}'")
    
    mem_id3 = generate_memory_id(memory3)
    print(f"   Generated ID: {mem_id3}")
    
    keywords3 = extract_keywords(memory3)
    print(f"   Keywords: {', '.join(keywords3)}")
    
    category3 = categorize_memory(memory3)
    print(f"   Category: {category3}")
    
    # Test formatting
    print("\n📋 Testing Memory Display Format:")
    print("-" * 40)
    
    metadata = {
        "timestamp": datetime.now().isoformat(),
        "category": category,
        "keywords": keywords
    }
    
    formatted = format_memory_for_display(
        mem_id,
        memory1,
        metadata,
        score=0.95
    )
    print(formatted)

def simulate_tools():
    """Simulate the three MCP tools."""
    print("\n🛠️ Simulating MCP Tools:")
    print("-" * 40)
    
    print("\n1. remember_this")
    print("   Input: memory='Learn Python decorators', context='For code review'")
    print("   Output: ✅ Memory stored (simulated)")
    
    print("\n2. show_my_memories")
    print("   Input: category='technical', limit=5")
    print("   Output: 📚 Showing 3 memories (simulated)")
    
    print("\n3. recall_memory")
    print("   Input: query='deployment process'")
    print("   Output: 🔍 Found 2 relevant memories (simulated)")

def main():
    """Main test function."""
    print("""
╔══════════════════════════════════════════╗
║   🧠 Pinecone Memory MCP Server Test     ║
╚══════════════════════════════════════════╝
    """)
    
    # Check environment
    print("🔍 Checking Environment...")
    print(f"   Python: {sys.version}")
    print(f"   Platform: {sys.platform}")
    
    # Check for API keys
    env_file = os.path.join(os.path.dirname(__file__), '.env')
    if os.path.exists(env_file):
        print(f"   ✅ .env file found")
        
        # Try to load and check keys
        try:
            from dotenv import load_dotenv
            load_dotenv(env_file)
            
            pinecone_key = os.getenv("PINECONE_API_KEY")
            openai_key = os.getenv("OPENAI_API_KEY")
            
            if pinecone_key and not pinecone_key.startswith("your-"):
                print("   ✅ Pinecone API key configured")
            else:
                print("   ⚠️ Pinecone API key not configured")
            
            if openai_key and not openai_key.startswith("your-"):
                print("   ✅ OpenAI API key configured")
            else:
                print("   ⚠️ OpenAI API key not configured")
        except ImportError:
            print("   ⚠️ python-dotenv not installed, can't check keys")
    else:
        print(f"   ⚠️ .env file not found")
    
    # Run tests
    test_memory_functions()
    simulate_tools()
    
    print("\n✅ Test completed successfully!")
    print("\n💡 To use the full server:")
    print("   1. Install dependencies: pip install -r requirements.txt")
    print("   2. Configure API keys in .env")
    print("   3. Run: python src/index.py")
    print("   Or use the installation script: python install.py")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n⚠️ Test interrupted")
    except Exception as e:
        print(f"\n❌ Test error: {e}")
        import traceback
        traceback.print_exc()