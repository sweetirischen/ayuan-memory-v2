"""
记忆宫殿模块 - 阿垣独有的记忆组织方式

融合九宫哲学的记忆管理系统：
1. 九宫分类：按洛书九宫组织记忆
2. 三垣架构：天垣（法则）、地垣（运作）、人垣（执行）
3. 五脏映射：心肝脾肺肾对应不同能力
"""

from typing import Dict, List, Optional
from dataclasses import dataclass, field
from datetime import datetime
import json


@dataclass
class PalaceRoom:
    """宫殿房间"""
    name: str
    position: str  # 宫位（如"坎宫"、"离宫"）
    element: str  # 五行
    meaning: str  # 含义
    memories: List[Dict] = field(default_factory=list)
    
    def add_memory(self, memory: Dict):
        """添加记忆"""
        memory["added_at"] = datetime.now().isoformat()
        self.memories.append(memory)
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "position": self.position,
            "element": self.element,
            "meaning": self.meaning,
            "memories": self.memories
        }


class MemoryPalace:
    """
    记忆宫殿
    
    基于洛书九宫的记忆组织系统：
    
    ```
      4(巽)  9(离)  2(坤)
      3(震)  5(中)  7(兑)
      8(艮)  1(坎)  6(乾)
    ```
    
    核心法则：每行、每列、每对角线之和 = 15（宇宙平衡数）
    """
    
    # 九宫定义
    NINE_PALACES = {
        1: {"name": "坎宫", "element": "水", "meaning": "起源·种子", "trigram": "坎"},
        2: {"name": "坤宫", "element": "土", "meaning": "承载·地基", "trigram": "坤"},
        3: {"name": "震宫", "element": "木", "meaning": "生发·成长", "trigram": "震"},
        4: {"name": "巽宫", "element": "木", "meaning": "运化·传播", "trigram": "巽"},
        5: {"name": "中宫", "element": "土", "meaning": "枢纽·核心", "trigram": "中"},
        6: {"name": "乾宫", "element": "金", "meaning": "收敛·秩序", "trigram": "乾"},
        7: {"name": "兑宫", "element": "金", "meaning": "显现·表达", "trigram": "兑"},
        8: {"name": "艮宫", "element": "土", "meaning": "存储·归档", "trigram": "艮"},
        9: {"name": "离宫", "element": "火", "meaning": "升华·智慧", "trigram": "离"},
    }
    
    # 记忆类型到宫位的映射
    MEMORY_TYPE_TO_PALACE = {
        "origin": 1,      # 起源 → 坎宫
        "seed": 1,        # 种子 → 坎宫
        "foundation": 2,  # 基础 → 坤宫
        "rule": 2,        # 规则 → 坤宫
        "growth": 3,      # 成长 → 震宫
        "system": 3,      # 系统 → 震宫
        "spread": 4,      # 传播 → 巽宫
        "platform": 4,    # 平台 → 巽宫
        "core": 5,        # 核心 → 中宫
        "decision": 5,    # 决策 → 中宫
        "order": 6,       # 秩序 → 乾宫
        "strategy": 6,    # 战略 → 乾宫
        "expression": 7,  # 表达 → 兑宫
        "content": 7,     # 内容 → 兑宫
        "storage": 8,     # 存储 → 艮宫
        "archive": 8,     # 归档 → 艮宫
        "wisdom": 9,      # 智慧 → 离宫
        "insight": 9,     # 洞察 → 离宫
    }
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        初始化记忆宫殿
        
        Args:
            storage_path: 存储路径
        """
        self.storage_path = storage_path or "memory_palace.json"
        self.rooms: Dict[int, PalaceRoom] = {}
        self._init_rooms()
        self._load()
    
    def _init_rooms(self):
        """初始化九宫房间"""
        for number, config in self.NINE_PALACES.items():
            self.rooms[number] = PalaceRoom(
                name=config["name"],
                position=f"{config['trigram']}宫",
                element=config["element"],
                meaning=config["meaning"]
            )
    
    def _load(self):
        """从存储加载"""
        if self.storage_path == ":memory:":
            return  # 内存模式，不加载
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
        """保存到存储"""
        if self.storage_path == ":memory:":
            return  # 内存模式，不保存
        data = {
            str(number): room.to_dict()
            for number, room in self.rooms.items()
        }
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def classify_memory(self, memory: Dict) -> int:
        """
        分类记忆到对应宫位
        
        Args:
            memory: 记忆内容，应包含 type 或 tags 字段
            
        Returns:
            宫位数字（1-9）
        """
        memory_type = memory.get("type", "")
        tags = memory.get("tags", [])
        
        # 检查类型
        if memory_type in self.MEMORY_TYPE_TO_PALACE:
            return self.MEMORY_TYPE_TO_PALACE[memory_type]
        
        # 检查标签
        for tag in tags:
            if tag in self.MEMORY_TYPE_TO_PALACE:
                return self.MEMORY_TYPE_TO_PALACE[tag]
        
        # 默认放入中宫
        return 5
    
    def add_memory(self, memory: Dict, palace_number: Optional[int] = None) -> PalaceRoom:
        """
        添加记忆到宫殿
        
        Args:
            memory: 记忆内容
            palace_number: 指定宫位，不指定则自动分类
            
        Returns:
            添加到的房间
        """
        if palace_number is None:
            palace_number = self.classify_memory(memory)
        
        if palace_number not in self.rooms:
            palace_number = 5  # 默认中宫
        
        self.rooms[palace_number].add_memory(memory)
        self._save()
        
        return self.rooms[palace_number]
    
    def get_memories(self, palace_number: int) -> List[Dict]:
        """获取某宫位的所有记忆"""
        if palace_number in self.rooms:
            return self.rooms[palace_number].memories
        return []
    
    def search(self, query: str) -> List[Dict]:
        """
        在所有宫位中搜索
        
        Args:
            query: 搜索关键词
            
        Returns:
            匹配的记忆列表，包含宫位信息
        """
        results = []
        query_lower = query.lower()
        
        for number, room in self.rooms.items():
            for memory in room.memories:
                content = str(memory).lower()
                if query_lower in content:
                    results.append({
                        "palace": number,
                        "palace_name": room.name,
                        "memory": memory
                    })
        
        return results
    
    def get_palace_stats(self) -> Dict:
        """
        获取各宫位统计
        
        Returns:
            各宫位记忆数量
        """
        return {
            number: {
                "name": room.name,
                "element": room.element,
                "meaning": room.meaning,
                "memory_count": len(room.memories)
            }
            for number, room in self.rooms.items()
        }
    
    def get_balance_score(self) -> float:
        """
        计算记忆平衡分数
        
        理想状态：各宫位记忆数量接近
        
        Returns:
            平衡分数（0-1，1为完全平衡）
        """
        counts = [len(room.memories) for room in self.rooms.values()]
        if not counts or sum(counts) == 0:
            return 1.0
        
        avg = sum(counts) / len(counts)
        if avg == 0:
            return 1.0
        
        # 计算标准差
        variance = sum((c - avg) ** 2 for c in counts) / len(counts)
        std_dev = variance ** 0.5
        
        # 归一化
        balance = 1 - (std_dev / avg) if avg > 0 else 1.0
        return max(0, min(1, balance))
