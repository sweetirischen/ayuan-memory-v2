"""
Memory Palace - A 9-zone memory organization system

Inspired by ancient wisdom that has guided seekers for millennia.
Each zone represents a stage in the natural cycle of growth and transformation.
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
import json
from .smart_classifier import SmartClassifier


@dataclass
class ZoneRoom:
    """A room in the memory palace"""
    name: str
    zone_number: int
    description: str
    memories: List[Dict] = field(default_factory=list)
    
    def add_memory(self, memory: Dict):
        """Add a memory to this zone"""
        memory["added_at"] = datetime.now().isoformat()
        self.memories.append(memory)
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "zone_number": self.zone_number,
            "description": self.description,
            "memories": self.memories
        }


class MemoryPalace:
    """
    Memory Palace - 9-zone memory organization system
    
    Inspired by ancient wisdom that has guided seekers for millennia.
    
    The 9 zones mirror the natural cycles of growth and transformation:
    - Zone 1: Origin - where things begin
    - Zone 2: Foundation - the base that supports
    - Zone 3: Growth - development and building
    - Zone 4: Flow - spreading and distribution
    - Zone 5: Center - the core and decision point
    - Zone 6: Structure - order and strategy
    - Zone 7: Expression - content and creation
    - Zone 8: Archive - storage and resources
    - Zone 9: Wisdom - the highest understanding
    
    The deeper meaning behind these zones is revealed in the premium version.
    """
    
    # Zone definitions
    ZONES = {
        1: {"name": "origin", "description": "Where things begin"},
        2: {"name": "foundation", "description": "The base that supports growth"},
        3: {"name": "growth", "description": "Development and building"},
        4: {"name": "flow", "description": "Spreading and distribution"},
        5: {"name": "center", "description": "The core and decision point"},
        6: {"name": "structure", "description": "Order and strategy"},
        7: {"name": "expression", "description": "Content and creation"},
        8: {"name": "archive", "description": "Storage and resources"},
        9: {"name": "wisdom", "description": "The highest understanding"},
    }
    
    # Memory type to zone mapping
    MEMORY_TYPE_TO_ZONE = {
        "origin": 1, "seed": 1, "community": 1, "sales": 1,
        "foundation": 2, "rule": 2, "law": 2, "policy": 2,
        "growth": 3, "system": 3, "tech": 3, "develop": 3,
        "flow": 4, "platform": 4, "spread": 4, "trend": 4,
        "core": 5, "center": 5, "hub": 5, "decision": 5,
        "structure": 6, "order": 6, "strategy": 6, "invest": 6,
        "expression": 7, "content": 7, "create": 7, "media": 7,
        "archive": 8, "storage": 8, "resource": 8, "history": 8,
        "wisdom": 9, "insight": 9, "philosophy": 9, "highest": 9,
    }
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        Initialize memory palace
        
        Args:
            storage_path: Storage path for persistence
        """
        self.storage_path = storage_path or "memory_palace.json"
        self.rooms: Dict[int, ZoneRoom] = {}
        self.classifier = SmartClassifier()
        self._init_rooms()
        self._load()
    
    def _init_rooms(self):
        """Initialize 9 zones"""
        for number, config in self.ZONES.items():
            self.rooms[number] = ZoneRoom(
                name=config["name"],
                zone_number=number,
                description=config["description"]
            )
    
    def _load(self):
        """Load from storage"""
        if self.storage_path == ":memory:":
            return
        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for number_str, room_data in data.items():
                    number = int(number_str)
                    if number in self.rooms:
                        self.rooms[number].memories = room_data.get("memories", [])
        except FileNotFoundError:
            pass
    
    def _save(self):
        """Save to storage"""
        if self.storage_path == ":memory:":
            return
        data = {
            str(number): room.to_dict()
            for number, room in self.rooms.items()
        }
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def classify_memory(self, memory: Dict) -> int:
        """
        Classify memory to corresponding zone
        
        Args:
            memory: Memory content with type or tags field
            
        Returns:
            Zone number (1-9)
        """
        memory_type = memory.get("type", "")
        tags = memory.get("tags", [])
        content = memory.get("content", "") or memory.get("text", "")
        
        # Check type
        if memory_type in self.MEMORY_TYPE_TO_ZONE:
            return self.MEMORY_TYPE_TO_ZONE[memory_type]
        
        # Check tags
        for tag in tags:
            if tag in self.MEMORY_TYPE_TO_ZONE:
                return self.MEMORY_TYPE_TO_ZONE[tag]
        
        # Use smart classifier for content
        if content:
            return self.classifier.classify_text(content)
        
        # Default to center
        return 5
    
    def add_memory(self, memory: Dict, zone_number: Optional[int] = None) -> ZoneRoom:
        """
        Add memory to palace
        
        Args:
            memory: Memory content
            zone_number: Specify zone, or auto-classify if None
            
        Returns:
            The room where memory was added
        """
        if zone_number is None:
            zone_number = self.classify_memory(memory)
        
        if zone_number not in self.rooms:
            zone_number = 5  # Default to center
        
        self.rooms[zone_number].add_memory(memory)
        self._save()
        
        return self.rooms[zone_number]
    
    def get_memories(self, zone_number: int) -> List[Dict]:
        """Get all memories in a zone"""
        if zone_number in self.rooms:
            return self.rooms[zone_number].memories
        return []
    
    def search(self, query: str) -> List[Dict]:
        """
        Search across all zones
        
        Args:
            query: Search keyword
            
        Returns:
            Matching memories with zone info
        """
        results = []
        query_lower = query.lower()
        
        for number, room in self.rooms.items():
            for memory in room.memories:
                content = str(memory).lower()
                if query_lower in content:
                    results.append({
                        "zone": number,
                        "zone_name": room.name,
                        "memory": memory
                    })
        
        return results
    
    def get_zone_stats(self) -> Dict:
        """
        Get statistics for each zone
        
        Returns:
            Memory count for each zone
        """
        return {
            number: {
                "name": room.name,
                "description": room.description,
                "memory_count": len(room.memories)
            }
            for number, room in self.rooms.items()
        }
    
    def get_balance_score(self) -> float:
        """
        Calculate memory balance score
        
        Ideal state: memories evenly distributed across zones
        
        Returns:
            Balance score (0-1, 1 is perfectly balanced)
        """
        counts = [len(room.memories) for room in self.rooms.values()]
        if not counts or sum(counts) == 0:
            return 1.0
        
        avg = sum(counts) / len(counts)
        if avg == 0:
            return 1.0
        
        # Calculate standard deviation
        variance = sum((c - avg) ** 2 for c in counts) / len(counts)
        std_dev = variance ** 0.5
        
        # Normalize
        balance = 1 - (std_dev / avg) if avg > 0 else 1.0
        return max(0, min(1, balance))
