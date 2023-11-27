from src.merge_sort import merge_sort

def test_case1():
    # 测试一个正确的用例
    assert merge_sort([4, 3, 2, 1, 6]) == [1, 2, 3, 4, 6]

def test_case2():
    # 测试具有重复项的用例
    assert merge_sort([5, 9, 6, 13, 9, 8, 4, 7, 0]) == [0, 4, 5, 6, 7, 8, 9, 9, 13]
    
def test_case3():
    # 测试正序用例
    assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

def test_case4():
    # 测试倒序用例
    assert merge_sort([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10]
    
def test_case5():
    # 测试具有负项的用例
    assert merge_sort([-4, 8, -5, 2, 4, -9]) == [-9, -4, -5, 2, 4, 8]

def test_case6():
    # 测试非整数用例
    assert merge_sort([7.834, 60.264, 9.2, 6.4987, 175.6]) == [6.4987, 7.834, 9.2, 60.264, 175.6]