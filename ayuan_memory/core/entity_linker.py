"""
实体链接模块 - 从文本中提取实体并建立链接

从Mem0消化而来的核心能力：
1. 从文本中提取实体（人名、项目、技术、概念）
2. 搜索是否已存在相似实体
3. 更新或创建实体记录，链接到相关记忆
"""

import re
from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import json


@dataclass
class Entity:
    """实体类"""
    name: str
    entity_type: str  # PERSON, PROJECT, TECH, CONCEPT, PLATFORM
    description: str = ""
    created_at: str = field(default_factory=lambda: datetime.now().isoformat())
    updated_at: str = field(default_factory=lambda: datetime.now().isoformat())
    related_memories: List[str] = field(default_factory=list)
    attributes: Dict = field(default_factory=dict)
    
    def to_dict(self) -> Dict:
        return {
            "name": self.name,
            "type": self.entity_type,
            "description": self.description,
            "created_at": self.created_at,
            "updated_at": self.updated_at,
            "related_memories": self.related_memories,
            "attributes": self.attributes
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "Entity":
        return cls(
            name=data["name"],
            entity_type=data["type"],
            description=data.get("description", ""),
            created_at=data.get("created_at", datetime.now().isoformat()),
            updated_at=data.get("updated_at", datetime.now().isoformat()),
            related_memories=data.get("related_memories", []),
            attributes=data.get("attributes", {})
        )


class EntityLinker:
    """实体链接器"""
    
    # 实体类型模式（改进版，减少误报）
    ENTITY_PATTERNS = {
        "PERSON": [
            r"DiJun",  # 核心人物
            r"(?<![a-zA-Z])[A-Z][a-z]+(?:\s[A-Z][a-z]+)*(?![a-zA-Z0-9])",  # 英文名（独立词，后面不能有数字）
        ],
        "PROJECT": [
            r"ZiWeiEmpire|NinePalacesSystem|AYuanCore|AYuan",
            r"(?<![a-zA-Z])[A-Z][a-zA-Z0-9]*(?:-[a-zA-Z0-9]+)+(?![a-zA-Z])",  # 项目名（必须有连字符）
        ],
        "ORG": [
            r"微软|谷歌|苹果|百度|阿里|腾讯|字节跳动|华为",
            r"(?<![a-zA-Z])Microsoft(?![a-zA-Z])",
            r"(?<![a-zA-Z])Google(?![a-zA-Z])",
            r"(?<![a-zA-Z])Apple(?![a-zA-Z])",
            r"(?<![a-zA-Z])OpenAI(?![a-zA-Z])",
            r"(?<![a-zA-Z])Anthropic(?![a-zA-Z])",
        ],
        "TECH": [
            r"(?<![a-zA-Z])AI(?![a-zA-Z])",  # AI单独是技术
            r"(?<![a-zA-Z])GitHub(?![a-zA-Z])",  # GitHub是技术平台
            r"(?<![a-zA-Z])Mem0(?![a-zA-Z])",
            r"(?<![a-zA-Z])Hermes(?![a-zA-Z])",
            r"(?<![a-zA-Z])Zep(?![a-zA-Z])",
            r"(?<![a-zA-Z])HippoRAG(?![a-zA-Z])",
            r"(?<![a-zA-Z])LangGraph(?![a-zA-Z])",
            r"(?<![a-zA-Z])CrewAI(?![a-zA-Z])",
            r"(?<![a-zA-Z])AutoGen(?![a-zA-Z])",
            r"(?<![a-zA-Z])Python(?![a-zA-Z])",
            r"(?<![a-zA-Z])JavaScript(?![a-zA-Z])",
            r"(?<![a-zA-Z])TypeScript(?![a-zA-Z])",
            r"(?<![a-zA-Z])React(?![a-zA-Z])",
            r"(?<![a-zA-Z])Vue(?![a-zA-Z])",
            r"(?<![a-zA-Z])Node(?![a-zA-Z])",
            r"(?<![a-zA-Z])LLM(?![a-zA-Z])",
            r"(?<![a-zA-Z])RAG(?![a-zA-Z])",
            r"(?<![a-zA-Z])MCP(?![a-zA-Z])",
        ],
        "CONCEPT": [
            r"洛书九宫|洛书|九宫",
            r"实体链接|记忆压缩|五脏|三垣",
            r"学习循环|自我进化|吸引进化",
        ],
        "PLATFORM": [
            r"百家号|小红书|知乎|微信公众号|飞书",
            r"(?<![a-zA-Z])Telegram(?![a-zA-Z])",
            r"(?<![a-zA-Z])Discord(?![a-zA-Z])",
            r"(?<![a-zA-Z])Slack(?![a-zA-Z])",
            r"(?<![a-zA-Z])WhatsApp(?![a-zA-Z])",
        ]
    }
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        初始化实体链接器
        
        Args:
            storage_path: 实体存储路径，默认为当前目录下的 entities.json
        """
        self.entities: Dict[str, Entity] = {}
        self.storage_path = storage_path or "entities.json"
        self._load_entities()
    
    def _load_entities(self):
        """从存储加载实体"""
        if self.storage_path == ":memory:":
            return  # 内存模式，不加载
        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
                for name, entity_data in data.items():
                    self.entities[name] = Entity.from_dict(entity_data)
        except FileNotFoundError:
            pass
    
    def _save_entities(self):
        """保存实体到存储"""
        if self.storage_path == ":memory:":
            return  # 内存模式，不保存
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(
                {name: entity.to_dict() for name, entity in self.entities.items()},
                f,
                ensure_ascii=False,
                indent=2
            )
    
    def extract_entities(self, text: str) -> List[Tuple[str, str]]:
        """
        从文本中提取实体
        
        Args:
            text: 输入文本
            
        Returns:
            List of (entity_name, entity_type) tuples
        """
        found_entities = []
        seen_names = set()  # 用于去重
        
        # 定义优先级：TECH > ORG > PROJECT > PLATFORM > CONCEPT > PERSON
        type_priority = {"TECH": 1, "ORG": 2, "PROJECT": 3, "PLATFORM": 4, "CONCEPT": 5, "PERSON": 6}
        type_order = sorted(self.ENTITY_PATTERNS.keys(), key=lambda t: type_priority.get(t, 99))
        
        for entity_type in type_order:
            patterns = self.ENTITY_PATTERNS[entity_type]
            for pattern in patterns:
                matches = re.findall(pattern, text)
                for match in matches:
                    if isinstance(match, tuple):
                        match = match[0]
                    if match and match not in seen_names:
                        found_entities.append((match, entity_type))
                        seen_names.add(match)
        
        return found_entities
    
    def link_entity(self, name: str, entity_type: str, memory_id: str, description: str = "") -> Entity:
        """
        链接实体到记忆
        
        Args:
            name: 实体名称
            entity_type: 实体类型
            memory_id: 相关记忆ID
            description: 实体描述
            
        Returns:
            Entity对象
        """
        if name in self.entities:
            # 更新已有实体
            entity = self.entities[name]
            if memory_id not in entity.related_memories:
                entity.related_memories.append(memory_id)
            if description and description not in entity.description:
                entity.description = f"{entity.description}; {description}".strip("; ")
            entity.updated_at = datetime.now().isoformat()
        else:
            # 创建新实体
            entity = Entity(
                name=name,
                entity_type=entity_type,
                description=description,
                related_memories=[memory_id]
            )
            self.entities[name] = entity
        
        self._save_entities()
        return entity
    
    def get_entity(self, name: str) -> Optional[Entity]:
        """获取实体"""
        return self.entities.get(name)
    
    def search_entities(self, query: str) -> List[Entity]:
        """
        搜索实体
        
        Args:
            query: 搜索关键词
            
        Returns:
            匹配的实体列表
        """
        results = []
        query_lower = query.lower()
        
        for entity in self.entities.values():
            if (query_lower in entity.name.lower() or
                query_lower in entity.description.lower() or
                query_lower in entity.entity_type.lower()):
                results.append(entity)
        
        return results
    
    def get_entities_by_type(self, entity_type: str) -> List[Entity]:
        """按类型获取实体"""
        return [e for e in self.entities.values() if e.entity_type == entity_type]
    
    def process_text(self, text: str, memory_id: str) -> List[Entity]:
        """
        处理文本，提取并链接所有实体
        
        Args:
            text: 输入文本
            memory_id: 相关记忆ID
            
        Returns:
            链接的实体列表
        """
        entities = self.extract_entities(text)
        linked = []
        
        for name, entity_type in entities:
            entity = self.link_entity(name, entity_type, memory_id)
            linked.append(entity)
        
        return linked
    
    def get_entity_index(self) -> Dict[str, Dict]:
        """
        获取实体索引
        
        Returns:
            实体名称到相关记忆位置的映射
        """
        return {
            name: {
                "type": entity.entity_type,
                "related_memories": entity.related_memories
            }
            for name, entity in self.entities.items()
        }
