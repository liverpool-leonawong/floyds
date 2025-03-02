"""
This module has a simple implementation of Floyd's Algorithm
It contains three main functions:
    main -> controls the execution of the script
    print_out_graph -> prints out the graph with nodes and distances
    recursive_floyd_warshall -> computes shortest path

The global variables are:
    NO_PATH = Marker for where there is no path. This is the max value of an integer
    GRAPH = Contains the distances for the graph. Node names are inferred by the position
    of the node, i.e. position  0 0 in the list is node 0
    MAX_LENGTH = The size of the graph
    MIN_LEVEL = The lowest search level for the shortest path calculation
    NO_PATH_MARKER = Holder for no path possible. This is used for the printing function.
"""
from sys import maxsize
NO_PATH = maxsize
GRAPH = [[0, 8, NO_PATH, NO_PATH],  # Node 0 (So Kwun Wat)
         [NO_PATH, 0, 5, NO_PATH],  # Node 1 (Town Plaza)
         [NO_PATH, 5, 0, 2],  # Node 2 (V City)
         [7, NO_PATH, 2, 0]]  # Node 3 (Trend Plaza)
MAX_LENGTH = len(GRAPH[0])
MIN_LEVEL = 0
NO_PATH_MARKER = "No Path"

def main():
    """
    This is the calling function for the recursive floyd's algorithm
    """
    # Start the recursive Floyd's algorithm
    recursive_floyd_warshall(MIN_LEVEL, MIN_LEVEL, MIN_LEVEL)

    # Print the updated graph
    print_out_graph()

def print_out_graph():
    """
    This function prints out the graph with the distances
    and a place holder for no path between nodes
    """
    for start_node in range(0, MAX_LENGTH):
        for end_node in range(0, MAX_LENGTH):
            distance = GRAPH[start_node][end_node]
            if distance == NO_PATH:
                distance = NO_PATH_MARKER

            message = "Distance from Node %s to Node %s is %s" %\
                (start_node, end_node, distance)
            print(message)

def recursive_floyd_warshall(outer_loop: int, middle_loop: int, inner_loop: int):
    """
    This function computes shortest path between each pair node
    It computes by comparing a direct path with paths that have
    intermediate nodes in the path.

    The recursive path is the shortest path function which
    calls itself to find the shortest path between a pair of nodes

    You need to increment each variable until it reaches a loop

    param: outer_loop: This variable is from the first loop of the iterative version
    param: middle_loop: This variable is from the second loop of the iterative version
    param: inner_loop: This variable is from the last loop of the iterative version
    """
    # Base case
    if outer_loop >= MAX_LENGTH:  # When outer loop reaches the maximum length, recursion ends
        return

    # handle the case where the start and end nodes are the same, set the distance to 0
    if middle_loop == inner_loop:
        GRAPH[middle_loop][inner_loop] = 0
    else:
        # update the shortest path by comparing the direct path with the path that has an intermediate node
        GRAPH[middle_loop][inner_loop] = min(GRAPH[middle_loop][inner_loop],
                                             GRAPH[middle_loop][outer_loop] + GRAPH[outer_loop][inner_loop])

    # Recursive steps that simulate the nested loops in the iterative version
    if inner_loop + 1 < MAX_LENGTH:
        # If the inner loop has not reached the end, increment the inner loop
        recursive_floyd_warshall(outer_loop, middle_loop, inner_loop + 1)
    else:
        # if the inner loop reaches the end, increment the middle loop and reset the inner loop
        if middle_loop + 1 < MAX_LENGTH:
            recursive_floyd_warshall(outer_loop, middle_loop + 1, MIN_LEVEL)
        else:
            # if the middle loop reaches the end, increment the outer loop and reset the middle and inner loops
            recursive_floyd_warshall(outer_loop + 1, MIN_LEVEL, MIN_LEVEL)


if __name__ == "__main__":
    main()
