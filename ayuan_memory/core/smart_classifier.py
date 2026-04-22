"""
Smart Classifier - A 9-zone classification system inspired by ancient wisdom.

This classifier organizes memories into 9 zones that mirror the natural cycles
of growth and transformation — from origin to wisdom.

Zone meanings (simplified):
- Zone 1: Origin - seeds, beginnings, ideas
- Zone 2: Foundation - basics, rules, frameworks
- Zone 3: Growth - development, systems, building
- Zone 4: Flow - spreading, platforms, distribution
- Zone 5: Center - core, decisions, hub
- Zone 6: Structure - order, strategy, management
- Zone 7: Expression - content, creation, publishing
- Zone 8: Archive - storage, resources, history
- Zone 9: Wisdom - insights, philosophy, highest level
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class Zone(Enum):
    """9 zones for memory classification"""
    ORIGIN = 1      # Seeds, beginnings
    FOUNDATION = 2  # Basics, rules
    GROWTH = 3      # Development, systems
    FLOW = 4        # Spreading, platforms
    CENTER = 5      # Core, decisions
    STRUCTURE = 6   # Order, strategy
    EXPRESSION = 7  # Content, creation
    ARCHIVE = 8     # Storage, resources
    WISDOM = 9      # Insights, philosophy


@dataclass
class ZoneInfo:
    """Zone information"""
    number: int
    name: str
    keywords: List[str]
    description: str


class SmartClassifier:
    """
    Smart Classifier - 9-zone classification system
    
    Inspired by ancient wisdom that has guided seekers for millennia.
    Each zone represents a stage in the natural cycle of growth and transformation.
    """
    
    # Zone definitions
    ZONE_INFO: Dict[int, ZoneInfo] = {
        1: ZoneInfo(
            number=1, name="origin", 
            keywords=["seed", "beginning", "start", "idea", "origin", "community", "sales"],
            description="Origin - where things begin"
        ),
        2: ZoneInfo(
            number=2, name="foundation",
            keywords=["basic", "rule", "law", "policy", "framework", "foundation"],
            description="Foundation - the base that supports growth"
        ),
        3: ZoneInfo(
            number=3, name="growth",
            keywords=["develop", "system", "build", "code", "tech", "engineer", "growth"],
            description="Growth - development and building"
        ),
        4: ZoneInfo(
            number=4, name="flow",
            keywords=["spread", "platform", "trend", "distribute", "flow", "promote"],
            description="Flow - spreading and distribution"
        ),
        5: ZoneInfo(
            number=5, name="center",
            keywords=["core", "hub", "center", "key", "important", "decision"],
            description="Center - the core and decision point"
        ),
        6: ZoneInfo(
            number=6, name="structure",
            keywords=["order", "strategy", "invest", "manage", "enterprise", "structure"],
            description="Structure - order and strategy"
        ),
        7: ZoneInfo(
            number=7, name="expression",
            keywords=["content", "create", "publish", "express", "media", "article", "video"],
            description="Expression - content and creation"
        ),
        8: ZoneInfo(
            number=8, name="archive",
            keywords=["store", "archive", "resource", "memory", "history", "knowledge"],
            description="Archive - storage and resources"
        ),
        9: ZoneInfo(
            number=9, name="wisdom",
            keywords=["wisdom", "insight", "philosophy", "create", "invent", "highest", "wisdom"],
            description="Wisdom - the highest level of understanding"
        ),
    }
    
    # Generation order (natural cycle)
    GENERATION_ORDER = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def __init__(self):
        """Initialize the classifier"""
        pass
    
    def get_zone(self, number: int) -> Optional[ZoneInfo]:
        """Get zone information"""
        return self.ZONE_INFO.get(number)
    
    def get_zone_by_name(self, name: str) -> Optional[ZoneInfo]:
        """Get zone by name"""
        name_lower = name.lower()
        for info in self.ZONE_INFO.values():
            if info.name == name_lower:
                return info
        return None
    
    def classify_text(self, text: str) -> int:
        """
        Classify text to corresponding zone
        
        Uses weighted keyword matching for accurate classification.
        
        Args:
            text: Input text
            
        Returns:
            Zone number (1-9)
        """
        text_lower = text.lower()
        
        # Weighted keywords for each zone
        keywords_weighted = {
            # Zone 9: Wisdom (highest priority)
            9: [
                ("create", 3), ("invent", 3), ("wisdom", 2), ("philosophy", 2),
                ("insight", 2), ("highest", 1)
            ],
            # Zone 6: Structure
            6: [
                ("invest", 3), ("strategy", 3), ("enterprise", 3),
                ("manage", 2), ("order", 2), ("decision", 2)
            ],
            # Zone 3: Growth
            3: [
                ("tech", 3), ("develop", 3), ("code", 3), ("system", 2),
                ("build", 2), ("engineer", 2), ("programming", 2),
                ("Mem0", 3), ("GitHub", 3), ("Python", 3), ("AI", 2),
                ("stars", 1), ("open source", 2)
            ],
            # Zone 7: Expression
            7: [
                ("content", 3), ("create", 3), ("publish", 3), ("express", 2),
                ("media", 2), ("article", 2), ("writing", 2), ("video", 2)
            ],
            # Zone 1: Origin
            1: [
                ("community", 3), ("sales", 3), ("ecommerce", 3),
                ("origin", 2), ("seed", 2), ("start", 1), ("idea", 1)
            ],
            # Zone 4: Flow
            4: [
                ("platform", 3), ("spread", 2), ("trend", 2),
                ("distribute", 2), ("promote", 2), ("flow", 2)
            ],
            # Zone 8: Archive
            8: [
                ("store", 3), ("archive", 3), ("memory", 2), ("resource", 2),
                ("history", 2), ("knowledge base", 3)
            ],
            # Zone 2: Foundation
            2: [
                ("basic", 2), ("rule", 3), ("law", 3), ("policy", 3),
                ("framework", 2), ("foundation", 2)
            ],
            # Zone 5: Center
            5: [
                ("core", 2), ("hub", 2), ("center", 2), ("key", 1),
                ("important", 1)
            ]
        }
        
        # Calculate scores for each zone
        scores = {i: 0 for i in range(1, 10)}
        
        for zone, keywords in keywords_weighted.items():
            for keyword, weight in keywords:
                if keyword in text_lower:
                    scores[zone] += weight
        
        # Find the zone with highest score
        max_score = max(scores.values())
        if max_score == 0:
            return 5  # Default to center
        
        # Return the zone with highest score
        for zone, score in scores.items():
            if score == max_score:
                return zone
        
        return 5
    
    def get_generation_path(self) -> List[int]:
        """
        Get the generation path
        
        Returns:
            Zone numbers in generation order
        """
        return self.GENERATION_ORDER
    
    def check_balance(self, zone_counts: Dict[int, int]) -> Tuple[bool, float]:
        """
        Check if memory distribution is balanced
        
        Args:
            zone_counts: Memory count for each zone
            
        Returns:
            (is_balanced, balance_score)
        """
        counts = [zone_counts.get(i, 0) for i in range(1, 10)]
        
        if sum(counts) == 0:
            return True, 1.0
        
        avg = sum(counts) / len(counts)
        if avg == 0:
            return True, 1.0
        
        # Calculate standard deviation
        variance = sum((c - avg) ** 2 for c in counts) / len(counts)
        std_dev = variance ** 0.5
        
        # Normalize
        balance_score = 1 - (std_dev / avg) if avg > 0 else 1.0
        balance_score = max(0, min(1, balance_score))
        
        # Balance threshold
        is_balanced = balance_score > 0.7
        
        return is_balanced, balance_score
    
    def get_zone_element(self, zone_number: int) -> Optional[str]:
        """
        Get the element associated with a zone
        
        This is a simplified version. Full version available in premium package.
        
        Args:
            zone_number: Zone number (1-9)
            
        Returns:
            Element name or None
        """
        # Simplified element mapping
        elements = {
            1: "water", 2: "earth", 3: "wood",
            4: "wood", 5: "earth", 6: "metal",
            7: "metal", 8: "earth", 9: "fire"
        }
        return elements.get(zone_number)
