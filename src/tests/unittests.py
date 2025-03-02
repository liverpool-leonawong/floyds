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
        """Graph Initialization"""
        # Define the connected graph for testing and store the original graph
        self.original_recursive_graph = deepcopy(RECURSIVE_GRAPH)
        self.original_iterative_graph = deepcopy(ITERATIVE_GRAPH)
        self.max_length = MAX_LENGTH  # Assuming same square graph for both versions

    def tearDown(self):
        """Graph Reset Test"""
        # Reset the graph after each test
        RECURSIVE_GRAPH[:] = self.original_recursive_graph
        ITERATIVE_GRAPH[:] = self.original_iterative_graph

    def run_recursive(self, graph=None):
        """Custom Graph Test (Recursive)"""
        # Test Recursive Version with optional custom graph
        if graph is not None:
            RECURSIVE_GRAPH[:] = deepcopy(graph)
        recursive_floyd_warshall(MIN_LEVEL, MIN_LEVEL, MIN_LEVEL)

    def run_iterative(self, graph=None):
        """Custom Graph Test (Iterative)"""
        # Test Iterative Version with optional custom graph
        if graph is not None:
            ITERATIVE_GRAPH[:] = deepcopy(graph)
        iterative_floyd()

    def test_connected_graph_correctness(self):
        """Shortest Path Accuracy Test"""
        self.run_recursive()
        self.run_iterative()

        expected_graph = [
            [0, 8, 13, 15],  # So Kwun Wat (Node 0)
            [14, 0, 5, 7],    # Town Plaza (Node 1)
            [9, 5, 0, 2],   # V City (Node 2)
            [7, 7, 2, 0]    # Trend Plaza (Node 3)
        ]

        # Test recursive
        for i in range(self.max_length):
            for j in range(self.max_length):
                self.assertEqual(RECURSIVE_GRAPH[i][j], expected_graph[i][j],
                                 f"Recursive failed at [{i},{j}]: expected {expected_graph[i][j]}, got {RECURSIVE_GRAPH[i][j]}")

        # Test iterative
        for i in range(self.max_length):
            for j in range(self.max_length):
                self.assertEqual(ITERATIVE_GRAPH[i][j], expected_graph[i][j],
                                 f"Iterative failed at [{i},{j}]: expected {expected_graph[i][j]}, got {ITERATIVE_GRAPH[i][j]}")

    def test_consistency_between_versions(self):
        """Consistency Test""" 
        # Check if both versions produce the same results
        self.run_recursive()
        self.run_iterative()

        for i in range(self.max_length):
            for j in range(self.max_length):
                self.assertEqual(RECURSIVE_GRAPH[i][j], ITERATIVE_GRAPH[i][j],
                                 f"Inconsistency at [{i},{j}]: recursive={RECURSIVE_GRAPH[i][j]}, iterative={ITERATIVE_GRAPH[i][j]}")

    def test_self_distance(self):
        """Self-Distance Handling"""
        self.run_recursive()
        self.run_iterative()

        for i in range(self.max_length):
            self.assertEqual(
                RECURSIVE_GRAPH[i][i], 0, f"Recursive self-distance failed at node {i}")
            self.assertEqual(
                ITERATIVE_GRAPH[i][i], 0, f"Iterative self-distance failed at node {i}")

    def test_one_way_route_handling(self):
        """One-Way Route Handling Scenario Test"""
        # Tests one-way route handling with no-path cases in directed graphs
        one_way_graph = [
            [0, 7, NO_PATH, 8],  # So Kwun Wat (Node 0)
            [NO_PATH, 0, 5, NO_PATH],  # Par City (Node 1)
            [NO_PATH, NO_PATH, 0, 2],  # Tuen Mun Park (Node 2)
            [NO_PATH, NO_PATH, NO_PATH, 0]  # Apple Shop (Node 3)
        ]

        # Test recursive version
        self.run_recursive(one_way_graph)
        self.assertEqual(
            RECURSIVE_GRAPH[1][0], NO_PATH, "Recursive should keep NO_PATH for Trend Plaza to So Kwun Wat")
        self.assertEqual(
            RECURSIVE_GRAPH[2][0], NO_PATH, "Recursive should keep NO_PATH for V City to So Kwun Wat")
        self.assertEqual(
            RECURSIVE_GRAPH[3][0], NO_PATH, "Recursive should keep NO_PATH for Town Plaza to So Kwun Wat")
        self.assertEqual(
            RECURSIVE_GRAPH[0][1], 7, "Recursive should maintain path from So Kwun Wat to Trend Plaza")
        self.assertEqual(
            RECURSIVE_GRAPH[0][3], 8, "Recursive should maintain initial path from So Kwun Wat to Town Plaza before updates")

        # Test iterative version
        self.run_iterative(one_way_graph)
        self.assertEqual(
            ITERATIVE_GRAPH[1][0], NO_PATH, "Iterative should keep NO_PATH for Trend Plaza to So Kwun Wat")
        self.assertEqual(
            ITERATIVE_GRAPH[2][0], NO_PATH, "Iterative should keep NO_PATH for V City to So Kwun Wat")
        self.assertEqual(
            ITERATIVE_GRAPH[3][0], NO_PATH, "Iterative should keep NO_PATH for Town Plaza to So Kwun Wat")
        self.assertEqual(
            ITERATIVE_GRAPH[0][1], 7, "Iterative should maintain path from So Kwun Wat to Trend Plaza")
        self.assertEqual(
            ITERATIVE_GRAPH[0][3], 8, "Iterative should maintain initial path from So Kwun Wat to Town Plaza before updates")

        # Verify shortest paths for existing one-way routes after updates
        expected_one_way_result = [
            [0, 7, 12, 8],  # So Kwun Wat (Node 0)
            [NO_PATH, 0, 5, 7],  # Par City (Node 1)
            [NO_PATH, NO_PATH, 0, 2],  # Tuen Mun Park (Node 2)
            [NO_PATH, NO_PATH, NO_PATH, 0]  # Apple Shop (Node 3)
        ]

        for i in range(self.max_length):
            for j in range(self.max_length):
                self.assertEqual(RECURSIVE_GRAPH[i][j], expected_one_way_result[i][j],
                                 f"Recursive failed at [{i},{j}] for one-way graph: expected {expected_one_way_result[i][j]}, got {RECURSIVE_GRAPH[i][j]}")
                self.assertEqual(ITERATIVE_GRAPH[i][j], expected_one_way_result[i][j],
                                 f"Iterative failed at [{i},{j}] for one-way graph: expected {expected_one_way_result[i][j]}, got {ITERATIVE_GRAPH[i][j]}")


if __name__ == "__main__":
    unittest.main(verbosity=2)
