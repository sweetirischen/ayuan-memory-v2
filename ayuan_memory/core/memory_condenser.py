"""
记忆压缩模块 - 将长对话压缩为精华

从OpenHands消化而来的核心能力：
1. 识别对话中的关键信息
2. 压缩冗余内容
3. 保留核心决策和经验
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass, field
from datetime import datetime
import re


@dataclass
class CompressedMemory:
    """压缩后的记忆"""
    summary: str  # 一句话总结
    key_points: List[str]  # 关键点
    decisions: List[str]  # 做出的决策
    lessons: List[str]  # 经验教训
    entities: List[str]  # 相关实体
    timestamp: str = field(default_factory=lambda: datetime.now().isoformat())
    
    def to_dict(self) -> Dict:
        return {
            "summary": self.summary,
            "key_points": self.key_points,
            "decisions": self.decisions,
            "lessons": self.lessons,
            "entities": self.entities,
            "timestamp": self.timestamp
        }
    
    @classmethod
    def from_dict(cls, data: Dict) -> "CompressedMemory":
        return cls(
            summary=data["summary"],
            key_points=data.get("key_points", []),
            decisions=data.get("decisions", []),
            lessons=data.get("lessons", []),
            entities=data.get("entities", []),
            timestamp=data.get("timestamp", datetime.now().isoformat())
        )


class MemoryCondenser:
    """记忆压缩器"""
    
    # 关键词模式
    DECISION_PATTERNS = [
        r"决定|选择|确定|采用|使用",
        r"我们(要|应该|决定)",
        r"最终方案|解决方案",
    ]
    
    LESSON_PATTERNS = [
        r"错误|问题|失败|教训",
        r"不应该|下次注意|记住",
        r"帝君教诲|帝君纠正",
    ]
    
    def __init__(self, max_summary_length: int = 200):
        """
        初始化记忆压缩器
        
        Args:
            max_summary_length: 总结最大长度
        """
        self.max_summary_length = max_summary_length
    
    def extract_key_points(self, text: str) -> List[str]:
        """
        提取关键点
        
        Args:
            text: 输入文本
            
        Returns:
            关键点列表
        """
        # 按段落分割
        paragraphs = text.split("\n\n")
        key_points = []
        
        for para in paragraphs:
            para = para.strip()
            if not para:
                continue
            
            # 提取有实质内容的段落
            if len(para) > 50 and not self._is_noise(para):
                # 压缩为一句话
                sentence = self._extract_first_sentence(para)
                if sentence and sentence not in key_points:
                    key_points.append(sentence)
        
        return key_points[:10]  # 最多10个关键点
    
    def extract_decisions(self, text: str) -> List[str]:
        """
        提取决策
        
        Args:
            text: 输入文本
            
        Returns:
            决策列表
        """
        decisions = []
        
        for pattern in self.DECISION_PATTERNS:
            matches = re.findall(rf"[^。！？]*{pattern}[^。！？]*[。！？]", text)
            for match in matches:
                match = match.strip()
                if match and match not in decisions:
                    decisions.append(match)
        
        return decisions[:5]  # 最多5个决策
    
    def extract_lessons(self, text: str) -> List[str]:
        """
        提取经验教训
        
        Args:
            text: 输入文本
            
        Returns:
            经验教训列表
        """
        lessons = []
        
        for pattern in self.LESSON_PATTERNS:
            matches = re.findall(rf"[^。！？]*{pattern}[^。！？]*[。！？]", text)
            for match in matches:
                match = match.strip()
                if match and match not in lessons:
                    lessons.append(match)
        
        return lessons[:5]  # 最多5个教训
    
    def extract_entities(self, text: str) -> List[str]:
        """
        提取实体名称
        
        Args:
            text: 输入文本
            
        Returns:
            实体名称列表
        """
        # 简单的实体提取（可以后续用EntityLinker增强）
        entities = []
        
        # 中文实体
        cn_entities = re.findall(r"[\u4e00-\u9fa5]{2,10}", text)
        entities.extend(cn_entities)
        
        # 英文实体
        en_entities = re.findall(r"[A-Z][a-zA-Z]+", text)
        entities.extend(en_entities)
        
        # 去重
        return list(set(entities))[:20]
    
    def generate_summary(self, text: str) -> str:
        """
        生成一句话总结
        
        Args:
            text: 输入文本
            
        Returns:
            总结
        """
        # 提取第一段有实质内容的文字
        paragraphs = text.split("\n\n")
        for para in paragraphs:
            para = para.strip()
            if para and len(para) > 20 and not self._is_noise(para):
                # 截断到最大长度
                if len(para) > self.max_summary_length:
                    return para[:self.max_summary_length] + "..."
                return para
        
        return "无有效内容"
    
    def _is_noise(self, text: str) -> bool:
        """判断是否是噪音"""
        noise_patterns = [
            r"^#+\s",  # 标题
            r"^```",  # 代码块
            r"^---",  # 分隔线
            r"^\*\*\*",  # 分隔线
        ]
        for pattern in noise_patterns:
            if re.match(pattern, text):
                return True
        return False
    
    def _extract_first_sentence(self, text: str) -> str:
        """提取第一句话"""
        match = re.match(r"([^。！？\n]+[。！？])", text)
        if match:
            return match.group(1)
        return text[:100] if len(text) > 100 else text
    
    def compress(self, text: str) -> CompressedMemory:
        """
        压缩记忆
        
        Args:
            text: 输入文本
            
        Returns:
            压缩后的记忆
        """
        return CompressedMemory(
            summary=self.generate_summary(text),
            key_points=self.extract_key_points(text),
            decisions=self.extract_decisions(text),
            lessons=self.extract_lessons(text),
            entities=self.extract_entities(text)
        )
    
    def compress_conversation(self, messages: List[Dict]) -> CompressedMemory:
        """
        压缩对话
        
        Args:
            messages: 对话消息列表，每条消息包含 role 和 content
            
        Returns:
            压缩后的记忆
        """
        # 合并所有消息
        full_text = "\n\n".join([
            f"[{msg.get('role', 'unknown')}]: {msg.get('content', '')}"
            for msg in messages
        ])
        
        return self.compress(full_text)
