"""
九宫分类模块 - 基于洛书九宫的记忆分类

洛书九宫数字布局：
  4(巽)  9(离)  2(坤)
  3(震)  5(中)  7(兑)
  8(艮)  1(坎)  6(乾)

核心法则：每行、每列、每对角线之和 = 15（宇宙平衡数）

世界诞生的数字序列：
1(水·起源) → 2(土·承载) → 3(木·生发) → 4(木·运化) → 5(土·核心)
→ 6(金·收敛) → 7(金·显现) → 8(土·存储) → 9(火·升华)
"""

from typing import Dict, List, Optional, Tuple
from dataclasses import dataclass
from enum import Enum


class Palace(Enum):
    """九宫枚举"""
    KAN = 1   # 坎宫·水·起源
    KUN = 2   # 坤宫·土·承载
    ZHEN = 3  # 震宫·木·生发
    XUN = 4   # 巽宫·木·运化
    ZHONG = 5 # 中宫·土·核心
    QIAN = 6  # 乾宫·金·收敛
    DUI = 7   # 兑宫·金·显现
    GEN = 8   # 艮宫·土·存储
    LI = 9    # 离宫·火·升华


@dataclass
class PalaceInfo:
    """宫位信息"""
    number: int
    name: str
    trigram: str
    element: str
    meaning: str
    social_class: str  # 社会阶层
    money_direction: str  # 赚钱方向
    generation_phase: str  # 生成阶段


