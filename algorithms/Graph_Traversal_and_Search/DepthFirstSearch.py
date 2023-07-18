def dfs_traversal(graph):
    # Initialize dictionaries and data structures for DFS
    visited = {}  # To keep track of visited nodes
    parent = {}   # To keep track of the parent of each node for DFS tree construction

    # Initialize all nodes as unvisited and parent as None
    for node in graph.keys():
        visited[node] = False
        parent[node] = None

    dfs_traversal_output = []  # To store the DFS traversal order

    # Define the DFS function that performs the recursive DFS traversal
    def dfs(node):
        visited[node] = True
        dfs_traversal_output.append(node)

        # Explore all neighbors of the current node
        for neighbor in graph[node]:
            if not visited[neighbor]:
                parent[neighbor] = node
                dfs(neighbor)

    # Start DFS from each unvisited node in the graph
    for node in graph.keys():
        if not visited[node]:
            dfs(node)

    return dfs_traversal_output, parent




if __name__ == "__main__":
    # Example graph represented by an adjacency list
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

    dfs_traversal_output, parent_dict = dfs_traversal(adj_list)

    print("DFS Traversal:", dfs_traversal_output)
    print("Parent Dictionary:", parent_dict)
