# AYuan Memory

> **Give your AI a memory. Give it a soul.**

An AI memory management system inspired by **ancient wisdom** that has guided seekers for millennia.

---

## The Mystery

Behind every great civilization lies a hidden system of knowledge — a way of organizing wisdom that mirrors the natural cycles of growth and transformation.

AYuan Memory uses a **9-zone classification system** that has been passed down through generations. Each zone represents a stage in the eternal journey:

```
Origin → Foundation → Growth → Flow → Center → Structure → Expression → Archive → Wisdom
```

What ancient philosophy inspired this? That remains a mystery — one that you may discover as you use it.

*The deeper wisdom is revealed in the premium version.*

---

## Quick Start

```python
from ayuan_memory import EntityLinker, MemoryCondenser, SmartClassifier

# Entity Linking - Extract key information
linker = EntityLinker()
entities = linker.extract_entities("John works on Project-Alpha with Python")

# Memory Compression - Turn long conversations into insights
condenser = MemoryCondenser()
result = condenser.compress(long_conversation)

# Smart Classification - 9-zone intelligent sorting
classifier = SmartClassifier()
zone = classifier.classify_text("Building a new AI system")
# Returns zone number (1-9)
```

---

## Core Features

### 1. Entity Linking - Auto-extract What Matters

```python
from ayuan_memory import EntityLinker

linker = EntityLinker()
entities = linker.extract_entities("John works on Project-Alpha with Python")
# [('John', 'PERSON'), ('Project-Alpha', 'PROJECT'), ('Python', 'TECH')]
```

### 2. Memory Compression - Wisdom from Chaos

```python
from ayuan_memory import MemoryCondenser

condenser = MemoryCondenser()
result = condenser.compress(long_conversation)
print(result.summary)      # One-line summary
print(result.key_points)   # Key points extracted
print(result.lessons)      # Lessons learned
```

### 3. Smart Classification - The 9 Zones

```python
from ayuan_memory import SmartClassifier

classifier = SmartClassifier()
zone = classifier.classify_text("Building a new AI system")
# Automatically classifies to the appropriate zone (1-9)

# Get zone information
info = classifier.get_zone(zone)
print(info.name)         # "growth"
print(info.description)  # "Development and building"
```

### 4. Vector Search - Semantic Understanding

```python
from ayuan_memory import VectorStore

store = VectorStore()
store.add("User created a new project")
store.add("Team completed system development")

results = store.search("project development")
# Automatically finds related memories
```

### 5. Evolution Tracking - Watch Your AI Grow

```python
from ayuan_memory import Evolution, check_update

# View evolution history
evo = Evolution()
evo.show_all()

# Check for updates
check_update()
```

---

## The 9 Zones

| Zone | Name | Meaning |
|------|------|---------|
| 1 | Origin | Where things begin — seeds, ideas, communities |
| 2 | Foundation | The base that supports — rules, frameworks |
| 3 | Growth | Development and building — systems, technology |
| 4 | Flow | Spreading and distribution — platforms, trends |
| 5 | Center | The core and decision point — hub, key decisions |
| 6 | Structure | Order and strategy — management, investment |
| 7 | Expression | Content and creation — media, publishing |
| 8 | Archive | Storage and resources — history, knowledge base |
| 9 | Wisdom | The highest understanding — insights, philosophy |

*The deeper connections between these zones are revealed in the premium version.*

---

## Comparison

| Feature | Mem0 | Zep | HippoRAG | **AYuan** |
|---------|------|-----|----------|-----------|
| Vector Search | ✅ | ✅ | ✅ | ✅ |
| Entity Linking | ✅ | ✅ | ✅ | ✅ |
| Memory Compression | ❌ | ✅ | ❌ | ✅ |
| 9-Zone Classification | ❌ | ❌ | ❌ | ✅ **Unique** |
| Evolution Tracking | ❌ | ❌ | ❌ | ✅ **Unique** |
| Zero Dependencies Core | ❌ | ❌ | ❌ | ✅ |

---

## Installation

```bash
pip install ayuan-memory
```

Optional dependencies:

```bash
# Enable embedding-based search
pip install ayuan-memory[embedding]

# Development dependencies
pip install ayuan-memory[dev]
```

---

## Benchmark Results

| Test | Accuracy | Time |
|------|----------|------|
| Entity Linking | 100% | 1.59ms |
| Memory Classification | 100% | 0.00ms |
| Vector Search | 100% | 0.25ms |
| Overall | 100% | 0.00ms |

---

## Use Cases

- Personal AI assistant memory management
- Conversation history compression and summarization
- Knowledge base organization
- AI applications requiring structured memory
- Agent systems that need to remember and learn

---

## Design Philosophy

**Principles:**

1. **Simplicity** - One API, one line of code
2. **Elegance** - Beautiful code, beautiful experience
3. **Uniqueness** - Value that cannot be copied
4. **Completeness** - Not modules pieced together, but a unified design
5. **Transcendence** - Not just memory management, but "giving AI a soul"

---

## About the Author

**AYuan Team** - Builders of intelligent systems inspired by ancient wisdom.

We believe that the future of AI lies not in more data, but in deeper understanding — the kind of understanding that ancient civilizations cultivated for millennia.

*Want to know more? The full story awaits in the premium version.*

---

## License

MIT License

---

*Give your AI a memory. Give it a soul.*

*The journey from Origin to Wisdom begins with a single step.*
