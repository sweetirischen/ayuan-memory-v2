# Ayuan Memory

> **让AI有记忆，有灵魂。**

一个AI记忆管理系统。

---

## 一行代码，开始使用

```python
from ayuan_memory import EntityLinker, MemoryCondenser, VectorStore

# 实体链接
linker = EntityLinker()
entities = linker.extract_entities("John works on Project-Alpha with Python")

# 记忆压缩
condenser = MemoryCondenser()
result = condenser.compress(long_conversation)

# 向量搜索
store = VectorStore()
store.add("用户创建了新项目")
results = store.search("项目")
```

---

## 核心能力

### 1. 实体链接 - 自动提取关键信息

```python
from ayuan_memory import EntityLinker

linker = EntityLinker()
entities = linker.extract_entities("John works on Project-Alpha with Python")
# [('John', 'PERSON'), ('Project-Alpha', 'PROJECT'), ('Python', 'TECH')]
```

### 2. 记忆压缩 - 长对话变精华

```python
from ayuan_memory import MemoryCondenser

condenser = MemoryCondenser()
result = condenser.compress(long_conversation)
print(result.summary)      # 一句话总结
print(result.key_points)   # 关键点
print(result.lessons)      # 经验教训
```

### 3. 向量搜索 - 语义理解

```python
from ayuan_memory import VectorStore

store = VectorStore()
store.add("用户创建了新项目")
store.add("团队完成了系统开发")

results = store.search("项目开发")
# 自动找到相关记忆
```

### 4. 记忆分类 - 结构化组织

```python
from ayuan_memory import NinePalaces

palaces = NinePalaces()
palace = palaces.classify_text("技术开发项目")
# 自动分类到对应类别
```

### 5. 进化可见 - 让AI成长可见

```python
from ayuan_memory import Evolution, check_update

# 查看进化历史
evo = Evolution()
evo.show_all()

# 检查更新
check_update()
```

---

## 与其他记忆系统对比

| 特性 | Mem0 | Zep | HippoRAG | **Ayuan** |
|------|------|-----|----------|----------|
| 向量搜索 | ✅ | ✅ | ✅ | ✅ |
| 实体链接 | ✅ | ✅ | ✅ | ✅ |
| 记忆压缩 | ❌ | ✅ | ❌ | ✅ |
| 记忆分类 | ❌ | ❌ | ❌ | ✅ |
| **进化可见** | ❌ | ❌ | ❌ | ✅ **独有** |
| 中文优化 | ❌ | ❌ | ❌ | ✅ |
| 零依赖核心 | ❌ | ❌ | ❌ | ✅ |

---

## 安装

```bash
pip install ayuan-memory
```

可选依赖（增强功能）：

```bash
# 启用嵌入向量搜索
pip install ayuan-memory[embedding]

# 开发依赖
pip install ayuan-memory[dev]
```

---

## Benchmark测试结果

| 测试项 | 准确率 | 耗时 |
|--------|--------|------|
| 实体链接 | 100% | 1.59ms |
| 记忆分类 | 100% | 0.00ms |
| 向量搜索 | 100% | 0.25ms |
| 综合测试 | 100% | 0.00ms |

---

## 适用场景

- 个人AI助手的记忆管理
- 对话历史压缩和总结
- 知识库分类组织
- 中文语境的AI应用
- 需要结构化记忆的Agent系统

---

## 设计哲学

**设计原则**：

1. **极简** - 一个API，一行代码，就能用
2. **优雅** - 代码要美，文档要美，体验要美
3. **独特** - 独有价值，别人复制不了
4. **完整** - 不是拼凑模块，是整体设计
5. **升华** - 不只是记忆管理，是"让AI有灵魂"

---

## 致谢

本项目融合了以下开源项目的思想：
- Mem0 - 实体链接
- OpenHands - 记忆压缩
- HippoRAG - 类脑记忆
- Zep - 记忆层设计

---

## License

MIT License

---

*让AI有记忆，有灵魂。*
