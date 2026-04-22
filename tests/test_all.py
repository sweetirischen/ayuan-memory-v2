"""
测试用例 - 确保代码可运行
"""

import sys
import os

# 添加父目录到路径
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from ayuan_memory import EntityLinker, MemoryCondenser, MemoryPalace, NinePalaces
from ayuan_memory.utils.storage import MemoryStorage


def test_entity_linker():
    """测试实体链接"""
    print("测试 EntityLinker...")
    
    # 使用内存存储
    linker = EntityLinker(storage_path=":memory:")
    
    # 测试提取实体
    text = "帝君让阿垣学习Mem0和Hermes的技术"
    entities = linker.extract_entities(text)
    print(f"  提取的实体: {entities}")
    
    # 测试链接实体
    entity = linker.link_entity("Mem0", "TECH", "memory_001", "记忆管理系统")
    print(f"  链接的实体: {entity.name}, 类型: {entity.entity_type}")
    
    print("  [OK] EntityLinker 测试通过\n")


def test_memory_condenser():
    """测试记忆压缩"""
    print("测试 MemoryCondenser...")
    
    condenser = MemoryCondenser()
    
    # 测试压缩
    text = """
    今天帝君教阿垣一个重要的道理：不要嘴把式，要做出真东西。
    
    阿垣决定做一个记忆管理系统，发到GitHub上。
    
    决定使用Python写一个可运行的包，不是文档。
    
    教训：写文档不等于完成，写出可运行的代码才是完成。
    """
    
    compressed = condenser.compress(text)
    print(f"  总结: {compressed.summary[:50]}...")
    print(f"  关键点数量: {len(compressed.key_points)}")
    print(f"  决策数量: {len(compressed.decisions)}")
    print(f"  教训数量: {len(compressed.lessons)}")
    
    print("  [OK] MemoryCondenser 测试通过\n")


def test_nine_palaces():
    """测试九宫分类"""
    print("测试 NinePalaces...")
    
    palaces = NinePalaces()
    
    # 测试获取宫位信息
    info = palaces.get_palace(1)
    print(f"  坎宫信息: {info.name}, 五行: {info.element}, 含义: {info.meaning}")
    
    # 测试分类
    text = "这是一个关于技术开发的项目"
    palace_num = palaces.classify_text(text)
    palace_info = palaces.get_palace(palace_num)
    print(f"  '{text}' 分类到: {palace_info.name}")
    
    # 测试三垣
    yuan = palaces.get_three_yuan(9)
    print(f"  离宫所属三垣: {yuan}")
    
    # 测试平衡检查
    counts = {1: 5, 2: 3, 3: 4, 4: 5, 5: 6, 6: 4, 7: 5, 8: 3, 9: 5}
    is_balanced, score = palaces.check_balance(counts)
    print(f"  平衡分数: {score:.2f}, 是否平衡: {is_balanced}")
    
    print("  [OK] NinePalaces 测试通过\n")


def test_memory_palace():
    """测试记忆宫殿"""
    print("测试 MemoryPalace...")
    
    # 使用内存存储
    palace = MemoryPalace(storage_path=":memory:")
    
    # 测试添加记忆
    memory = {
        "content": "帝君教阿垣要做出真东西",
        "type": "wisdom",
        "tags": ["教诲", "重要"]
    }
    room = palace.add_memory(memory, palace_number=9)
    print(f"  记忆添加到: {room.name}")
    
    # 测试搜索
    results = palace.search("帝君")
    print(f"  搜索'帝君'结果数量: {len(results)}")
    
    # 测试统计
    stats = palace.get_palace_stats()
    print(f"  离宫记忆数量: {stats[9]['memory_count']}")
    
    print("  [OK] MemoryPalace 测试通过\n")


def test_storage():
    """测试存储"""
    print("测试 Storage...")
    
    storage = MemoryStorage()
    
    # 测试保存
    data = {"test": "data", "number": 123}
    storage.save("test_001", data)
    print("  保存成功")
    
    # 测试加载
    loaded = storage.load("test_001")
    print(f"  加载成功: {loaded}")
    
    # 测试存在
    exists = storage.exists("test_001")
    print(f"  存在检查: {exists}")
    
    # 测试列表
    keys = storage.list_keys()
    print(f"  所有键: {keys}")
    
    print("  [OK] Storage 测试通过\n")


def run_all_tests():
    """运行所有测试"""
    print("=" * 50)
    print("阿垣记忆系统 - 测试套件")
    print("=" * 50 + "\n")
    
    test_entity_linker()
    test_memory_condenser()
    test_nine_palaces()
    test_memory_palace()
    test_storage()
    
    print("=" * 50)
    print("所有测试通过！")
    print("=" * 50)


if __name__ == "__main__":
    run_all_tests()
