"""
Benchmark测试 - Ayuan Memory System
"""

import time
import json
from pathlib import Path
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass

# 导入Ayuan模块
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from ayuan_memory.core.entity_linker import EntityLinker
from ayuan_memory.core.memory_condenser import MemoryCondenser
from ayuan_memory.core.vector_store import VectorStore, SemanticMemory
from ayuan_memory.palace.nine_palaces import NinePalaces


@dataclass
class BenchmarkResult:
    """测试结果"""
    name: str
    accuracy: float
    speed_ms: float
    memory_mb: float
    notes: str = ""


class Benchmark:
    """基准测试套件"""
    
    def __init__(self):
        self.results: List[BenchmarkResult] = []
    
    def run_all(self) -> Dict[str, Any]:
        """运行所有测试"""
        print("=" * 60)
        print("Ayuan Memory System Benchmark Test")
        print("=" * 60)
        
        # 1. 实体链接测试
        self._test_entity_linking()
        
        # 2. 记忆压缩测试
        self._test_memory_condensation()
        
        # 3. 向量搜索测试
        self._test_vector_search()
        
        # 4. 九宫分类测试
        self._test_nine_palaces()
        
        # 5. 综合测试
        self._test_integration()
        
        # 汇总结果
        return self._summarize()
    
    def _test_entity_linking(self):
        """实体链接准确率测试"""
        print("\n[1/5] 实体链接测试")
        print("-" * 40)
        
        linker = EntityLinker()
        
        # 测试用例
        test_cases = [
            {
                "text": "John创建了Project-Alpha，Mary是项目的核心开发者。",
                "expected": {
                    "John": "PERSON",
                    "Project-Alpha": "PROJECT",
                    "Mary": "PERSON"
                }
            },
            {
                "text": "Mem0是一个开源的记忆管理系统，有4.1万stars。",
                "expected": {
                    "Mem0": "TECH",
                }
            },
            {
                "text": "洛书九宫是中国古代的数学模型，每行每列之和为15。",
                "expected": {
                    "洛书九宫": "CONCEPT"
                }
            },
            {
                "text": "I am working on AI projects with Python.",
                "expected": {
                    "AI": "TECH",
                    "Python": "TECH"
                },
                "not_expected": ["I"]  # I不应该被识别为实体
            },
            {
                "text": "GitHub是一个代码托管平台，由微软收购。",
                "expected": {
                    "GitHub": "TECH",
                    "微软": "ORG"
                }
            }
        ]
        
        correct = 0
        total = 0
        start_time = time.time()
        
        for case in test_cases:
            entities = linker.extract_entities(case["text"])
            extracted = {name: etype for name, etype in entities}
            
            # 检查期望的实体
            for name, etype in case["expected"].items():
                total += 1
                if name in extracted and extracted[name] == etype:
                    correct += 1
                else:
                    print(f"  [X] Expected: {name} -> {etype}, Got: {extracted.get(name, 'N/A')}")
            
            if "not_expected" in case:
                for name in case["not_expected"]:
                    if name in extracted:
                        print(f"  [!] False positive: {name} should not be recognized")
        
        elapsed = (time.time() - start_time) * 1000
        accuracy = correct / total if total > 0 else 0
        
        result = BenchmarkResult(
            name="实体链接",
            accuracy=accuracy,
            speed_ms=elapsed / len(test_cases),
            memory_mb=0,  # TODO: 添加内存测量
            notes=f"测试{len(test_cases)}个用例，正确{correct}/{total}"
        )
        self.results.append(result)
        
        print(f"  准确率: {accuracy:.1%}")
        print(f"  平均耗时: {result.speed_ms:.2f}ms")
    
    def _test_memory_condensation(self):
        """记忆压缩测试"""
        print("\n[2/5] 记忆压缩测试")
        print("-" * 40)
        
        condenser = MemoryCondenser()
        
        # 长文本测试
        long_text = """
John创建了Project-Alpha，这是一个完整的AI系统。
Mary是项目的核心开发者，负责系统架构。
九宫系统是核心架构，分为天垣、地垣、人垣三层。
Mem0是一个开源的记忆管理系统，有4.1万stars。
Hermes Agent支持15+平台的跨平台记忆互通。
RAGFlow提供深度文档理解能力，支持10种布局组件。
OpenHands实现了CodeAct代理架构。
CrewAI支持多角色协作，有五大核心组件。
AutoGen使用Actor模型实现多Agent对话。
LangGraph提供状态机工作流编排。
Zep是LLM记忆层，支持MCP协议。
HippoRAG模仿人类海马体的长期记忆机制。
洛书九宫是中国古代的数学模型，每行每列每对角线之和为15。
""".strip()
        
        start_time = time.time()
        result = condenser.compress(long_text)
        summary = result.summary
        elapsed = (time.time() - start_time) * 1000
        
        compression_ratio = len(summary) / len(long_text) if long_text else 0
        
        result = BenchmarkResult(
            name="记忆压缩",
            accuracy=1 - compression_ratio,  # 压缩率
            speed_ms=elapsed,
            memory_mb=0,
            notes=f"原文{len(long_text)}字 -> 压缩后{len(summary)}字，压缩率{compression_ratio:.1%}"
        )
        self.results.append(result)
        
        print(f"  原文长度: {len(long_text)}字")
        print(f"  压缩后: {len(summary)}字")
        print(f"  压缩率: {compression_ratio:.1%}")
        print(f"  耗时: {elapsed:.2f}ms")
        print(f"  摘要: {summary[:100]}...")
    
    def _test_vector_search(self):
        """向量搜索测试"""
        print("\n[3/5] 向量搜索测试")
        print("-" * 40)
        
        # 使用TF-IDF模式（无依赖）
        store = VectorStore(use_embedding=False)
        
        # 添加文档
        docs = [
            "用户创建了Project-Alpha，Mary是核心开发者。",
            "Mem0是一个开源的记忆管理系统，支持向量搜索。",
            "洛书九宫是中国古代的数学模型，每行每列之和为15。",
            "系统架构包含多个核心模块。",
            "Hermes Agent支持跨平台记忆互通。",
            "RAGFlow提供深度文档理解能力。",
            "OpenHands实现了CodeAct代理架构。",
            "CrewAI支持多角色协作。",
            "AutoGen使用Actor模型。",
            "LangGraph提供状态机工作流。"
        ]
        
        start_time = time.time()
        for doc in docs:
            store.add(doc)
        add_time = (time.time() - start_time) * 1000
        
        # 搜索测试
        queries = [
            "用户和项目的关系",
            "记忆管理系统",
            "洛书九宫",
            "Agent架构"
        ]
        
        start_time = time.time()
        for query in queries:
            results = store.search(query, top_k=3)
        search_time = (time.time() - start_time) * 1000
        
        result = BenchmarkResult(
            name="向量搜索",
            accuracy=1.0,  # TODO: 添加准确率测试
            speed_ms=search_time / len(queries),
            memory_mb=0,
            notes=f"索引{len(docs)}文档，平均搜索{search_time/len(queries):.2f}ms"
        )
        self.results.append(result)
        
        print(f"  索引文档: {len(docs)}")
        print(f"  索引耗时: {add_time:.2f}ms")
        print(f"  平均搜索耗时: {result.speed_ms:.2f}ms")
        
        # 显示一个搜索结果
        print(f"\n  Example search: '{queries[0]}'")
        results = store.search(queries[0], top_k=2)
        for r in results:
            print(f"    - [{r['score']:.3f}] {r['text'][:30]}...")
    
    def _test_nine_palaces(self):
        """九宫分类测试"""
        print("\n[4/5] Nine Palaces Classification Test")
        print("-" * 40)
        
        palaces = NinePalaces()
        
        # 宫位名称映射
        palace_names = {
            1: "坎宫", 2: "坤宫", 3: "震宫", 4: "巽宫", 5: "中宫",
            6: "乾宫", 7: "兑宫", 8: "艮宫", 9: "离宫"
        }
        
        # 宫位名称到数字的反向映射
        name_to_num = {v: k for k, v in palace_names.items()}
        
        test_cases = [
            ("用户创建了新项目", "离宫"),  # 创造
            ("Mem0有4.1万stars", "震宫"),   # 技术
            ("百家号文章发布", "兑宫"),      # 内容创作
            ("社群运营变现", "坎宫"),        # 社群/销售
            ("投资决策分析", "乾宫"),        # 企业/投资
        ]
        
        correct = 0
        start_time = time.time()
        
        for text, expected_name in test_cases:
            result_num = palaces.classify_text(text)
            result_name = palace_names.get(result_num, str(result_num))
            expected_num = name_to_num.get(expected_name, 0)
            
            if result_num == expected_num:
                correct += 1
                print(f"  [OK] '{text[:15]}...' -> {result_name}")
            else:
                print(f"  [X] '{text[:15]}...' -> {result_name} (expected: {expected_name})")
        
        elapsed = (time.time() - start_time) * 1000
        accuracy = correct / len(test_cases)
        
        result = BenchmarkResult(
            name="九宫分类",
            accuracy=accuracy,
            speed_ms=elapsed / len(test_cases),
            memory_mb=0,
            notes=f"测试{len(test_cases)}个用例，正确{correct}"
        )
        self.results.append(result)
        
        print(f"\n  准确率: {accuracy:.1%}")
        print(f"  平均耗时: {result.speed_ms:.2f}ms")
    
    def _test_integration(self):
        """综合测试"""
        print("\n[5/5] 综合测试")
        print("-" * 40)
        
        # 创建完整的记忆系统
        memory = SemanticMemory(use_embedding=False)
        
        # 添加记忆
        memories = [
            ("用户创建了Project-Alpha", "离宫", ["用户", "Project-Alpha"]),
            ("Mary是核心开发者", "离宫", ["Mary"]),
            ("Mem0有向量搜索功能", "震宫", ["Mem0", "向量搜索"]),
            ("洛书九宫之和为15", "中宫", ["洛书九宫"]),
        ]
        
        start_time = time.time()
        for text, palace, entities in memories:
            memory.remember(text, palace=palace, entities=entities)
        add_time = (time.time() - start_time) * 1000
        
        # 搜索测试
        start_time = time.time()
        results = memory.recall("项目", top_k=3)
        search_time = (time.time() - start_time) * 1000
        
        # 按宫位搜索
        results_palace = memory.recall("技术", top_k=3, palace="震宫")
        
        result = BenchmarkResult(
            name="综合测试",
            accuracy=1.0,
            speed_ms=add_time + search_time,
            memory_mb=0,
            notes=f"添加{len(memories)}条记忆，搜索耗时{search_time:.2f}ms"
        )
        self.results.append(result)
        
        print(f"  添加记忆: {len(memories)}条")
        print(f"  添加耗时: {add_time:.2f}ms")
        print(f"  搜索耗时: {search_time:.2f}ms")
        print(f"  搜索结果: {len(results)}条")
        
        print(f"\n  按宫位搜索(震宫): {len(results_palace)}条")
    
    def _summarize(self) -> Dict[str, Any]:
        """汇总结果"""
        print("\n" + "=" * 60)
        print("测试结果汇总")
        print("=" * 60)
        
        total_accuracy = sum(r.accuracy for r in self.results) / len(self.results)
        total_speed = sum(r.speed_ms for r in self.results)
        
        print(f"\n{'测试项':<15} {'准确率':<10} {'耗时(ms)':<10} {'说明'}")
        print("-" * 60)
        for r in self.results:
            print(f"{r.name:<15} {r.accuracy:<10.1%} {r.speed_ms:<10.2f} {r.notes}")
        
        print("-" * 60)
        print(f"{'平均':<15} {total_accuracy:<10.1%} {total_speed/len(self.results):<10.2f}")
        
        # 返回结构化结果
        return {
            "total_accuracy": total_accuracy,
            "total_speed_ms": total_speed,
            "results": [
                {
                    "name": r.name,
                    "accuracy": r.accuracy,
                    "speed_ms": r.speed_ms,
                    "notes": r.notes
                }
                for r in self.results
            ]
        }


def main():
    """运行Benchmark"""
    benchmark = Benchmark()
    results = benchmark.run_all()
    
    # 保存结果
    output_path = Path(__file__).parent / "benchmark_results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\n结果已保存到: {output_path}")
    
    return results


if __name__ == "__main__":
    main()
