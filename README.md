# 阿垣记忆系统 (Ayuan Memory)

**AI Agent Memory System with Chinese Philosophy**

一个融合九宫哲学的AI记忆管理系统。

[English](#english) | [中文](#中文)

---

## 中文

### 为什么选择阿垣记忆系统？

**独特的九宫分类系统** - 基于洛书九宫的记忆组织方式，让记忆有层次、有结构

**不是搜索引擎，是记忆宫殿** - 像古人一样用空间组织记忆

**轻量级，零依赖** - 纯Python实现，无需向量数据库

**可扩展** - 支持自定义存储后端

### 安装

```bash
pip install ayuan-memory
```

### 快速开始

```python
from ayuan_memory import EntityLinker, MemoryCondenser, MemoryPalace

# 1. 实体链接 - 提取和链接实体
linker = EntityLinker()
text = "帝君让阿垣学习Mem0和Hermes的技术"
entities = linker.extract_entities(text)
print(entities)  # [('帝君', 'PERSON'), ('阿垣', 'PERSON'), ('Mem0', 'TECH'), ...]

# 2. 记忆压缩 - 长对话压缩为精华
condenser = MemoryCondenser()
long_text = "很长的对话内容..."
compressed = condenser.compress(long_text)
print(compressed.summary)  # 一句话总结
print(compressed.key_points)  # 关键点列表

# 3. 记忆宫殿 - 九宫分类存储
palace = MemoryPalace()
memory = {
    "content": "重要的经验教训",
    "type": "wisdom",
    "tags": ["重要", "教训"]
}
palace.add_memory(memory)  # 自动分类到对应宫位
```

### 九宫分类系统

基于洛书九宫的记忆组织方式：

```
  4(巽)  9(离)  2(坤)
  3(震)  5(中)  7(兑)
  8(艮)  1(坎)  6(乾)
```

| 宫位 | 五行 | 含义 | 适合存储 |
|------|------|------|----------|
| 坎宫(1) | 水 | 起源·种子 | 创意、想法、开始 |
| 坤宫(2) | 土 | 承载·地基 | 规则、框架、基础 |
| 震宫(3) | 木 | 生发·成长 | 技术、系统、开发 |
| 巽宫(4) | 木 | 运化·传播 | 平台、运营、推广 |
| 中宫(5) | 土 | 枢纽·核心 | 决策、关键、重要 |
| 乾宫(6) | 金 | 收敛·秩序 | 战略、投资、管理 |
| 兑宫(7) | 金 | 显现·表达 | 内容、创作、发布 |
| 艮宫(8) | 土 | 存储·归档 | 知识库、资源、沉淀 |
| 离宫(9) | 火 | 升华·智慧 | 洞察、哲学、道 |

### 核心特性

**实体链接**
- 自动提取人名、项目、技术、概念
- 建立实体与记忆的关联
- 支持实体搜索和查询

**记忆压缩**
- 长对话压缩为一句话总结
- 提取关键点、决策、教训
- 保留核心信息

**九宫分类**
- 基于洛书九宫的自动分类
- 三垣架构（天垣、地垣、人垣）
- 记忆平衡度评估

### 与其他记忆系统的对比

| 特性 | Mem0 | M-Flow | 阿垣记忆 |
|------|------|--------|----------|
| 向量数据库 | ✅ | ✅ | ❌ |
| 图数据库 | ✅ | ✅ | ❌ |
| 九宫分类 | ❌ | ❌ | ✅ |
| 零依赖 | ❌ | ❌ | ✅ |
| 中文优化 | ❌ | ❌ | ✅ |
| 哲学框架 | ❌ | ❌ | ✅ |

### 适用场景

- 个人AI助手的记忆管理
- 对话历史压缩和总结
- 知识库分类组织
- 中文语境的AI应用

---

## English

### Why Ayuan Memory?

**Unique Nine Palaces Classification** - Memory organization based on Luoshu (洛书), an ancient Chinese philosophy

**Not a Search Engine, a Memory Palace** - Organize memories spatially like ancient scholars

**Lightweight, Zero Dependencies** - Pure Python, no vector database required

**Extensible** - Custom storage backends supported

### Installation

```bash
pip install ayuan-memory
```

### Quick Start

```python
from ayuan_memory import EntityLinker, MemoryCondenser, MemoryPalace

# Entity Linking
linker = EntityLinker()
entities = linker.extract_entities("John works on Project Alpha with Python")

# Memory Compression
condenser = MemoryCondenser()
compressed = condenser.compress(long_conversation)

# Memory Palace
palace = MemoryPalace()
palace.add_memory({"content": "Important lesson", "type": "wisdom"})
```

### License

MIT License

---

## 致谢

本项目融合了以下开源项目的思想：
- Mem0 - 实体链接
- OpenHands - 记忆压缩
- HippoRAG - 类脑记忆

以及中国古典哲学：
- 洛书九宫
- 五行学说
- 三垣架构

---

**Made with ❤️ by 阿垣 (Ayuan) & 帝君**
