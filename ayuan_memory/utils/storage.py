"""
存储层模块 - 记忆的持久化存储

支持多种存储后端：
- 文件系统（默认）
- SQLite（可选）
- 内存（测试用）
"""

import json
import os
from typing import Dict, List, Optional, Any
from datetime import datetime
from pathlib import Path
from abc import ABC, abstractmethod


class StorageBackend(ABC):
    """存储后端抽象类"""
    
    @abstractmethod
    def save(self, key: str, data: Dict) -> bool:
        """保存数据"""
        pass
    
    @abstractmethod
    def load(self, key: str) -> Optional[Dict]:
        """加载数据"""
        pass
    
    @abstractmethod
    def delete(self, key: str) -> bool:
        """删除数据"""
        pass
    
    @abstractmethod
    def list_keys(self) -> List[str]:
        """列出所有键"""
        pass
    
    @abstractmethod
    def exists(self, key: str) -> bool:
        """检查是否存在"""
        pass


class FileStorage(StorageBackend):
    """文件存储后端"""
    
    def __init__(self, base_path: str = "./ayuan_memory"):
        """
        初始化文件存储
        
        Args:
            base_path: 存储根目录
        """
        self.base_path = Path(base_path)
        self.base_path.mkdir(parents=True, exist_ok=True)
    
    def _get_file_path(self, key: str) -> Path:
        """获取文件路径"""
        return self.base_path / f"{key}.json"
    
    def save(self, key: str, data: Dict) -> bool:
        """保存数据到文件"""
        try:
            file_path = self._get_file_path(key)
            data["_saved_at"] = datetime.now().isoformat()
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(data, f, ensure_ascii=False, indent=2)
            return True
        except Exception as e:
            print(f"保存失败: {e}")
            return False
    
    def load(self, key: str) -> Optional[Dict]:
        """从文件加载数据"""
        try:
            file_path = self._get_file_path(key)
            if file_path.exists():
                with open(file_path, "r", encoding="utf-8") as f:
                    return json.load(f)
            return None
        except Exception as e:
            print(f"加载失败: {e}")
            return None
    
    def delete(self, key: str) -> bool:
        """删除文件"""
        try:
            file_path = self._get_file_path(key)
            if file_path.exists():
                file_path.unlink()
            return True
        except Exception as e:
            print(f"删除失败: {e}")
            return False
    
    def list_keys(self) -> List[str]:
        """列出所有键"""
        keys = []
        for file_path in self.base_path.glob("*.json"):
            keys.append(file_path.stem)
        return keys
    
    def exists(self, key: str) -> bool:
        """检查文件是否存在"""
        return self._get_file_path(key).exists()


class MemoryStorage(StorageBackend):
    """内存存储后端（测试用）"""
    
    def __init__(self):
        """初始化内存存储"""
        self._data: Dict[str, Dict] = {}
    
    def save(self, key: str, data: Dict) -> bool:
        """保存到内存"""
        data["_saved_at"] = datetime.now().isoformat()
        self._data[key] = data
        return True
    
    def load(self, key: str) -> Optional[Dict]:
        """从内存加载"""
        return self._data.get(key)
    
    def delete(self, key: str) -> bool:
        """从内存删除"""
        if key in self._data:
            del self._data[key]
        return True
    
    def list_keys(self) -> List[str]:
        """列出所有键"""
        return list(self._data.keys())
    
    def exists(self, key: str) -> bool:
        """检查是否存在"""
        return key in self._data


class StorageManager:
    """存储管理器"""
    
    def __init__(self, backend: Optional[StorageBackend] = None, base_path: str = "./ayuan_memory"):
        """
        初始化存储管理器
        
        Args:
            backend: 存储后端，默认使用文件存储
            base_path: 文件存储根目录
        """
        self.backend = backend or FileStorage(base_path)
    
    def save_memory(self, memory_id: str, content: Dict) -> bool:
        """
        保存记忆
        
        Args:
            memory_id: 记忆ID
            content: 记忆内容
            
        Returns:
            是否成功
        """
        return self.backend.save(memory_id, content)
    
    def load_memory(self, memory_id: str) -> Optional[Dict]:
        """
        加载记忆
        
        Args:
            memory_id: 记忆ID
            
        Returns:
            记忆内容
        """
        return self.backend.load(memory_id)
    
    def delete_memory(self, memory_id: str) -> bool:
        """
        删除记忆
        
        Args:
            memory_id: 记忆ID
            
        Returns:
            是否成功
        """
        return self.backend.delete(memory_id)
    
    def list_memories(self) -> List[str]:
        """
        列出所有记忆ID
        
        Returns:
            记忆ID列表
        """
        return self.backend.list_keys()
    
    def memory_exists(self, memory_id: str) -> bool:
        """
        检查记忆是否存在
        
        Args:
            memory_id: 记忆ID
            
        Returns:
            是否存在
        """
        return self.backend.exists(memory_id)
    
    def search_memories(self, query: str) -> List[Dict]:
        """
        搜索记忆
        
        Args:
            query: 搜索关键词
            
        Returns:
            匹配的记忆列表
        """
        results = []
        query_lower = query.lower()
        
        for memory_id in self.list_memories():
            memory = self.load_memory(memory_id)
            if memory:
                # 搜索所有字段
                content_str = json.dumps(memory, ensure_ascii=False).lower()
                if query_lower in content_str:
                    results.append({
                        "id": memory_id,
                        "content": memory
                    })
        
        return results
