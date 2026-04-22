"""
Test Suite - AYuan Memory System
"""

import sys
import os

# Add parent directory to path
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ayuan_memory import EntityLinker, MemoryCondenser, MemoryPalace, SmartClassifier, Evolution
from ayuan_memory.utils.storage import MemoryStorage


def test_entity_linker():
    """Test Entity Linker"""
    print("Testing EntityLinker...")
    
    # Use memory storage
    linker = EntityLinker(storage_path=":memory:")
    
    # Test extracting entities
    text = "DiJun created ZiWeiEmpire, AYuan is the core system"
    entities = linker.extract_entities(text)
    print(f"  Extracted entities: {entities}")
    
    # Test linking entity
    entity = linker.link_entity("AYuan", "PROJECT", "memory_001", "Memory management system")
    print(f"  Linked entity: {entity.name}, type: {entity.entity_type}")
    
    print("  [OK] EntityLinker test passed\n")


def test_memory_condenser():
    """Test Memory Condenser"""
    print("Testing MemoryCondenser...")
    
    condenser = MemoryCondenser()
    
    # Test compression
    text = """
    Today we learned an important lesson: don't just talk, make real things.
    
    We decided to build a memory management system and publish to GitHub.
    
    Decision: Use Python to write a runnable package, not just documentation.
    
    Lesson: Writing documentation is not completion, runnable code is completion.
    """
    
    compressed = condenser.compress(text)
    print(f"  Summary: {compressed.summary[:50]}...")
    print(f"  Key points count: {len(compressed.key_points)}")
    print(f"  Decisions count: {len(compressed.decisions)}")
    print(f"  Lessons count: {len(compressed.lessons)}")
    
    print("  [OK] MemoryCondenser test passed\n")


def test_smart_classifier():
    """Test Smart Classifier"""
    print("Testing SmartClassifier...")
    
    classifier = SmartClassifier()
    
    # Test getting zone info
    info = classifier.get_zone(1)
    print(f"  Zone 1 info: {info.name}, description: {info.description}")
    
    # Test classification
    text = "This is a project about technical development"
    zone_num = classifier.classify_text(text)
    zone_info = classifier.get_zone(zone_num)
    print(f"  '{text}' classified to: Zone {zone_num} ({zone_info.name})")
    
    # Test balance check
    counts = {1: 5, 2: 3, 3: 4, 4: 5, 5: 6, 6: 4, 7: 5, 8: 3, 9: 5}
    is_balanced, score = classifier.check_balance(counts)
    print(f"  Balance score: {score:.2f}, is balanced: {is_balanced}")
    
    # Test generation path
    path = classifier.get_generation_path()
    print(f"  Generation path: {path}")
    
    print("  [OK] SmartClassifier test passed\n")


def test_memory_palace():
    """Test Memory Palace"""
    print("Testing MemoryPalace...")
    
    # Use memory storage
    palace = MemoryPalace(storage_path=":memory:")
    
    # Test adding memory
    memory = {
        "content": "Important lesson learned today",
        "type": "wisdom",
        "tags": ["lesson", "important"]
    }
    room = palace.add_memory(memory, zone_number=9)
    print(f"  Memory added to: Zone {room.zone_number} ({room.name})")
    
    # Test search
    results = palace.search("lesson")
    print(f"  Search 'lesson' results count: {len(results)}")
    
    # Test stats
    stats = palace.get_zone_stats()
    print(f"  Zone 9 memory count: {stats[9]['memory_count']}")
    
    print("  [OK] MemoryPalace test passed\n")


def test_storage():
    """Test Storage"""
    print("Testing Storage...")
    
    storage = MemoryStorage()
    
    # Test save
    data = {"test": "data", "number": 123}
    storage.save("test_001", data)
    print("  Save successful")
    
    # Test load
    loaded = storage.load("test_001")
    print(f"  Load successful: {loaded}")
    
    # Test exists
    exists = storage.exists("test_001")
    print(f"  Exists check: {exists}")
    
    # Test list
    keys = storage.list_keys()
    print(f"  All keys: {keys}")
    
    print("  [OK] Storage test passed\n")


def test_evolution():
    """Test Evolution"""
    print("Testing Evolution...")
    
    evo = Evolution()
    
    # Test version
    version = evo.get_version()
    print(f"  Current version: v{version}")
    
    # Test abilities count
    abilities_count = len(evo.abilities)
    print(f"  Abilities count: {abilities_count}")
    
    # Test plans count
    plans_count = len(evo.plans)
    print(f"  Future plans count: {plans_count}")
    
    # Test evolution history
    history_count = len(evo.history)
    print(f"  Evolution history count: {history_count}")
    
    print("  [OK] Evolution test passed\n")


def run_all_tests():
    """Run all tests"""
    print("=" * 50)
    print("AYuan Memory System - Test Suite")
    print("=" * 50 + "\n")
    
    test_entity_linker()
    test_memory_condenser()
    test_smart_classifier()
    test_memory_palace()
    test_storage()
    test_evolution()
    
    print("=" * 50)
    print("All tests passed!")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
