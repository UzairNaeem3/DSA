def add_node(v):
    if v in graph:
        print(f"{v} is already present in the graph.")
        return 
    else:
        graph[v] = []

# Function for adding edge in undirected and unweighted graph                
def add_edge_undirected_unweighted(v1, v2):  # For adding edge we need two vertices
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the graph.")
    else:
        graph[v1].append(v2)
        graph[v2].append(v1)
        
# Function for adding edge in undirected and weighted graph 
def add_edge_undirected_weighted(v1, v2, cost):  # For adding edge we need two vertices
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the graph.")
    else:
        graph[v1].append([v2, cost])
        graph[v2].append([v1, cost])
        

# Function for adding edge in directed and weighted graph 
def add_edge_directed_weighted(v1, v2, cost):  # For adding edge we need two vertices
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the graph.")
    else:
        graph[v1].append([v2, cost])
        

def delete_node_unweighted(node):  # For unweigthed directed and unweighted undirected graph
    if node not in graph:
        print(f"{node} is not present in the graph.")
        return
    else: 
        graph.pop(node)
        for i in graph:
            list_ = graph[i]    
            if node in list_:
                list_.remove(node)
                
def delete_node_weighted(node):  # For weigthed directed and weighted undirected graph
    if node not in graph:
        print(f"{node} is not present in the graph.")
        return
    else: 
        graph.pop(node)
        for i in graph:
            list_ = graph[i]
            for j in list_:    
                if node == j[0]:
                    list_.remove(j)
                    break
                
                
def delete_edge_unweighted(v1,v2):  # For undirected and unweighted graph
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the graph.")
    else:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
            graph[v2].remove(v1)  # For directed and unweighted graph this line is not needed
            

def delete_edge_weighted(v1,v2, cost):  # For undirected and weighted graph
    if v1 not in graph:
        print(v1, "is not present in the graph.")
    elif v2 not in graph:
        print(v2, "is not present in the graph.")
    else:
        temp1 = [v1, cost]
        temp2 = [v2, cost]
        if temp2 in graph[v1]:
            graph[v1].remove(temp2)
            graph[v2].remove(temp1)  # For directed and weighted graph this line is not needed
                        
def DFS_iterative(node, graph):
    if node not in graph:
        print(node, "is not present in the graph.")
        return
    
    visited = set()
    stack = []
    stack.append(node)
    visited.add(node)
    
    while stack: # Loop until the stack is empty
        current_node = stack.pop()
        print(current_node)
        
        # loop through the neighbors of the current node
        for neighbor in graph[current_node]:
            # check if the neighbor is not visited
            if neighbor not in visited:
                stack.append(neighbor)
                visited.add(neighbor)
                

# For unweighted and undirected graph
def DFS_recursive(node, visited, graph):
    # Check if the graph is empty or None
    if not graph:
        raise ValueError("The graph cannot be empty or None.")
    
    # Check if the node is present in the graph
    if node not in graph:
        print(node, "is not present in the graph.")
        return
    
    # Check if the node has been visited
    if node not in visited:
        print(node)
        visited.add(node)
        for neighbor in graph[node]:
            DFS_recursive(neighbor, visited, graph)
                
             
    
    

            
visited = set()
graph = {}
add_node("A")
add_node("B")
add_node("C")
add_node("D")
add_node("E")

add_edge_undirected_unweighted("A","B")
add_edge_undirected_unweighted("B","E")
add_edge_undirected_unweighted("A","C")
add_edge_undirected_unweighted("A","D")
add_edge_undirected_unweighted("B","D")
add_edge_undirected_unweighted("C","D")
add_edge_undirected_unweighted("E","D")
print(graph)
print("Graph Traversal using DFS: ")
DFS_recursive("A", visited, graph)