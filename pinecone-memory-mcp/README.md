# Pinecone Memory MCP Server

A Model Context Protocol (MCP) server that provides intelligent memory storage and retrieval using Pinecone vector database. This server allows AI assistants to remember information, retrieve all memories, and recall contextually relevant memories using semantic search.

## Features

- **🧠 Intelligent Memory Storage**: Automatically categorizes and extracts keywords from memories
- **📚 Complete Memory Retrieval**: View all stored memories with metadata and organization
- **🔍 Semantic Memory Search**: Find contextually relevant memories using vector similarity
- **🏷️ Automatic Categorization**: Memories are automatically categorized (technical, work, personal, learning, etc.)
- **🔑 Keyword Extraction**: Important terms are extracted for better organization
- **💾 Dual Storage System**: Combines Pinecone vector database with local ID tracking for efficiency

## Architecture

```
┌─────────────┐     ┌──────────────┐     ┌─────────────┐
│   Claude    │────▶│  MCP Server  │────▶│  Pinecone   │
│  Desktop    │     │   (Python)   │     │   Vector DB │
└─────────────┘     └──────────────┘     └─────────────┘
                            │
                            ▼
                    ┌──────────────┐
                    │ Local JSON   │
                    │  ID Storage  │
                    └──────────────┘
```

## Prerequisites

- Python 3.8+
- Pinecone account (free tier available at [pinecone.io](https://www.pinecone.io))
- OpenAI API key (for embeddings)
- Claude Desktop application

## Installation

1. **Clone or download this repository**

2. **Install dependencies**:
```bash
cd pinecone-memory-mcp
pip install -r requirements.txt
```

3. **Set up environment variables**:
```bash
cp .env.example .env
```

Edit `.env` and add your API keys:
```env
PINECONE_API_KEY=your-pinecone-api-key
PINECONE_INDEX_NAME=memory-index
OPENAI_API_KEY=your-openai-api-key
```

4. **Configure Claude Desktop**:

Add to your Claude Desktop configuration file:
- macOS: `~/Library/Application Support/Claude/claude_desktop_config.json`
- Windows: `%APPDATA%\Claude\claude_desktop_config.json`

```json
{
  "mcpServers": {
    "pinecone-memory": {
      "command": "python",
      "args": [
        "/absolute/path/to/pinecone-memory-mcp/src/index.py"
      ],
      "env": {
        "PINECONE_API_KEY": "your-pinecone-api-key",
        "PINECONE_INDEX_NAME": "memory-index",
        "OPENAI_API_KEY": "your-openai-api-key"
      }
    }
  }
}
```

## Usage

Once configured, you can use three commands in Claude Desktop:

### 1. Remember This
Store a new memory with automatic categorization and keyword extraction.

**Example**:
```
"Remember this: The deployment process requires running 'npm run build' before 'npm run deploy'"
```

**Response**:
```
✅ Memory stored successfully!

📝 Memory ID: mem_20240115_143022_a1b2c3d4
🏷️ Category: technical
🔑 Keywords: deployment, process, npm, build, deploy
📅 Timestamp: 2024-01-15T14:30:22

Your memory has been securely stored and indexed for future retrieval.
```

### 2. Show Me My Memories
Display all stored memories or filter by category.

**Examples**:
```
"Show me my memories"
"Show me my technical memories"
"Show me my work memories with limit 5"
```

**Response**:
```
📚 Showing 3 memories out of 42 total:

📝 Memory ID: mem_20240115_143022_a1b2c3d4
📅 Created: 2024-01-15T14:30:22
🏷️ Category: technical
🔑 Keywords: deployment, process, npm, build, deploy

💭 Memory:
The deployment process requires running 'npm run build' before 'npm run deploy'
--------------------------------------------------
[Additional memories...]

📊 Memory Statistics:
Total memories: 42
Categories: technical: 15, work: 10, personal: 8, learning: 9
```

### 3. Recall My Memory
Find contextually relevant memories using semantic search.

**Examples**:
```
"Recall my memory about deployment"
"Recall my memory about that UI design principle"
"Recall my memory about the meeting with Sarah"
```

**Response**:
```
🔍 Found 3 relevant memories for: 'deployment'

#1 📝 Memory ID: mem_20240115_143022_a1b2c3d4
🎯 Relevance: 94.5%
📅 Created: 2024-01-15T14:30:22
🏷️ Category: technical
🔑 Keywords: deployment, process, npm, build, deploy

💭 Memory:
The deployment process requires running 'npm run build' before 'npm run deploy'
--------------------------------------------------
[Additional relevant memories...]
```

## Memory Categories

Memories are automatically categorized into:
- **technical**: Code, programming, software-related
- **work**: Meetings, projects, deadlines, tasks
- **personal**: Family, friends, personal events
- **learning**: Studies, courses, tutorials, research
- **idea**: Concepts, brainstorming, innovations
- **reminder**: To-dos, important notes
- **reference**: Links, resources, documentation
- **general**: Default category for uncategorized memories

## Data Storage

### Pinecone Vector Database
- Stores vector embeddings for semantic search
- Maintains all metadata (text, timestamp, category, keywords)
- Enables similarity-based retrieval

### Local JSON Storage
- Tracks all memory IDs for efficient batch retrieval
- Stores memory summaries and categories
- Provides quick access without API calls
- Location: `memory_ids.json` in the project root

## Troubleshooting

### "PINECONE_API_KEY environment variable is required"
- Ensure you've set up the `.env` file with your Pinecone API key
- Or add the API key to the Claude Desktop configuration

### "Error generating embedding"
- Check that your OpenAI API key is valid
- Ensure you have credits in your OpenAI account

### "Index does not exist"
- The server will automatically create the index on first run
- Ensure your Pinecone API key has permission to create indexes

### Memories not showing up
- Check that the `memory_ids.json` file exists and is writable
- Verify that memories are being stored in both Pinecone and local storage

## Advanced Configuration

### Custom Embedding Model
Edit `utils.py` to change the embedding model:
```python
async def generate_embedding(text: str, model: str = "text-embedding-3-small"):
    # Change model parameter to use different OpenAI models
```

### Index Configuration
Edit `pinecone_client.py` to modify index settings:
```python
self.pc.create_index(
    name=self.index_name,
    dimension=1536,  # Adjust based on embedding model
    metric="cosine",  # Can be: cosine, euclidean, dotproduct
    spec=ServerlessSpec(
        cloud="aws",
        region="us-east-1"
    )
)
```

## Privacy & Security

- All memories are stored in your personal Pinecone account
- API keys are never transmitted except to their respective services
- Local storage contains only IDs and metadata, not embeddings
- You maintain full control over your data

## Contributing

Contributions are welcome! Please feel free to submit issues or pull requests.

## License

MIT License - See LICENSE file for details

## Support

For issues or questions:
1. Check the troubleshooting section above
2. Review Pinecone documentation at [docs.pinecone.io](https://docs.pinecone.io)
3. Open an issue in the repository

## Acknowledgments

- Built with the [Model Context Protocol](https://modelcontextprotocol.io)
- Powered by [Pinecone](https://www.pinecone.io) vector database
- Embeddings by [OpenAI](https://openai.com)