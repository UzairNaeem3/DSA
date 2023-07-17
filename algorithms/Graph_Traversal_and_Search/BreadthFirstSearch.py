from collections import deque
def bfs_traversal(graph, source_node):
    visited = {}
    parent = {}
    level = {}

    for node in graph.keys():
        visited[node] = False
        parent[node] = None
        level[node] = -1

    # Using deque for BFS traversal
    queue = deque()
    bfs_traversal_output = []

    visited[source_node] = True
    level[source_node] = 0
    queue.append(source_node)

    while queue:
        current_node = queue.popleft()
        bfs_traversal_output.append(current_node)

        for neighbor in graph[current_node]:
            if not visited[neighbor]:
                visited[neighbor] = True
                parent[neighbor] = current_node
                level[neighbor] = level[current_node] + 1
                queue.append(neighbor)

    return bfs_traversal_output, parent, level


# Graph represented by an adjacency list
ADJ_LIST = {
    "A": ["B", "D"],
    "B": ["C", "A"],
    "C": ["D", "B"],
    "D": ["A", "C", "G", "E"],
    "E": ["D", "F"],
    "F": ["E", "G"],
    "G": ["D", "F"],
}

# Source Node: A
SOURCE_NODE = "A"

bfs_traversal_output, parent_dict, level_dict = bfs_traversal(ADJ_LIST, SOURCE_NODE)

print("BFS Traversal:", bfs_traversal_output)
print("Parent Dictionary:", parent_dict)
print("Level Dictionary:", level_dict)
