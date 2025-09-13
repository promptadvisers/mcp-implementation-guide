"""
Pinecone client integration for memory storage and retrieval.
Handles all vector database operations.
"""

from pinecone import Pinecone, ServerlessSpec
from typing import List, Dict, Any, Optional
import os
from dotenv import load_dotenv
import logging

load_dotenv()

logger = logging.getLogger(__name__)


class PineconeMemoryClient:
    """Manages Pinecone operations for memory storage and retrieval."""
    
    def __init__(self):
        """Initialize Pinecone client and index."""
        self.api_key = os.getenv("PINECONE_API_KEY")
        self.index_name = os.getenv("PINECONE_INDEX_NAME", "memory-index")
        self.namespace = "memories"
        
        if not self.api_key:
            raise ValueError("PINECONE_API_KEY environment variable is required")
        
        # Initialize Pinecone
        self.pc = Pinecone(api_key=self.api_key)
        
        # Create index if it doesn't exist
        self._ensure_index_exists()
        
        # Connect to index
        self.index = self.pc.Index(self.index_name)
    
    def _ensure_index_exists(self):
        """Create Pinecone index if it doesn't exist."""
        try:
            existing_indexes = self.pc.list_indexes()
            index_names = [idx.name for idx in existing_indexes]
            
            if self.index_name not in index_names:
                logger.info(f"Creating new index: {self.index_name}")
                self.pc.create_index(
                    name=self.index_name,
                    dimension=1536,  # OpenAI embedding dimension
                    metric="cosine",
                    spec=ServerlessSpec(
                        cloud="aws",
                        region="us-east-1"
                    )
                )
                logger.info(f"Index {self.index_name} created successfully")
            else:
                logger.info(f"Index {self.index_name} already exists")
        except Exception as e:
            logger.error(f"Error ensuring index exists: {str(e)}")
            raise
    
    async def upsert_memory(
        self,
        memory_id: str,
        embedding: List[float],
        metadata: Dict[str, Any]
    ) -> bool:
        """
        Store a memory vector in Pinecone.
        
        Args:
            memory_id: Unique identifier for the memory
            embedding: Vector embedding of the memory
            metadata: Additional metadata (text, timestamp, category, etc.)
        
        Returns:
            Success status
        """
        try:
            # Prepare vector for upsert
            vector = {
                "id": memory_id,
                "values": embedding,
                "metadata": metadata
            }
            
            # Upsert to Pinecone
            response = self.index.upsert(
                vectors=[vector],
                namespace=self.namespace
            )
            
            logger.info(f"Memory {memory_id} stored successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error storing memory: {str(e)}")
            return False
    
    async def fetch_memories(self, memory_ids: List[str]) -> Dict[str, Any]:
        """
        Fetch specific memories by their IDs.
        
        Args:
            memory_ids: List of memory IDs to fetch
        
        Returns:
            Dictionary containing memory vectors and metadata
        """
        try:
            response = self.index.fetch(
                ids=memory_ids,
                namespace=self.namespace
            )
            
            memories = []
            for vec_id, vec_data in response.vectors.items():
                memory = {
                    "id": vec_id,
                    "metadata": vec_data.metadata,
                    "score": 1.0  # Exact match
                }
                memories.append(memory)
            
            return {"memories": memories, "count": len(memories)}
            
        except Exception as e:
            logger.error(f"Error fetching memories: {str(e)}")
            return {"memories": [], "count": 0, "error": str(e)}
    
    async def query_memories(
        self,
        query_embedding: List[float],
        top_k: int = 5,
        filter_dict: Optional[Dict] = None
    ) -> Dict[str, Any]:
        """
        Query for similar memories using semantic search.
        
        Args:
            query_embedding: Vector embedding of the query
            top_k: Number of results to return
            filter_dict: Optional metadata filters
        
        Returns:
            Dictionary containing matching memories with similarity scores
        """
        try:
            # Perform semantic search
            response = self.index.query(
                vector=query_embedding,
                top_k=top_k,
                namespace=self.namespace,
                include_metadata=True,
                filter=filter_dict
            )
            
            memories = []
            for match in response.matches:
                memory = {
                    "id": match.id,
                    "metadata": match.metadata,
                    "score": match.score
                }
                memories.append(memory)
            
            return {
                "memories": memories,
                "count": len(memories)
            }
            
        except Exception as e:
            logger.error(f"Error querying memories: {str(e)}")
            return {"memories": [], "count": 0, "error": str(e)}
    
    async def delete_memory(self, memory_id: str) -> bool:
        """
        Delete a specific memory.
        
        Args:
            memory_id: ID of the memory to delete
        
        Returns:
            Success status
        """
        try:
            self.index.delete(
                ids=[memory_id],
                namespace=self.namespace
            )
            logger.info(f"Memory {memory_id} deleted successfully")
            return True
            
        except Exception as e:
            logger.error(f"Error deleting memory: {str(e)}")
            return False
    
    async def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about the memory index.
        
        Returns:
            Dictionary containing index statistics
        """
        try:
            stats = self.index.describe_index_stats()
            namespace_stats = stats.namespaces.get(self.namespace, {})
            
            return {
                "total_memories": namespace_stats.get("vector_count", 0),
                "index_fullness": stats.index_fullness,
                "dimension": stats.dimension
            }
            
        except Exception as e:
            logger.error(f"Error getting stats: {str(e)}")
            return {"error": str(e)}