from collections import deque

def bfs_traversal(graph):
    # Initialize dictionaries and data structures for BFS
    visited = {}  # To keep track of visited nodes
    parent = {}   # To keep track of the parent of each node for finding the minimum distance
    level = {}    # To keep track of the level (distance) of each node from the source node

    # Initialize all nodes as unvisited, and parent and level as None and -1 respectively
    for node in graph.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    # Using deque for BFS traversal
    queue = deque()
    bfs_traversal_output = []  # To store the BFS traversal order

    # Start BFS from each unvisited node in the graph
    for source_node in graph.keys():
        if not visited[source_node]:
            visited[source_node] = True
            level[source_node] = 0
            queue.append(source_node)

            while queue:
                current_node = queue.popleft()
                bfs_traversal_output.append(current_node)

                # Explore all neighbors of the current node
                for neighbor in graph[current_node]:
                    if not visited[neighbor]:
                        visited[neighbor] = True
                        parent[neighbor] = current_node
                        level[neighbor] = level[current_node] + 1
                        queue.append(neighbor)

    return bfs_traversal_output, parent, level

# Graph represented by an adjacency list
adj_list = {
    "A": ["B", "D"],
    "B": ["C", "A"],
    "C": ["D", "B"],
    "D": ["A", "C", "G", "E"],
    "E": ["D", "F"],
    "F": ["E", "G"],
    "G": ["D", "F"],
    "X": ["Y"],
    "Y": ["X"]
}

bfs_traversal_output, parent_dict, level_dict = bfs_traversal(adj_list)

print("BFS Traversal:", bfs_traversal_output)
print("Parent Dictionary:", parent_dict)
print("Level Dictionary:", level_dict)
