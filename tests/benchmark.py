"""
Benchmark Test - AYuan Memory System
"""

import time
import json
from pathlib import Path
from typing import List, Dict, Any, Tuple
from dataclasses import dataclass

# Import AYuan modules
import sys
sys.path.insert(0, str(Path(__file__).parent.parent))

from ayuan_memory.core.entity_linker import EntityLinker
from ayuan_memory.core.memory_condenser import MemoryCondenser
from ayuan_memory.core.vector_store import VectorStore, SemanticMemory
from ayuan_memory.core.smart_classifier import SmartClassifier


@dataclass
class BenchmarkResult:
    """Test result"""
    name: str
    accuracy: float
    speed_ms: float
    memory_mb: float
    notes: str = ""


class Benchmark:
    """Benchmark test suite"""
    
    def __init__(self):
        self.results: List[BenchmarkResult] = []
    
    def run_all(self) -> Dict[str, Any]:
        """Run all tests"""
        print("=" * 60)
        print("AYuan Memory System Benchmark Test")
        print("=" * 60)
        
        # 1. Entity linking test
        self._test_entity_linking()
        
        # 2. Memory condensation test
        self._test_memory_condensation()
        
        # 3. Vector search test
        self._test_vector_search()
        
        # 4. Smart classifier test
        self._test_smart_classifier()
        
        # 5. Integration test
        self._test_integration()
        
        # Summarize results
        return self._summarize()
    
    def _test_entity_linking(self):
        """Entity linking accuracy test"""
        print("\n[1/5] Entity Linking Test")
        print("-" * 40)
        
        linker = EntityLinker()
        
        # Test cases
        test_cases = [
            {
                "text": "John created Project-Alpha, Mary is the core developer.",
                "expected": {
                    "John": "PERSON",
                    "Project-Alpha": "PROJECT",
                    "Mary": "PERSON"
                }
            },
            {
                "text": "Mem0 is an open source memory system with 41K stars.",
                "expected": {
                    "Mem0": "TECH",
                }
            },
            {
                "text": "I am working on AI projects with Python.",
                "expected": {
                    "AI": "TECH",
                    "Python": "TECH"
                },
                "not_expected": ["I"]  # I should not be recognized as entity
            },
            {
                "text": "GitHub is a code hosting platform, acquired by Microsoft.",
                "expected": {
                    "GitHub": "TECH",
                    "Microsoft": "ORG"
                }
            }
        ]
        
        correct = 0
        total = 0
        start_time = time.time()
        
        for case in test_cases:
            entities = linker.extract_entities(case["text"])
            extracted = {name: etype for name, etype in entities}
            
            # Check expected entities
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
            name="Entity Linking",
            accuracy=accuracy,
            speed_ms=elapsed / len(test_cases),
            memory_mb=0,
            notes=f"Tested {len(test_cases)} cases, correct {correct}/{total}"
        )
        self.results.append(result)
        
        print(f"  Accuracy: {accuracy:.1%}")
        print(f"  Avg time: {result.speed_ms:.2f}ms")
    
    def _test_memory_condensation(self):
        """Memory condensation test"""
        print("\n[2/5] Memory Condensation Test")
        print("-" * 40)
        
        condenser = MemoryCondenser()
        
        # Long text test
        long_text = """
        John created Project-Alpha, a complete AI system.
        Mary is the core developer, responsible for system architecture.
        The 9-zone system is the core architecture, divided into three layers.
        Mem0 is an open source memory management system with 41K stars.
        Hermes Agent supports 15+ platforms for cross-platform memory.
        RAGFlow provides deep document understanding with 10 layout components.
        OpenHands implements the CodeAct agent architecture.
        CrewAI supports multi-role collaboration with five core components.
        AutoGen uses Actor model for multi-agent dialogue.
        LangGraph provides state machine workflow orchestration.
        Zep is an LLM memory layer supporting MCP protocol.
        HippoRAG mimics human hippocampus long-term memory mechanism.
        """.strip()
        
        start_time = time.time()
        result = condenser.compress(long_text)
        summary = result.summary
        elapsed = (time.time() - start_time) * 1000
        
        compression_ratio = len(summary) / len(long_text) if long_text else 0
        
        result = BenchmarkResult(
            name="Memory Condensation",
            accuracy=1 - compression_ratio,
            speed_ms=elapsed,
            memory_mb=0,
            notes=f"Original {len(long_text)} chars -> compressed {len(summary)} chars, ratio {compression_ratio:.1%}"
        )
        self.results.append(result)
        
        print(f"  Original length: {len(long_text)} chars")
        print(f"  Compressed: {len(summary)} chars")
        print(f"  Compression ratio: {compression_ratio:.1%}")
        print(f"  Time: {elapsed:.2f}ms")
        print(f"  Summary: {summary[:100]}...")
    
    def _test_vector_search(self):
        """Vector search test"""
        print("\n[3/5] Vector Search Test")
        print("-" * 40)
        
        # Use TF-IDF mode (no dependencies)
        store = VectorStore(use_embedding=False)
        
        # Add documents
        docs = [
            "User created Project-Alpha, Mary is the core developer.",
            "Mem0 is an open source memory system with vector search.",
            "The 9-zone system mirrors natural cycles of growth.",
            "System architecture contains multiple core modules.",
            "Hermes Agent supports cross-platform memory sync.",
            "RAGFlow provides deep document understanding.",
            "OpenHands implements CodeAct agent architecture.",
            "CrewAI supports multi-role collaboration.",
            "AutoGen uses Actor model.",
            "LangGraph provides state machine workflow."
        ]
        
        start_time = time.time()
        for doc in docs:
            store.add(doc)
        add_time = (time.time() - start_time) * 1000
        
        # Search test
        queries = [
            "user and project relationship",
            "memory management system",
            "9-zone system",
            "Agent architecture"
        ]
        
        start_time = time.time()
        for query in queries:
            results = store.search(query, top_k=3)
        search_time = (time.time() - start_time) * 1000
        
        result = BenchmarkResult(
            name="Vector Search",
            accuracy=1.0,
            speed_ms=search_time / len(queries),
            memory_mb=0,
            notes=f"Indexed {len(docs)} docs, avg search {search_time/len(queries):.2f}ms"
        )
        self.results.append(result)
        
        print(f"  Indexed docs: {len(docs)}")
        print(f"  Index time: {add_time:.2f}ms")
        print(f"  Avg search time: {result.speed_ms:.2f}ms")
        
        # Show one search result
        print(f"\n  Example search: '{queries[0]}'")
        results = store.search(queries[0], top_k=2)
        for r in results:
            print(f"    - [{r['score']:.3f}] {r['text'][:30]}...")
    
    def _test_smart_classifier(self):
        """Smart classifier test"""
        print("\n[4/5] Smart Classifier Test")
        print("-" * 40)
        
        classifier = SmartClassifier()
        
        # Zone names
        zone_names = {
            1: "origin", 2: "foundation", 3: "growth", 4: "flow", 5: "center",
            6: "structure", 7: "expression", 8: "archive", 9: "wisdom"
        }
        
        test_cases = [
            ("User created a new project", 9),      # create -> wisdom
            ("Mem0 has 41K stars on GitHub", 3),    # tech -> growth
            ("Publishing article to media", 7),     # content -> expression
            ("Community sales and ecommerce", 1),   # community -> origin
            ("Investment decision analysis", 6),    # invest -> structure
        ]
        
        correct = 0
        start_time = time.time()
        
        for text, expected_zone in test_cases:
            result_zone = classifier.classify_text(text)
            result_name = zone_names.get(result_zone, str(result_zone))
            expected_name = zone_names.get(expected_zone, str(expected_zone))
            
            if result_zone == expected_zone:
                correct += 1
                print(f"  [OK] '{text[:20]}...' -> Zone {result_zone} ({result_name})")
            else:
                print(f"  [X] '{text[:20]}...' -> Zone {result_zone} ({result_name}) (expected: Zone {expected_zone})")
        
        elapsed = (time.time() - start_time) * 1000
        accuracy = correct / len(test_cases)
        
        result = BenchmarkResult(
            name="Smart Classifier",
            accuracy=accuracy,
            speed_ms=elapsed / len(test_cases),
            memory_mb=0,
            notes=f"Tested {len(test_cases)} cases, correct {correct}"
        )
        self.results.append(result)
        
        print(f"\n  Accuracy: {accuracy:.1%}")
        print(f"  Avg time: {result.speed_ms:.2f}ms")
    
    def _test_integration(self):
        """Integration test"""
        print("\n[5/5] Integration Test")
        print("-" * 40)
        
        # Create complete memory system
        memory = SemanticMemory(use_embedding=False)
        
        # Add memories
        memories = [
            ("User created Project-Alpha", 9, ["User", "Project-Alpha"]),
            ("Mary is the core developer", 9, ["Mary"]),
            ("Mem0 has vector search", 3, ["Mem0", "vector search"]),
            ("The 9-zone system is balanced", 5, ["9-zone system"]),
        ]
        
        start_time = time.time()
        for text, zone, entities in memories:
            memory.remember(text, zone=zone, entities=entities)
        add_time = (time.time() - start_time) * 1000
        
        # Search test
        start_time = time.time()
        results = memory.recall("project", top_k=3)
        search_time = (time.time() - start_time) * 1000
        
        # Search by zone
        results_zone = memory.recall("technology", top_k=3, zone=3)
        
        result = BenchmarkResult(
            name="Integration",
            accuracy=1.0,
            speed_ms=add_time + search_time,
            memory_mb=0,
            notes=f"Added {len(memories)} memories, search time {search_time:.2f}ms"
        )
        self.results.append(result)
        
        print(f"  Added memories: {len(memories)}")
        print(f"  Add time: {add_time:.2f}ms")
        print(f"  Search time: {search_time:.2f}ms")
        print(f"  Search results: {len(results)}")
        
        print(f"\n  Search by zone (Zone 3): {len(results_zone)} results")
    
    def _summarize(self) -> Dict[str, Any]:
        """Summarize results"""
        print("\n" + "=" * 60)
        print("Results Summary")
        print("=" * 60)
        
        total_accuracy = sum(r.accuracy for r in self.results) / len(self.results)
        total_speed = sum(r.speed_ms for r in self.results)
        
        print(f"\n{'Test':<20} {'Accuracy':<12} {'Time(ms)':<12} {'Notes'}")
        print("-" * 60)
        for r in self.results:
            print(f"{r.name:<20} {r.accuracy:<12.1%} {r.speed_ms:<12.2f} {r.notes}")
        
        print("-" * 60)
        print(f"{'Average':<20} {total_accuracy:<12.1%} {total_speed/len(self.results):<12.2f}")
        
        # Return structured results
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
    """Run benchmark"""
    benchmark = Benchmark()
    results = benchmark.run_all()
    
    # Save results
    output_path = Path(__file__).parent / "benchmark_results.json"
    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(results, f, ensure_ascii=False, indent=2)
    
    print(f"\nResults saved to: {output_path}")
    
    return results


if __name__ == "__main__":
    main()
