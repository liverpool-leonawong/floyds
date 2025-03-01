"""
This module contains unit tests for both recursive and iterative implementations of Floyd's Algorithm
to ensure they correctly compute shortest paths.
"""

import sys
sys.path.append('../')
import unittest
from copy import deepcopy

from recursion.recursive_floyd import recursive_floyd_warshall, GRAPH as RECURSIVE_GRAPH, MIN_LEVEL, NO_PATH, MAX_LENGTH
from iterative.iterative_floyd import iterative_floyd, GRAPH as ITERATIVE_GRAPH

class TestFloydsAlgorithm(unittest.TestCase):
    def setUp(self):
        """在每個測試之前初始化 GRAPH，確保測試獨立"""
        # 複製原始 GRAPH，避免測試互相影響
        self.original_recursive_graph = deepcopy(RECURSIVE_GRAPH)
        self.original_iterative_graph = deepcopy(ITERATIVE_GRAPH)
        self.max_length = MAX_LENGTH  # 假設兩版本 MAX_LENGTH 相同

    def tearDown(self):
        """在每個測試之後還原 GRAPH"""
        RECURSIVE_GRAPH[:] = self.original_recursive_graph
        ITERATIVE_GRAPH[:] = self.original_iterative_graph

    def run_recursive(self):
        """執行 recursive 版本"""
        recursive_floyd_warshall(MIN_LEVEL, MIN_LEVEL, MIN_LEVEL)

    def run_iterative(self):
        """執行 iterative 版本"""
        iterative_floyd()

    def test_recursive_correctness(self):
        """測試 recursive 版本是否正確計算最短路徑"""
        self.run_recursive()

        expected_graph = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

        for i in range(self.max_length):
            for j in range(self.max_length):
                self.assertEqual(RECURSIVE_GRAPH[i][j], expected_graph[i][j],
                                 f"Recursive failed at [{i},{j}]: expected {expected_graph[i][j]}, got {RECURSIVE_GRAPH[i][j]}")

    def test_iterative_correctness(self):
        """測試 iterative 版本是否正確計算最短路徑"""
        self.run_iterative()

        expected_graph = [
            [0, 7, 12, 8],
            [NO_PATH, 0, 5, 7],
            [NO_PATH, NO_PATH, 0, 2],
            [NO_PATH, NO_PATH, NO_PATH, 0]
        ]

        for i in range(self.max_length):
            for j in range(self.max_length):
                self.assertEqual(ITERATIVE_GRAPH[i][j], expected_graph[i][j],
                                 f"Iterative failed at [{i},{j}]: expected {expected_graph[i][j]}, got {ITERATIVE_GRAPH[i][j]}")

    def test_consistency_between_versions(self):
        """測試兩版本是否產生相同嘅結果"""
        self.run_recursive()
        self.run_iterative()

        for i in range(self.max_length):
            for j in range(self.max_length):
                self.assertEqual(RECURSIVE_GRAPH[i][j], ITERATIVE_GRAPH[i][j],
                                 f"Inconsistency at [{i},{j}]: recursive={RECURSIVE_GRAPH[i][j]}, iterative={ITERATIVE_GRAPH[i][j]}")

    def test_no_path_handling(self):
        """測試兩版本是否正確處理無路徑（NO_PATH）"""
        self.run_recursive()
        self.run_iterative()

        self.assertEqual(
            RECURSIVE_GRAPH[1][0], NO_PATH, "Recursive should keep NO_PATH for Trend Plaza to So Kwun Wat")
        self.assertEqual(
            ITERATIVE_GRAPH[1][0], NO_PATH, "Iterative should keep NO_PATH for Trend Plaza to So Kwun Wat")

    def test_self_distance(self):
        """測試兩版本嘅節點到自己嘅距離是否為 0"""
        self.run_recursive()
        self.run_iterative()

        for i in range(self.max_length):
            self.assertEqual(
                RECURSIVE_GRAPH[i][i], 0, f"Recursive self-distance failed at node {i}")
            self.assertEqual(
                ITERATIVE_GRAPH[i][i], 0, f"Iterative self-distance failed at node {i}")


if __name__ == "__main__":
    unittest.main()
