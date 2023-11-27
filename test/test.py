import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
import unittest
from src.merge_sort import merge_sort

class TestMergeSort(unittest.TestCase):
    def test_case1(self):
        # 测试一个正确的用例
        assert merge_sort([4, 3, 2, 1, 6]) == [1, 2, 3, 4, 6]

if __name__ == '__main__':
    unittest.main()