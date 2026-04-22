"""
向量存储模块 - 支持语义搜索

可选依赖：
- sentence-transformers: 用于生成嵌入向量
- numpy: 用于向量计算

设计原则：
- 核心功能零依赖
- 向量搜索为可选增强
- 自动检测依赖可用性
"""

import json
import math
from pathlib import Path
from typing import List, Dict, Any, Optional, Tuple

# 可选依赖检测
try:
    import numpy as np
    HAS_NUMPY = True
except ImportError:
    HAS_NUMPY = False
    np = None

try:
    from sentence_transformers import SentenceTransformer
    HAS_SENTENCE_TRANSFORMERS = True
except ImportError:
    HAS_SENTENCE_TRANSFORMERS = False
    SentenceTransformer = None


class VectorStore:
    """
    向量存储，支持语义搜索
    
    使用方式：
    1. 无依赖模式：使用TF-IDF相似度
    2. 有依赖模式：使用sentence-transformers嵌入
    """
    
    def __init__(
        self,
        storage_path: Optional[str] = None,
        model_name: str = "all-MiniLM-L6-v2",
        use_embedding: bool = True
    ):
        """
        初始化向量存储
        
        Args:
            storage_path: 存储路径
            model_name: 嵌入模型名称
            use_embedding: 是否使用嵌入向量（需要sentence-transformers）
        """
        self.storage_path = Path(storage_path) if storage_path else None
        self.model_name = model_name
        self.use_embedding = use_embedding and HAS_SENTENCE_TRANSFORMERS
        
        # 嵌入模型
        self.model = None
        if self.use_embedding:
            try:
                self.model = SentenceTransformer(model_name)
            except Exception as e:
                print(f"Warning: Failed to load model {model_name}: {e}")
                self.use_embedding = False
        
        # 存储
        self.documents: List[Dict[str, Any]] = []
        self.vectors: List[List[float]] = []
        self.idf_cache: Dict[str, float] = {}  # TF-IDF缓存
        
        # 加载已有数据
        if self.storage_path and self.storage_path.exists():
            self._load()
    
    def add(
        self,
        text: str,
        metadata: Optional[Dict[str, Any]] = None,
        doc_id: Optional[str] = None
    ) -> str:
        """
        添加文档
        
        Args:
            text: 文档文本
            metadata: 元数据
            doc_id: 文档ID（可选）
            
        Returns:
            文档ID
        """
        import uuid
        
        doc_id = doc_id or str(uuid.uuid4())
        metadata = metadata or {}
        
        doc = {
            "id": doc_id,
            "text": text,
            "metadata": metadata
        }
        
        # 生成向量
        if self.use_embedding and self.model:
            vector = self.model.encode(text).tolist()
        else:
            vector = self._tfidf_vectorize(text)
        
        self.documents.append(doc)
        self.vectors.append(vector)
        
        # 更新IDF缓存
        self._update_idf(text)
        
        # 保存
        if self.storage_path:
            self._save()
        
        return doc_id
    
    def search(
        self,
        query: str,
        top_k: int = 5,
        filter_func: Optional[callable] = None
    ) -> List[Dict[str, Any]]:
        """
        语义搜索
        
        Args:
            query: 查询文本
            top_k: 返回数量
            filter_func: 过滤函数
            
        Returns:
            搜索结果列表
        """
        if not self.documents:
            return []
        
        # 生成查询向量
        if self.use_embedding and self.model:
            query_vector = self.model.encode(query).tolist()
        else:
            query_vector = self._tfidf_vectorize(query)
        
        # 计算相似度
        similarities = []
        for i, doc_vector in enumerate(self.vectors):
            sim = self._cosine_similarity(query_vector, doc_vector)
            doc = self.documents[i]
            
            # 应用过滤
            if filter_func and not filter_func(doc):
                continue
            
            similarities.append((sim, doc))
        
        # 排序
        similarities.sort(key=lambda x: x[0], reverse=True)
        
        # 返回top_k
        results = []
        for sim, doc in similarities[:top_k]:
            result = doc.copy()
            result["score"] = sim
            results.append(result)
        
        return results
    
    def delete(self, doc_id: str) -> bool:
        """
        删除文档
        
        Args:
            doc_id: 文档ID
            
        Returns:
            是否成功
        """
        for i, doc in enumerate(self.documents):
            if doc["id"] == doc_id:
                self.documents.pop(i)
                self.vectors.pop(i)
                if self.storage_path:
                    self._save()
                return True
        return False
    
    def clear(self):
        """清空所有文档"""
        self.documents = []
        self.vectors = []
        self.idf_cache = {}
        if self.storage_path:
            self._save()
    
    def _tfidf_vectorize(self, text: str) -> List[float]:
        """
        TF-IDF向量化（无依赖模式）
        
        简化实现：使用词频和逆文档频率
        """
        # 分词（简单按空格和标点）
        words = self._tokenize(text)
        
        # 计算词频
        tf = {}
        for word in words:
            tf[word] = tf.get(word, 0) + 1
        
        # 归一化
        total = len(words) if words else 1
        for word in tf:
            tf[word] = tf[word] / total
        
        # 转换为向量（使用IDF加权）
        # 向量维度 = 所有出现过的词
        all_words = set(self.idf_cache.keys()) | set(tf.keys())
        vector = []
        for word in all_words:
            tf_val = tf.get(word, 0)
            idf_val = self.idf_cache.get(word, 1.0)
            vector.append(tf_val * idf_val)
        
        # 归一化向量
        norm = math.sqrt(sum(v * v for v in vector)) if vector else 1
        vector = [v / norm for v in vector]
        
        return vector
    
    def _tokenize(self, text: str) -> List[str]:
        """简单分词"""
        import re
        # 移除标点，转小写，分词
        text = text.lower()
        text = re.sub(r'[^\w\s]', ' ', text)
        words = text.split()
        # 过滤停用词（简化版）
        stop_words = {'the', 'a', 'an', 'is', 'are', 'was', 'were', 'be', 'been', 
                      'being', 'have', 'has', 'had', 'do', 'does', 'did', 'will',
                      'would', 'could', 'should', 'may', 'might', 'must', 'shall',
                      'can', 'need', 'dare', 'ought', 'used', 'to', 'of', 'in',
                      'for', 'on', 'with', 'at', 'by', 'from', 'as', 'into',
                      'through', 'during', 'before', 'after', 'above', 'below',
                      'between', 'under', 'again', 'further', 'then', 'once',
                      'here', 'there', 'when', 'where', 'why', 'how', 'all',
                      'each', 'few', 'more', 'most', 'other', 'some', 'such',
                      'no', 'nor', 'not', 'only', 'own', 'same', 'so', 'than',
                      'too', 'very', 'just', 'and', 'but', 'if', 'or', 'because',
                      'until', 'while', 'about', 'against', 'i', 'me', 'my',
                      'myself', 'we', 'our', 'ours', 'ourselves', 'you', 'your',
                      'yours', 'yourself', 'yourselves', 'he', 'him', 'his',
                      'himself', 'she', 'her', 'hers', 'herself', 'it', 'its',
                      'itself', 'they', 'them', 'their', 'theirs', 'themselves',
                      'what', 'which', 'who', 'whom', 'this', 'that', 'these',
                      'those', 'am'}
        return [w for w in words if w not in stop_words and len(w) > 1]
    
    def _update_idf(self, text: str):
        """更新IDF缓存"""
        words = set(self._tokenize(text))
        for word in words:
            # IDF = log(N / df)，这里简化处理
            self.idf_cache[word] = self.idf_cache.get(word, 0) + 1
    
    def _cosine_similarity(self, vec1: List[float], vec2: List[float]) -> float:
        """
        计算余弦相似度
        
        处理不同长度的向量（对齐维度）
        """
        if not vec1 or not vec2:
            return 0.0
        
        # 对齐维度
        max_len = max(len(vec1), len(vec2))
        v1 = vec1 + [0] * (max_len - len(vec1))
        v2 = vec2 + [0] * (max_len - len(vec2))
        
        # 使用numpy（如果可用）
        if HAS_NUMPY:
            v1 = np.array(v1)
            v2 = np.array(v2)
            dot = np.dot(v1, v2)
            norm1 = np.linalg.norm(v1)
            norm2 = np.linalg.norm(v2)
            if norm1 == 0 or norm2 == 0:
                return 0.0
            return float(dot / (norm1 * norm2))
        
        # 纯Python实现
        dot = sum(a * b for a, b in zip(v1, v2))
        norm1 = math.sqrt(sum(a * a for a in v1))
        norm2 = math.sqrt(sum(b * b for b in v2))
        
        if norm1 == 0 or norm2 == 0:
            return 0.0
        
        return dot / (norm1 * norm2)
    
    def _save(self):
        """保存到文件"""
        if not self.storage_path:
            return
        
        self.storage_path.parent.mkdir(parents=True, exist_ok=True)
        
        data = {
            "documents": self.documents,
            "vectors": self.vectors,
            "idf_cache": self.idf_cache,
            "model_name": self.model_name,
            "use_embedding": self.use_embedding
        }
        
        with open(self.storage_path, "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    
    def _load(self):
        """从文件加载"""
        if not self.storage_path or not self.storage_path.exists():
            return
        
        try:
            with open(self.storage_path, "r", encoding="utf-8") as f:
                data = json.load(f)
            
            self.documents = data.get("documents", [])
            self.vectors = data.get("vectors", [])
            self.idf_cache = data.get("idf_cache", {})
        except Exception as e:
            print(f"Warning: Failed to load vector store: {e}")
    
    def __len__(self) -> int:
        return len(self.documents)
    
    def __repr__(self) -> str:
        mode = "embedding" if self.use_embedding else "tfidf"
        return f"VectorStore(docs={len(self)}, mode={mode})"


class SemanticMemory:
    """
    语义记忆系统
    
    结合向量搜索和九宫分类
    """
    
    def __init__(
        self,
        storage_path: Optional[str] = None,
        use_embedding: bool = True
    ):
        """
        初始化语义记忆系统
        
        Args:
            storage_path: 存储路径
            use_embedding: 是否使用嵌入向量
        """
        self.vector_store = VectorStore(
            storage_path=storage_path,
            use_embedding=use_embedding
        )
    
    def remember(
        self,
        text: str,
        palace: Optional[str] = None,
        entities: Optional[List[str]] = None,
        metadata: Optional[Dict[str, Any]] = None
    ) -> str:
        """
        记忆内容
        
        Args:
            text: 文本内容
            palace: 归属宫位
            entities: 相关实体
            metadata: 其他元数据
            
        Returns:
            记忆ID
        """
        meta = metadata or {}
        if palace:
            meta["palace"] = palace
        if entities:
            meta["entities"] = entities
        
        return self.vector_store.add(text, metadata=meta)
    
    def recall(
        self,
        query: str,
        top_k: int = 5,
        palace: Optional[str] = None
    ) -> List[Dict[str, Any]]:
        """
        回忆内容
        
        Args:
            query: 查询文本
            top_k: 返回数量
            palace: 限定宫位
            
        Returns:
            记忆列表
        """
        def filter_func(doc):
            if palace and doc.get("metadata", {}).get("palace") != palace:
                return False
            return True
        
        return self.vector_store.search(query, top_k=top_k, filter_func=filter_func)
    
    def forget(self, memory_id: str) -> bool:
        """遗忘记忆"""
        return self.vector_store.delete(memory_id)
    
    def clear_all(self):
        """清空所有记忆"""
        self.vector_store.clear()
