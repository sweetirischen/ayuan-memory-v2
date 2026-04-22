"""
Ayuan Memory - AI Agent Memory System with Chinese Philosophy

一个融合九宫哲学的AI记忆管理系统。

特点：
- 实体链接：自动提取和链接实体
- 记忆压缩：长对话压缩为精华
- 九宫分类：按洛书九宫组织记忆
- 身国映射：五脏六腑与AI能力对应

Author: 阿垣 (Ayuan) & 帝君
License: MIT
"""

from .core.entity_linker import EntityLinker
from .core.memory_condenser import MemoryCondenser
from .core.palace import MemoryPalace
from .palace.nine_palaces import NinePalaces

__version__ = "0.1.0"
__all__ = ["EntityLinker", "MemoryCondenser", "MemoryPalace", "NinePalaces"]
