"""
Ayuan Memory - AI Agent Memory System with Chinese Philosophy

A memory management system based on Luoshu Nine Palaces philosophy.

Features:
- Entity Linking: Auto-extract and link entities
- Memory Compression: Compress long conversations
- Nine Palaces Classification: Organize memories by Luoshu
- Vector Search: Semantic search capability
- Evolution: Make AI growth visible

Author: AYuan Team
License: MIT
"""

from .core.entity_linker import EntityLinker
from .core.memory_condenser import MemoryCondenser
from .core.palace import MemoryPalace
from .core.vector_store import VectorStore, SemanticMemory
from .core.evolution import Evolution
from .core.evolution_reminder import EvolutionReminder, check_update, show_evolution
from .palace.nine_palaces import NinePalaces

__version__ = "0.1.0"
__all__ = [
    "EntityLinker", 
    "MemoryCondenser", 
    "MemoryPalace", 
    "NinePalaces", 
    "VectorStore", 
    "SemanticMemory",
    "Evolution",
    "EvolutionReminder",
    "check_update",
    "show_evolution",
]


def show_task_board():
    """显示任务栏"""
    import os
    task_file = os.path.join(os.path.dirname(__file__), "..", "TASK_BOARD.md")
    if os.path.exists(task_file):
        with open(task_file, "r", encoding="utf-8") as f:
            print(f.read())
    else:
        print("Task board not found")
