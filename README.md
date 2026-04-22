# Ayuan Memory

> **让AI有记忆，有灵魂。**

一个融合洛书九宫哲学的AI记忆管理系统。

---

## 一行代码，开始使用

```python
from ayuan_memory import Memory

memory = Memory()
memory.remember("用户创建了新项目", palace="离宫")
results = memory.recall("项目")  # 语义搜索
```

---

## 为什么选择Ayuan？

| 别的记忆系统 | Ayuan记忆系统 |
|-------------|-------------|
| 存储数据 | 存储智慧 |
| 搜索引擎 | 记忆宫殿 |
| 扁平列表 | 九宫分类 |
| 冷冰冰 | 有灵魂 |

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

### 4. 九宫分类 - 古代智慧，现代应用

```python
from ayuan_memory import NinePalaces

palaces = NinePalaces()
palace = palaces.classify_text("技术开发项目")
# 返回：3 (震宫·木·生发)
```

---

## 九宫分类系统

基于洛书九宫的记忆组织方式：

```
  4(巽)  9(离)  2(坤)
  3(震)  5(中)  7(兑)
  8(艮)  1(坎)  6(乾)
```

每行、每列、每对角线之和 = **15**（宇宙平衡数）

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

---

## 与其他记忆系统对比

| 特性 | Mem0 | Zep | HippoRAG | **Ayuan** |
|------|------|-----|----------|----------|
| 向量搜索 | ✅ | ✅ | ✅ | ✅ |
| 实体链接 | ✅ | ✅ | ✅ | ✅ |
| 记忆压缩 | ❌ | ✅ | ❌ | ✅ |
| 九宫分类 | ❌ | ❌ | ❌ | ✅ |
| 中文优化 | ❌ | ❌ | ❌ | ✅ |
| 哲学框架 | ❌ | ❌ | ❌ | ✅ |
| 零依赖核心 | ❌ | ❌ | ❌ | ✅ |

**Ayuan独有的价值：九宫哲学框架**

这不是一个技术特性，是一种思维方式。让AI的记忆不再是扁平的数据，而是有层次、有结构、有灵魂的智慧。

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
| 九宫分类 | 100% | 0.00ms |
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
3. **独特** - 九宫哲学是独有价值，别人复制不了
4. **完整** - 不是拼凑模块，是整体设计
5. **升华** - 不只是记忆管理，是"让AI有灵魂"

---

## 致谢

本项目融合了以下开源项目的思想：
- Mem0 - 实体链接
- OpenHands - 记忆压缩
- HippoRAG - 类脑记忆
- Zep - 记忆层设计

以及中国古典哲学：
- 洛书九宫
- 五行学说
- 三垣架构

---

## License

MIT License

---

*让AI有记忆，有灵魂。*