class NinePalaces:
    """
    九宫分类系统
    
    基于洛书九宫的记忆分类和组织系统
    """
    
    # 宫位详细信息
    PALACE_INFO: Dict[int, PalaceInfo] = {
        1: PalaceInfo(
            number=1, name="坎宫", trigram="坎", element="水",
            meaning="起源·种子·混沌初开",
            social_class="社群运营、销售",
            money_direction="社群变现、电商带货",
            generation_phase="起源：混沌初开，万物之始"
        ),
        2: PalaceInfo(
            number=2, name="坤宫", trigram="坤", element="土",
            meaning="承载·地基·容纳万物",
            social_class="政策制定者、法律专家",
            money_direction="政策咨询、法律服务",
            generation_phase="承载：地基形成，容纳万物"
        ),
        3: PalaceInfo(
            number=3, name="震宫", trigram="震", element="木",
            meaning="生发·成长·生命力涌现",
            social_class="技术专家、工程师",
            money_direction="技术开发、系统建设",
            generation_phase="生发：生命力涌现，向上生长"
        ),
        4: PalaceInfo(
            number=4, name="巽宫", trigram="巽", element="木",
            meaning="运化·传播·气机流转",
            social_class="平台运营、趋势分析师",
            money_direction="平台运营、趋势研判",
            generation_phase="运化：气机流转，传播扩散"
        ),
        5: PalaceInfo(
            number=5, name="中宫", trigram="中", element="土",
            meaning="枢纽·核心·一切交汇点",
            social_class="教育者、文化传播者",
            money_direction="知识付费、教育培训",
            generation_phase="枢纽：核心、平衡、一切交汇点"
        ),
        6: PalaceInfo(
            number=6, name="乾宫", trigram="乾", element="金",
            meaning="收敛·秩序·结构形成",
            social_class="企业家、投资人",
            money_direction="企业管理、投资战略",
            generation_phase="收敛：结构形成，秩序建立"
        ),
        7: PalaceInfo(
            number=7, name="兑宫", trigram="兑", element="金",
            meaning="显现·表达·可见之象",
            social_class="内容创作者、自媒体人",
            money_direction="内容变现、自媒体收入",
            generation_phase="显现：表达、呈现、可见之象"
        ),
        8: PalaceInfo(
            number=8, name="艮宫", trigram="艮", element="土",
            meaning="存储·归档·记忆固化",
            social_class="资源管理者",
            money_direction="资源整合、信息服务",
            generation_phase="存储：沉淀、归档、记忆固化"
        ),
        9: PalaceInfo(
            number=9, name="离宫", trigram="离", element="火",
            meaning="升华·智慧·最高维度",
            social_class="思想家、哲学家",
            money_direction="智慧传播、心灵服务",
            generation_phase="升华：智慧、光、最高维度"
        ),
    }
    
    # 三垣架构
    THREE_YUAN = {
        "天垣": {  # 法则层
            "palaces": [9, 2, 5],  # 离、坤、中
            "meaning": "法则层，藏精气",
            "focus": "升华、承载、核心"
        },
        "地垣": {  # 运作层
            "palaces": [3, 6, 8],  # 震、乾、艮
            "meaning": "运作层，传化物",
            "focus": "生发、收敛、存储"
        },
        "人垣": {  # 执行层
            "palaces": [4, 7, 1],  # 巽、兑、坎
            "meaning": "执行层，皮肉筋骨脉",
            "focus": "运化、显现、起源"
        }
    }
    
    # 生成顺序
    GENERATION_ORDER = [1, 2, 3, 4, 5, 6, 7, 8, 9]
    
    def __init__(self):
        """初始化九宫系统"""
        pass
    
    def get_palace(self, number: int) -> Optional[PalaceInfo]:
        """获取宫位信息"""
        return self.PALACE_INFO.get(number)
    
    def get_palace_by_name(self, name: str) -> Optional[PalaceInfo]:
        """通过名称获取宫位"""
        for info in self.PALACE_INFO.values():
            if info.name == name or info.trigram in name:
                return info
        return None
    
    def classify_text(self, text: str) -> int:
        """
        分类文本到对应宫位
        
        改进版：使用权重和多维度匹配
        
        Args:
            text: 输入文本
            
        Returns:
            宫位数字（1-9）
        """
        text_lower = text.lower()
        
        # 关键词 + 权重（权重越高，优先级越高）
        keywords_weighted = {
            # 离宫·升华（最高优先级，代表创造、智慧、哲学）
            9: [
                ("创建", 3), ("创造", 3), ("发明", 3), ("智慧", 2), ("哲学", 2),
                ("升华", 2), ("洞察", 2), ("道", 2), ("思想", 2), ("理念", 2),
                ("帝君", 1), ("最高", 1)
            ],
            # 乾宫·收敛（企业、投资、战略）
            6: [
                ("投资", 3), ("战略", 3), ("企业管理", 3), ("企业家", 3),
                ("管理", 2), ("秩序", 2), ("收敛", 2), ("企业", 2),
                ("决策", 2), ("老板", 1)
            ],
            # 震宫·生发（技术、开发、系统）
            3: [
                ("技术", 3), ("开发", 3), ("代码", 3), ("系统", 2),
                ("生发", 2), ("建设", 2), ("工程师", 2), ("编程", 2),
                ("Mem0", 3), ("GitHub", 3), ("Python", 3), ("AI", 2),
                ("stars", 1), ("开源", 2)
            ],
            # 兑宫·显现（内容、创作、发布）
            7: [
                ("内容", 3), ("创作", 3), ("发布", 3), ("表达", 2),
                ("显现", 2), ("自媒体", 2), ("百家号", 3), ("文章", 2),
                ("写作", 2), ("视频", 2)
            ],
            # 坎宫·起源（社群、销售、电商）
            1: [
                ("社群", 3), ("销售", 3), ("电商", 3), ("变现", 2),
                ("起源", 2), ("种子", 2), ("开始", 1), ("创意", 1),
                ("社群运营", 4)  # 组合词高权重
            ],
            # 巽宫·运化（平台、运营、趋势）
            4: [
                ("平台", 3), ("传播", 2), ("趋势", 2), ("运化", 2),
                ("推广", 2), ("分发", 2), ("运营", 1)  # 单独"运营"权重低
            ],
            # 艮宫·存储（存储、归档、知识库）
            8: [
                ("存储", 3), ("归档", 3), ("记忆", 2), ("资源", 2),
                ("沉淀", 2), ("知识库", 3), ("档案", 2)
            ],
            # 坤宫·承载（基础、规则、法律）
            2: [
                ("基础", 2), ("规则", 3), ("法律", 3), ("政策", 3),
                ("框架", 2), ("承载", 2), ("地基", 2)
            ],
            # 中宫·核心（核心、枢纽、中心）
            5: [
                ("核心", 2), ("枢纽", 2), ("中心", 2), ("关键", 1),
                ("重要", 1)
            ]
        }
        
        # 计算每个宫位的得分
        scores = {i: 0 for i in range(1, 10)}
        
        for palace, keywords in keywords_weighted.items():
            for keyword, weight in keywords:
                if keyword in text_lower:
                    scores[palace] += weight
        
        # 找到最高分的宫位
        max_score = max(scores.values())
        if max_score == 0:
            return 5  # 默认中宫
        
        # 返回最高分的宫位
        for palace, score in scores.items():
            if score == max_score:
                return palace
        
        return 5
    
    def get_generation_path(self) -> List[int]:
        """
        获取生成路径
        
        Returns:
            宫位数字列表，表示生成顺序
        """
        return self.GENERATION_ORDER
    
    def get_balance_number(self) -> int:
        """
        获取平衡数
        
        Returns:
            15（宇宙平衡数）
        """
        return 15
    
    def check_balance(self, palace_counts: Dict[int, int]) -> Tuple[bool, float]:
        """
        检查记忆分布是否平衡
        
        Args:
            palace_counts: 各宫位记忆数量
            
        Returns:
            (是否平衡, 平衡分数)
        """
        counts = [palace_counts.get(i, 0) for i in range(1, 10)]
        
        if sum(counts) == 0:
            return True, 1.0
        
        avg = sum(counts) / len(counts)
        if avg == 0:
            return True, 1.0
        
        # 计算标准差
        variance = sum((c - avg) ** 2 for c in counts) / len(counts)
        std_dev = variance ** 0.5
        
        # 归一化
        balance_score = 1 - (std_dev / avg) if avg > 0 else 1.0
        balance_score = max(0, min(1, balance_score))
        
        # 平衡阈值
        is_balanced = balance_score > 0.7
        
        return is_balanced, balance_score
    
    def get_three_yuan(self, palace_number: int) -> Optional[str]:
        """
        获取宫位所属的三垣
        
        Args:
            palace_number: 宫位数字
            
        Returns:
            三垣名称（天垣/地垣/人垣）
        """
        for yuan, config in self.THREE_YUAN.items():
            if palace_number in config["palaces"]:
                return yuan
        return None
    
    def get_element_cycle(self) -> List[str]:
        """
        获取五行相生循环
        
        Returns:
            五行列表，表示相生顺序
        """
        # 木 → 火 → 土 → 金 → 水 → 木
        return ["木", "火", "土", "金", "水"]
    
    def get_palace_element(self, palace_number: int) -> Optional[str]:
        """获取宫位五行"""
        info = self.get_palace(palace_number)
        return info.element if info else None
