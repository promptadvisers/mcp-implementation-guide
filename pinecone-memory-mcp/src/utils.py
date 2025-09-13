"""
Utility functions for text processing, embedding generation, and metadata extraction.
"""

from typing import List, Dict, Any, Optional
import os
from datetime import datetime
import re
import hashlib

# Try to load dotenv (optional)
try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    pass

# Try to import OpenAI (optional for testing)
try:
    import openai
    openai.api_key = os.getenv("OPENAI_API_KEY")
    OPENAI_AVAILABLE = True
except ImportError:
    OPENAI_AVAILABLE = False


async def generate_embedding(text: str, model: str = "text-embedding-3-small") -> List[float]:
    """
    Generate embedding for text using OpenAI's embedding model.
    
    Args:
        text: Text to embed
        model: OpenAI embedding model to use
    
    Returns:
        List of floats representing the embedding
    """
    if not OPENAI_AVAILABLE:
        # Return a mock embedding for testing
        import random
        random.seed(hash(text))
        return [random.random() for _ in range(1536)]
    
    try:
        response = openai.embeddings.create(
            input=text,
            model=model
        )
        return response.data[0].embedding
    except Exception as e:
        print(f"Error generating embedding: {str(e)}")
        # Return a zero vector as fallback
        return [0.0] * 1536


def generate_memory_id(text: str) -> str:
    """
    Generate a unique ID for a memory based on its content and timestamp.
    
    Args:
        text: The memory text
    
    Returns:
        Unique memory ID
    """
    timestamp = datetime.now().isoformat()
    content_hash = hashlib.md5(f"{text}{timestamp}".encode()).hexdigest()[:8]
    return f"mem_{datetime.now().strftime('%Y%m%d_%H%M%S')}_{content_hash}"


def extract_keywords(text: str, max_keywords: int = 5) -> List[str]:
    """
    Extract important keywords from text.
    
    Args:
        text: Text to extract keywords from
        max_keywords: Maximum number of keywords to extract
    
    Returns:
        List of keywords
    """
    # Remove common stop words
    stop_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'in', 'on', 'at', 'to', 'for',
        'of', 'with', 'by', 'from', 'up', 'about', 'into', 'through', 'during',
        'is', 'are', 'was', 'were', 'be', 'been', 'being', 'have', 'has', 'had',
        'do', 'does', 'did', 'will', 'would', 'should', 'could', 'may', 'might',
        'must', 'can', 'this', 'that', 'these', 'those', 'i', 'you', 'he', 'she',
        'it', 'we', 'they', 'what', 'which', 'who', 'when', 'where', 'why', 'how'
    }
    
    # Extract words (alphanumeric only)
    words = re.findall(r'\b[a-zA-Z0-9]+\b', text.lower())
    
    # Filter out stop words and short words
    keywords = [w for w in words if w not in stop_words and len(w) > 2]
    
    # Count word frequency
    word_freq = {}
    for word in keywords:
        word_freq[word] = word_freq.get(word, 0) + 1
    
    # Sort by frequency and return top keywords
    sorted_keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, _ in sorted_keywords[:max_keywords]]


def categorize_memory(text: str) -> str:
    """
    Automatically categorize a memory based on its content.
    
    Args:
        text: Memory text to categorize
    
    Returns:
        Category string
    """
    text_lower = text.lower()
    
    # Define category patterns
    categories = {
        "technical": ["code", "programming", "software", "api", "database", "algorithm", 
                     "function", "debug", "error", "bug", "server", "deploy"],
        "work": ["meeting", "project", "deadline", "task", "client", "presentation",
                "report", "team", "manager", "office", "colleague"],
        "personal": ["family", "friend", "birthday", "vacation", "hobby", "home",
                    "weekend", "holiday", "personal", "myself"],
        "learning": ["learn", "study", "course", "tutorial", "book", "article",
                    "research", "understand", "knowledge", "skill"],
        "idea": ["idea", "concept", "thought", "brainstorm", "innovation", "creative",
                "imagine", "possibility", "what if", "consider"],
        "reminder": ["remember", "remind", "don't forget", "note to self", "important",
                    "todo", "must", "need to", "should"],
        "reference": ["link", "url", "website", "resource", "documentation", "guide",
                     "manual", "reference", "source", "information"]
    }
    
    # Count matches for each category
    category_scores = {}
    for category, keywords in categories.items():
        score = sum(1 for keyword in keywords if keyword in text_lower)
        if score > 0:
            category_scores[category] = score
    
    # Return category with highest score, or "general" if no matches
    if category_scores:
        return max(category_scores.items(), key=lambda x: x[1])[0]
    return "general"


def format_memory_for_display(
    memory_id: str,
    memory_text: str,
    metadata: Dict[str, Any],
    score: Optional[float] = None
) -> str:
    """
    Format a memory for display to the user.
    
    Args:
        memory_id: The memory ID
        memory_text: The memory text
        metadata: Memory metadata
        score: Optional similarity score
    
    Returns:
        Formatted string for display
    """
    output = f"📝 Memory ID: {memory_id}\n"
    
    if score is not None:
        output += f"🎯 Relevance: {score:.2%}\n"
    
    output += f"📅 Created: {metadata.get('timestamp', 'Unknown')}\n"
    output += f"🏷️ Category: {metadata.get('category', 'general')}\n"
    
    keywords = metadata.get('keywords', [])
    if keywords:
        output += f"🔑 Keywords: {', '.join(keywords)}\n"
    
    output += f"\n💭 Memory:\n{memory_text}\n"
    output += "-" * 50
    
    return output


def truncate_text(text: str, max_length: int = 500) -> str:
    """
    Truncate text to a maximum length while preserving word boundaries.
    
    Args:
        text: Text to truncate
        max_length: Maximum length
    
    Returns:
        Truncated text
    """
    if len(text) <= max_length:
        return text
    
    # Find the last space before max_length
    truncated = text[:max_length]
    last_space = truncated.rfind(' ')
    
    if last_space > 0:
        truncated = truncated[:last_space]
    
    return truncated + "..."


def extract_context_from_query(query: str) -> Dict[str, Any]:
    """
    Extract context and intent from a recall query.
    
    Args:
        query: The user's recall query
    
    Returns:
        Dictionary containing extracted context
    """
    context = {
        "original_query": query,
        "intent": "recall",
        "filters": {}
    }
    
    # Check for time-based queries
    time_patterns = {
        "today": r"\btoday\b",
        "yesterday": r"\byesterday\b",
        "this week": r"\bthis week\b",
        "last week": r"\blast week\b",
        "this month": r"\bthis month\b"
    }
    
    for time_period, pattern in time_patterns.items():
        if re.search(pattern, query, re.IGNORECASE):
            context["filters"]["time_period"] = time_period
            break
    
    # Check for category mentions
    categories = ["technical", "work", "personal", "learning", "idea", "reminder", "reference"]
    for category in categories:
        if category in query.lower():
            context["filters"]["category"] = category
            break
    
    # Extract any quoted phrases as exact matches
    quoted = re.findall(r'"([^"]+)"', query)
    if quoted:
        context["filters"]["exact_phrases"] = quoted
    
    return context