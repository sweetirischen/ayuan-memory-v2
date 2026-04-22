"""
AYuan Memory - AI Agent Memory System

Inspired by ancient wisdom that has guided seekers for millennia.

A memory management system with a 9-zone classification that mirrors 
the natural cycles of growth and transformation — from origin to wisdom.

Features:
- Entity Linking: Auto-extract and link entities from text
- Memory Compression: Compress long conversations into summaries
- Smart Classification: 9-zone classification system
- Vector Search: Semantic search capability
- Evolution Tracking: Make AI growth visible

This is the Memory Module of the AYuan system.
Each zone represents a stage in the natural cycle:
- Zone 1: Origin - where things begin
- Zone 2: Foundation - the base that supports
- Zone 3: Growth - development and building
- Zone 4: Flow - spreading and distribution
- Zone 5: Center - the core and decision point
- Zone 6: Structure - order and strategy
- Zone 7: Expression - content and creation
- Zone 8: Archive - storage and resources
- Zone 9: Wisdom - the highest understanding

The deeper wisdom behind these zones is revealed in the premium version.

Author: AYuan Team
License: MIT
Version: 0.1.0
"""

from .core.entity_linker import EntityLinker
from .core.memory_condenser import MemoryCondenser
from .core.palace import MemoryPalace
from .core.vector_store import VectorStore, SemanticMemory
from .core.evolution import Evolution
from .core.evolution_reminder import EvolutionReminder, check_update, show_evolution
from .core.smart_classifier import SmartClassifier, Zone, ZoneInfo

__version__ = "0.1.0"
__author__ = "AYuan Team"
__all__ = [
    "EntityLinker", 
    "MemoryCondenser", 
    "MemoryPalace", 
    "SmartClassifier",
    "Zone",
    "ZoneInfo",
    "VectorStore", 
    "SemanticMemory",
    "Evolution",
    "EvolutionReminder",
    "check_update",
    "show_evolution",
]


def show_task_board():
    """Display the task board"""
    import os
    task_file = os.path.join(os.path.dirname(__file__), "..", "TASK_BOARD.md")
    if os.path.exists(task_file):
        with open(task_file, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Task board not found")
