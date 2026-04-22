"""
Evolution Module - 让AI进化可见

用户可以看到：
- 当前版本学会了什么
- 历史进化记录
- 未来计划
- 能力清单
"""

from typing import List, Dict, Optional
from dataclasses import dataclass, field
from datetime import datetime
import json


@dataclass
class EvolutionRecord:
    """进化记录"""
    version: str
    date: str
    learned: List[str]  # 学会了什么
    improved: List[str] = field(default_factory=list)  # 改进了什么
    metrics: Dict[str, float] = field(default_factory=dict)  # 指标
    
    def to_dict(self) -> Dict:
        return {
            "version": self.version,
            "date": self.date,
            "learned": self.learned,
            "improved": self.improved,
            "metrics": self.metrics
        }


@dataclass 
class FuturePlan:
    """未来计划"""
    feature: str
    priority: str  # high, medium, low
    status: str  # planned, in_progress, done
    
    def to_dict(self) -> Dict:
        return {
            "feature": self.feature,
            "priority": self.priority,
            "status": self.status
        }


class Evolution:
    """
    进化系统 - 让AI成长可见
    
    使用方式：
        from ayuan_memory import Evolution
        
        evo = Evolution()
        evo.show_evolution()  # 显示进化历史
        evo.show_abilities()  # 显示当前能力
        evo.show_plans()      # 显示未来计划
    """
    
    # 进化历史（版本记录）
    EVOLUTION_HISTORY: List[EvolutionRecord] = [
        EvolutionRecord(
            version="0.1.0",
            date="2026-04-22",
            learned=[
                "Entity Linking - extract entities from text",
                "Memory Compression - compress long conversations",
                "Nine Palaces Classification - organize memories by Luoshu",
                "Vector Search - semantic search with TF-IDF",
            ],
            improved=[],
            metrics={
                "entity_linking_accuracy": 1.0,
                "nine_palaces_accuracy": 1.0,
                "compression_rate": 0.569,
            }
        ),
    ]
    
    # 当前能力
    ABILITIES: Dict[str, Dict] = {
        "entity_linking": {
            "name": "Entity Linking",
            "description": "Extract and link entities from text",
            "accuracy": 1.0,
            "speed_ms": 1.59,
            "status": "active",
        },
        "memory_compression": {
            "name": "Memory Compression",
            "description": "Compress long conversations into summaries",
            "compression_rate": 0.569,
            "speed_ms": 9.93,
            "status": "active",
        },
        "nine_palaces": {
            "name": "Nine Palaces Classification",
            "description": "Classify memories by Luoshu Nine Palaces philosophy",
            "accuracy": 1.0,
            "speed_ms": 0.0,
            "status": "active",
        },
        "vector_search": {
            "name": "Vector Search",
            "description": "Semantic search with TF-IDF (zero dependency)",
            "accuracy": 1.0,
            "speed_ms": 0.25,
            "status": "active",
        },
    }
    
    # 未来计划
    FUTURE_PLANS: List[FuturePlan] = [
        FuturePlan("Graph Database - entity relationship storage", "high", "planned"),
        FuturePlan("LLM Enhancement - better semantic understanding", "high", "planned"),
        FuturePlan("Embedding Vector Mode - with sentence-transformers", "medium", "planned"),
        FuturePlan("REST API - easy integration", "medium", "planned"),
        FuturePlan("Cloud Storage - multi-backend support", "low", "planned"),
    ]
    
    def __init__(self, storage_path: Optional[str] = None):
        """
        初始化进化系统
        
        Args:
            storage_path: 存储路径（可选）
        """
        self.storage_path = storage_path
        self.history = list(self.EVOLUTION_HISTORY)
        self.abilities = dict(self.ABILITIES)
        self.plans = list(self.FUTURE_PLANS)
    
    def show_evolution(self) -> str:
        """
        显示进化历史
        
        Returns:
            格式化的进化历史字符串
        """
        lines = []
        lines.append("=" * 50)
        lines.append("  AYuan Evolution History")
        lines.append("=" * 50)
        lines.append("")
        
        for record in reversed(self.history):
            lines.append(f"v{record.version} ({record.date})")
            for item in record.learned:
                lines.append(f"  + Learned: {item}")
            for item in record.improved:
                lines.append(f"  ^ Improved: {item}")
            if record.metrics:
                lines.append(f"  Metrics: {self._format_metrics(record.metrics)}")
            lines.append("")
        
        lines.append("=" * 50)
        lines.append(f"  Total Evolutions: {len(self.history)}")
        lines.append(f"  Current Version: v{self.history[-1].version}")
        lines.append("=" * 50)
        
        result = "\n".join(lines)
        print(result)
        return result
    
    def show_abilities(self) -> str:
        """
        显示当前能力
        
        Returns:
            格式化的能力清单字符串
        """
        lines = []
        lines.append("=" * 50)
        lines.append("  AYuan Current Abilities")
        lines.append("=" * 50)
        lines.append("")
        
        for key, ability in self.abilities.items():
            status_icon = "[OK]" if ability["status"] == "active" else "[--]"
            lines.append(f"{status_icon} {ability['name']}")
            lines.append(f"    {ability['description']}")
            if "accuracy" in ability:
                lines.append(f"    Accuracy: {ability['accuracy']:.1%}")
            if "speed_ms" in ability:
                lines.append(f"    Speed: {ability['speed_ms']:.2f}ms")
            lines.append("")
        
        lines.append("=" * 50)
        lines.append(f"  Total Abilities: {len(self.abilities)}")
        lines.append("=" * 50)
        
        result = "\n".join(lines)
        print(result)
        return result
    
    def show_plans(self) -> str:
        """
        显示未来计划
        
        Returns:
            格式化的计划清单字符串
        """
        lines = []
        lines.append("=" * 50)
        lines.append("  AYuan Future Plans")
        lines.append("=" * 50)
        lines.append("")
        
        priority_order = {"high": 1, "medium": 2, "low": 3}
        sorted_plans = sorted(self.plans, key=lambda p: priority_order.get(p.priority, 99))
        
        for plan in sorted_plans:
            priority_icon = {"high": "!!!", "medium": "!! ", "low": "!  "}
            status_icon = {"planned": "[ ]", "in_progress": "[>]", "done": "[X]"}
            
            icon = priority_icon.get(plan.priority, "   ")
            status = status_icon.get(plan.status, "[?]")
            
            lines.append(f"{icon} {status} {plan.feature}")
        
        lines.append("")
        lines.append("=" * 50)
        lines.append(f"  Total Plans: {len(self.plans)}")
        lines.append("=" * 50)
        
        result = "\n".join(lines)
        print(result)
        return result
    
    def show_all(self) -> str:
        """
        显示完整进化报告
        
        Returns:
            格式化的完整报告字符串
        """
        lines = []
        lines.append("")
        lines.append("╔" + "═" * 48 + "╗")
        lines.append("║" + " AYuan Memory System - Evolution Report ".center(48) + "║")
        lines.append("╚" + "═" * 48 + "╝")
        lines.append("")
        
        # 当前版本
        current = self.history[-1]
        lines.append(f"Current Version: v{current.version}")
        lines.append(f"Last Evolution: {current.date}")
        lines.append("")
        
        # 能力统计
        lines.append("Abilities Overview:")
        lines.append(f"  - Total: {len(self.abilities)}")
        lines.append(f"  - Active: {sum(1 for a in self.abilities.values() if a['status'] == 'active')}")
        lines.append("")
        
        # 进化统计
        lines.append("Evolution Stats:")
        lines.append(f"  - Total Evolutions: {len(self.history)}")
        lines.append(f"  - Total Learned: {sum(len(r.learned) for r in self.history)}")
        lines.append("")
        
        # 未来计划
        lines.append("Future Plans:")
        high_priority = sum(1 for p in self.plans if p.priority == "high")
        lines.append(f"  - High Priority: {high_priority}")
        lines.append(f"  - Total Plans: {len(self.plans)}")
        lines.append("")
        
        lines.append("─" * 50)
        lines.append("Use show_evolution(), show_abilities(), show_plans() for details")
        lines.append("─" * 50)
        
        result = "\n".join(lines)
        print(result)
        return result
    
    def _format_metrics(self, metrics: Dict[str, float]) -> str:
        """格式化指标"""
        parts = []
        for key, value in metrics.items():
            if "accuracy" in key:
                parts.append(f"{key}={value:.1%}")
            else:
                parts.append(f"{key}={value:.3f}")
        return ", ".join(parts)
    
    def add_evolution(self, record: EvolutionRecord):
        """
        添加进化记录
        
        Args:
            record: 进化记录
        """
        self.history.append(record)
    
    def add_ability(self, key: str, ability: Dict):
        """
        添加能力
        
        Args:
            key: 能力键
            ability: 能力信息
        """
        self.abilities[key] = ability
    
    def update_plan_status(self, feature: str, status: str):
        """
        更新计划状态
        
        Args:
            feature: 功能名称
            status: 新状态
        """
        for plan in self.plans:
            if plan.feature == feature:
                plan.status = status
                break
    
    def get_version(self) -> str:
        """获取当前版本号"""
        return self.history[-1].version if self.history else "0.0.0"
    
    def __repr__(self) -> str:
        return f"Evolution(version={self.get_version()}, abilities={len(self.abilities)})"
