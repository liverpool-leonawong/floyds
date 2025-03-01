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
GRAPH = [[0,   7,  NO_PATH, 8],
         [NO_PATH,  0,  5,  NO_PATH],
         [NO_PATH, 5, 0, 2],
         [NO_PATH, NO_PATH, 2, 0]]
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
    # Base case: 如果 outer_loop 到達 MAX_LENGTH，停止遞迴
    if outer_loop >= MAX_LENGTH:
        return

    # 處理當前情況
    if middle_loop == inner_loop:
        GRAPH[middle_loop][inner_loop] = 0  # 起點同終點相同，距離為 0
    else:
        # 更新最短路徑
        GRAPH[middle_loop][inner_loop] = min(GRAPH[middle_loop][inner_loop],
                                             GRAPH[middle_loop][outer_loop] + GRAPH[outer_loop][inner_loop])

    # 遞迴步驟：模擬三層迴圈
    if inner_loop + 1 < MAX_LENGTH:
        # 如果 inner_loop 未到盡頭，繼續增加 inner_loop
        recursive_floyd_warshall(outer_loop, middle_loop, inner_loop + 1)
    else:
        # 如果 inner_loop 到咗盡頭，檢查 middle_loop
        if middle_loop + 1 < MAX_LENGTH:
            # 如果 middle_loop 未到盡頭，增加 middle_loop，重設 inner_loop
            recursive_floyd_warshall(outer_loop, middle_loop + 1, MIN_LEVEL)
        else:
            # 如果 middle_loop 到咗盡頭，增加 outer_loop，重設 middle_loop 同 inner_loop
            recursive_floyd_warshall(outer_loop + 1, MIN_LEVEL, MIN_LEVEL)

if __name__ == "__main__":
    main()
