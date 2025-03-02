"""
This module contains a simple performance test which
compares the recursive and iterative versions of Floyd's Algorithm,
testing both time and space scalability with the imperative version
"""
import sys
sys.path.append('../')
from time import process_time
from copy import deepcopy
import tracemalloc  # For memory measurement
from itertools import product
from iterative.iterative_floyd import iterative_floyd, GRAPH as ITERATIVE_GRAPH, MAX_LENGTH as ITERATIVE_MAX_LENGTH
from recursion.recursive_floyd import recursive_floyd_warshall, GRAPH as RECURSIVE_GRAPH, MIN_LEVEL, NO_PATH

def generate_graph(size):
    """
    Generate a square graph of the specified size with distances initialized.
    The graph is a 2D matrix where diagonal elements (node to itself) are 0,
    and off-diagonal elements are set to NO_PATH, representing no direct connection.
    """
    return [[0 if i == j else NO_PATH for j in range(size)] for i in range(size)]

def measure_memory():
    """
    Measure the current memory usage in kilobytes (KB)
    """
    snapshot = tracemalloc.take_snapshot()
    total_size = sum(stat.size for stat in snapshot.statistics('lineno')) / 1024  # Convert to KB
    return total_size

def performance_test(function_handle, graph_size, runs=10):
    """
    Perform a performance test measuring both execution time and memory usage.
    function_handle (callable): The function to test, either recursive_floyd_warshall or iterative_floyd.
    graph_size (int): The size of the square graph (n x n) to test.
    runs (int, optional): Number of times to run the test for averaging. Defaults to 10.
    """
    # Graph Generation
    global RECURSIVE_GRAPH, ITERATIVE_GRAPH, RECURSIVE_MAX_LENGTH, ITERATIVE_MAX_LENGTH
    RECURSIVE_GRAPH = generate_graph(graph_size)
    ITERATIVE_GRAPH = generate_graph(graph_size)
    RECURSIVE_MAX_LENGTH = graph_size
    ITERATIVE_MAX_LENGTH = graph_size

    total_time = 0
    total_memory = 0

    for _ in range(runs):
        # Measure memory usage (before execution)
        tracemalloc.start()
        start_memory = measure_memory()

        if function_handle.__name__ == "recursive_floyd_warshall":
            graph_copy = deepcopy(RECURSIVE_GRAPH)
            start_time = process_time()
            function_handle(MIN_LEVEL, MIN_LEVEL, MIN_LEVEL)
            total_time += process_time() - start_time
            RECURSIVE_GRAPH[:] = graph_copy
        else:
            graph_copy = deepcopy(ITERATIVE_GRAPH)
            start_time = process_time()
            function_handle()
            total_time += process_time() - start_time
            ITERATIVE_GRAPH[:] = graph_copy

        # Measure memory usage (after execution)
        end_memory = measure_memory()
        total_memory += end_memory - start_memory
        tracemalloc.stop()

    avg_time = total_time / runs
    avg_memory = total_memory / runs  # Average memory usage in KB
    return avg_time, avg_memory

# Test different graph sizes
graph_sizes = [4, 10, 20, 50, 100, 200, 500]

for size in graph_sizes:
    print(f"\nTesting graph size {size}x{size}")
    
    # Test recursive version
    recursive_time, recursive_memory = performance_test(recursive_floyd_warshall, size)
    print(f"Recursive version took {recursive_time:.6f} seconds and {recursive_memory:.2f} KB memory")

    # Test iterative version
    iterative_time, iterative_memory = performance_test(iterative_floyd, size)
    print(f"Iterative version took {iterative_time:.6f} seconds and {iterative_memory:.2f} KB memory")

    # Compare results
    if recursive_time < iterative_time:
        print(f"Recursive version is faster by {iterative_time - recursive_time:.6f} seconds")
    else:
        print(f"Iterative version is faster by {recursive_time - iterative_time:.6f} seconds")

    if recursive_memory < iterative_memory:
        print(f"Recursive version uses less memory by {iterative_memory - recursive_memory:.2f} KB")
    else:
        print(f"Iterative version uses less memory by {recursive_memory - iterative_memory:.2f} KB")