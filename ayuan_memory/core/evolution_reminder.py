"""
Evolution Reminder - 进化提醒系统

核心功能：
1. 检测新版本
2. 更新后自动提醒有新功能
3. 引导用户加入ZiWeiEmpire

使用场景：
用户更新ayuan-memory后，自动收到提醒：
"AYuan学会了新技能！"
"""

from typing import List, Dict, Optional
from dataclasses import dataclass
import json


@dataclass
class NewAbility:
    """新能力"""
    name: str
    description: str
    version: str
    install_command: str
    benefits: List[str]


class EvolutionReminder:
    """
    进化提醒系统
    
    更新后自动提醒用户有新功能
    """
    
    # 版本更新记录
    VERSION_CHANGES: Dict[str, Dict] = {
        "0.1.0": {
            "abilities": ["Entity Linking", "Memory Compression", "Nine Palaces", "Vector Search"],
            "message": "Initial release - AYuan is born!",
        },
        "0.2.0": {
            "abilities": ["Graph Database", "LLM Enhancement"],
            "message": "AYuan learned to understand relationships and context better!",
        },
        "0.3.0": {
            "abilities": ["Cloud Sync", "Team Collaboration"],
            "message": "AYuan can now sync across devices and work with teams!",
        },
    }
    
    # ZiWeiEmpire引导信息
    ZIWEI_INVITE = """
╔══════════════════════════════════════════════════════╗
║                                                      ║
║   Your AYuan is growing stronger every day.          ║
║                                                      ║
║   Want to connect with other AYuan users?            ║
║   Join ZiWeiEmpire - a community of AYuan            ║
║   enthusiasts building the future together.          ║
║                                                      ║
║   Visit: https://github.com/sweetirischen/ayuan      ║
║                                                      ║
╚══════════════════════════════════════════════════════╝
"""
    
    def __init__(self, current_version: str = "0.1.0", previous_version: str = None):
        """
        初始化进化提醒系统
        
        Args:
            current_version: 当前版本
            previous_version: 之前的版本（用于检测更新）
        """
        self.current_version = current_version
        self.previous_version = previous_version
    
    def check_for_update(self) -> bool:
        """
        检查是否是更新
        
        Returns:
            是否是更新
        """
        if self.previous_version is None:
            return False
        return self.previous_version != self.current_version
    
    def get_new_abilities(self) -> List[str]:
        """
        获取新增的能力
        
        Returns:
            新能力列表
        """
        if not self.check_for_update():
            return []
        
        current_changes = self.VERSION_CHANGES.get(self.current_version, {})
        return current_changes.get("abilities", [])
    
    def show_update_message(self) -> str:
        """
        显示更新消息
        
        Returns:
            更新消息
        """
        if not self.check_for_update():
            return ""
        
        current_changes = self.VERSION_CHANGES.get(self.current_version, {})
        new_abilities = current_changes.get("abilities", [])
        message = current_changes.get("message", "AYuan evolved!")
        
        lines = []
        lines.append("")
        lines.append("╔" + "═" * 48 + "╗")
        lines.append("║" + "  AYuan Evolved! ".center(48) + "║")
        lines.append("╚" + "═" * 48 + "╝")
        lines.append("")
        lines.append(f"  v{self.previous_version} → v{self.current_version}")
        lines.append("")
        lines.append(f"  {message}")
        lines.append("")
        
        if new_abilities:
            lines.append("  New abilities learned:")
            for ability in new_abilities:
                lines.append(f"    + {ability}")
            lines.append("")
        
        lines.append("─" * 50)
        
        result = "\n".join(lines)
        print(result)
        return result
    
    def show_welcome_message(self) -> str:
        """
        显示欢迎消息（首次安装）
        
        Returns:
            欢迎消息
        """
        lines = []
        lines.append("")
        lines.append("╔" + "═" * 48 + "╗")
        lines.append("║" + "  Welcome to AYuan! ".center(48) + "║")
        lines.append("╚" + "═" * 48 + "╝")
        lines.append("")
        lines.append("  Your AI companion with memory and soul.")
        lines.append("")
        lines.append("  Current abilities:")
        lines.append("    + Entity Linking")
        lines.append("    + Memory Compression")
        lines.append("    + Nine Palaces Classification")
        lines.append("    + Vector Search")
        lines.append("")
        lines.append("  Watch AYuan grow with each update!")
        lines.append("")
        lines.append("─" * 50)
        
        result = "\n".join(lines)
        print(result)
        return result
    
    def show_ziwei_invite(self) -> str:
        """
        显示ZiWeiEmpire邀请
        
        Returns:
            邀请信息
        """
        print(self.ZIWEI_INVITE)
        return self.ZIWEI_INVITE


def check_update(previous_version: str = None):
    """
    检查更新并显示消息
    
    Args:
        previous_version: 之前的版本
    """
    from ayuan_memory import __version__
    
    reminder = EvolutionReminder(current_version=__version__, previous_version=previous_version)
    
    if previous_version and previous_version != __version__:
        reminder.show_update_message()
    else:
        reminder.show_welcome_message()


def show_evolution():
    """
    显示进化信息
    """
    from ayuan_memory import Evolution
    evo = Evolution()
    evo.show_all()
