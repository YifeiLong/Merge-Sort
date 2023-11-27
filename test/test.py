import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from src.merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_case1(self):
        # 测试一个正确的用例
        assert merge_sort([4, 3, 2, 1, 6]) == [1, 2, 3, 4, 6]
    def test_case2(self):
        # 测试具有重复项的用例
        assert merge_sort([5, 9, 6, 13, 9, 8, 4, 7, 0]) == [0, 4, 5, 6, 7, 8, 9, 9, 13]
        
    def test_case3(self):
        # 测试正序用例
        assert merge_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]

    def test_case4(self):
        # 测试倒序用例
        assert merge_sort([10, 9, 8, 7, 6]) == [6, 7, 8, 9, 10]
        
    def test_case5(self):
        # 测试具有负项的用例
        assert merge_sort([-4, 8, -5, 2, 4, -9]) == [-9, -5, -4, 2, 4, 8]

    def test_case6(self):
        # 测试非整数用例
        assert merge_sort([7.834, 60.264, 9.2, 6.4987, 175.6]) == [6.4987, 7.834, 9.2, 60.264, 175.6]
if __name__ == '__main__':
    unittest.main()