"""
Local storage system for managing memory IDs and metadata.
Provides fast access to memory identifiers without querying Pinecone.
"""

import json
import os
from pathlib import Path
from typing import List, Dict, Any, Optional
from datetime import datetime
import aiofiles
import asyncio
from threading import Lock


class MemoryStore:
    """Manages local storage of memory IDs and metadata."""
    
    def __init__(self, storage_path: str = "memory_ids.json"):
        """
        Initialize the memory store.
        
        Args:
            storage_path: Path to the JSON file for storing memory IDs
        """
        self.storage_path = Path(storage_path)
        self.lock = Lock()
        self._ensure_storage_exists()
    
    def _ensure_storage_exists(self):
        """Create storage file if it doesn't exist."""
        if not self.storage_path.exists():
            initial_data = {
                "vector_ids": [],
                "memories": {},
                "last_updated": datetime.now().isoformat(),
                "total_memories": 0
            }
            with open(self.storage_path, 'w') as f:
                json.dump(initial_data, f, indent=2)
    
    async def add_memory_id(
        self,
        memory_id: str,
        memory_text: str,
        category: str = "general",
        keywords: List[str] = None
    ) -> bool:
        """
        Add a new memory ID to the store.
        
        Args:
            memory_id: Unique identifier for the memory
            memory_text: The actual memory text
            category: Category of the memory
            keywords: List of keywords associated with the memory
        
        Returns:
            Success status
        """
        try:
            # Read current data
            async with aiofiles.open(self.storage_path, 'r') as f:
                data = json.loads(await f.read())
            
            # Add new memory ID if not already present
            if memory_id not in data["vector_ids"]:
                data["vector_ids"].append(memory_id)
                
                # Store memory metadata
                data["memories"][memory_id] = {
                    "text": memory_text[:500],  # Store first 500 chars
                    "category": category,
                    "keywords": keywords or [],
                    "created_at": datetime.now().isoformat()
                }
                
                data["total_memories"] = len(data["vector_ids"])
                data["last_updated"] = datetime.now().isoformat()
                
                # Write updated data
                async with aiofiles.open(self.storage_path, 'w') as f:
                    await f.write(json.dumps(data, indent=2))
                
                return True
            
            return False  # Memory ID already exists
            
        except Exception as e:
            print(f"Error adding memory ID: {str(e)}")
            return False
    
    async def get_all_memory_ids(self) -> List[str]:
        """
        Get all stored memory IDs.
        
        Returns:
            List of memory IDs
        """
        try:
            async with aiofiles.open(self.storage_path, 'r') as f:
                data = json.loads(await f.read())
            return data.get("vector_ids", [])
        except Exception as e:
            print(f"Error getting memory IDs: {str(e)}")
            return []
    
    async def get_memory_metadata(self, memory_id: str) -> Optional[Dict[str, Any]]:
        """
        Get metadata for a specific memory.
        
        Args:
            memory_id: The memory ID to look up
        
        Returns:
            Memory metadata or None if not found
        """
        try:
            async with aiofiles.open(self.storage_path, 'r') as f:
                data = json.loads(await f.read())
            return data.get("memories", {}).get(memory_id)
        except Exception as e:
            print(f"Error getting memory metadata: {str(e)}")
            return None
    
    async def remove_memory_id(self, memory_id: str) -> bool:
        """
        Remove a memory ID from the store.
        
        Args:
            memory_id: The memory ID to remove
        
        Returns:
            Success status
        """
        try:
            async with aiofiles.open(self.storage_path, 'r') as f:
                data = json.loads(await f.read())
            
            if memory_id in data["vector_ids"]:
                data["vector_ids"].remove(memory_id)
                
                # Remove memory metadata
                if memory_id in data["memories"]:
                    del data["memories"][memory_id]
                
                data["total_memories"] = len(data["vector_ids"])
                data["last_updated"] = datetime.now().isoformat()
                
                async with aiofiles.open(self.storage_path, 'w') as f:
                    await f.write(json.dumps(data, indent=2))
                
                return True
            
            return False  # Memory ID not found
            
        except Exception as e:
            print(f"Error removing memory ID: {str(e)}")
            return False
    
    async def get_memories_by_category(self, category: str) -> List[Dict[str, Any]]:
        """
        Get all memories in a specific category.
        
        Args:
            category: The category to filter by
        
        Returns:
            List of memories in the category
        """
        try:
            async with aiofiles.open(self.storage_path, 'r') as f:
                data = json.loads(await f.read())
            
            memories = []
            for memory_id, metadata in data.get("memories", {}).items():
                if metadata.get("category") == category:
                    memories.append({
                        "id": memory_id,
                        **metadata
                    })
            
            return memories
            
        except Exception as e:
            print(f"Error getting memories by category: {str(e)}")
            return []
    
    async def search_memories_by_keyword(self, keyword: str) -> List[Dict[str, Any]]:
        """
        Search memories by keyword.
        
        Args:
            keyword: The keyword to search for
        
        Returns:
            List of memories containing the keyword
        """
        try:
            async with aiofiles.open(self.storage_path, 'r') as f:
                data = json.loads(await f.read())
            
            keyword_lower = keyword.lower()
            memories = []
            
            for memory_id, metadata in data.get("memories", {}).items():
                # Check if keyword is in the text or keywords list
                text_match = keyword_lower in metadata.get("text", "").lower()
                keyword_match = keyword_lower in [k.lower() for k in metadata.get("keywords", [])]
                
                if text_match or keyword_match:
                    memories.append({
                        "id": memory_id,
                        **metadata
                    })
            
            return memories
            
        except Exception as e:
            print(f"Error searching memories: {str(e)}")
            return []
    
    async def get_stats(self) -> Dict[str, Any]:
        """
        Get statistics about stored memories.
        
        Returns:
            Dictionary containing memory statistics
        """
        try:
            async with aiofiles.open(self.storage_path, 'r') as f:
                data = json.loads(await f.read())
            
            # Count memories by category
            category_counts = {}
            for metadata in data.get("memories", {}).values():
                category = metadata.get("category", "unknown")
                category_counts[category] = category_counts.get(category, 0) + 1
            
            return {
                "total_memories": data.get("total_memories", 0),
                "last_updated": data.get("last_updated"),
                "categories": category_counts,
                "storage_file": str(self.storage_path)
            }
            
        except Exception as e:
            print(f"Error getting stats: {str(e)}")
            return {"error": str(e)}