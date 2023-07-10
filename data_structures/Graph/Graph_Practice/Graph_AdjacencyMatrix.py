# Function for adding node in a graph
def add_node(node):
    global node_count
    if node in nodes:
        print(f"{node} is already present in the graph.")
        return
    else:
        node_count += 1
        nodes.append(node)
        for i in graph:
            i.append(0)
            
        temp = [0 for j in range(node_count)]
        graph.append(temp)

# Function for adding edge in undirected and unweighted graph        
def add_edge_undirected_unweighted(v1, v2):  # For adding edge we need two vertices
    if v1 not in nodes:
        print(v1, "is not present in the graph.")
    elif v2 not in nodes:
        print(v2, "is not present in the graph.")
    else:
        v1_index = nodes.index(v1)
        v2_index = nodes.index(v2)
        graph[v1_index][v2_index] = 1
        graph[v2_index][v1_index] = 1
        

# Function for adding edge in undirected and weighted graph 
def add_edge_undirected_weighted(v1, v2, cost):  # For adding edge we need two vertices
    if v1 not in nodes:
        print(v1, "is not present in the graph.")
    elif v2 not in nodes:
        print(v2, "is not present in the graph.")
    else:
        v1_index = nodes.index(v1)
        v2_index = nodes.index(v2)
        graph[v1_index][v2_index] = cost
        graph[v2_index][v1_index] = cost 
        

# Function for adding edge in directed and unweighted graph 
def add_edge_directed_unweighted(v1, v2):  # For adding edge we need two vertices
    if v1 not in nodes:
        print(v1, "is not present in the graph.")
    elif v2 not in nodes:
        print(v2, "is not present in the graph.")
    else:
        v1_index = nodes.index(v1)
        v2_index = nodes.index(v2)
        graph[v1_index][v2_index] = 1
        # graph[v2_index][v1_index] = 1 
        
def delete_node(node):
    global node_count
    if node not in nodes:
        print(node, "is not present in the graph.")
    else:
        index = nodes.index(node)
        node_count = node_count - 1
        nodes.remove(node)
        graph.pop(index)
        for i in graph:
            i.pop(index)
            
def delete_edge(v1, v2): # For weighted or unweighted it doesn't matter
    if v1 not in nodes:
        print(v1, "is not present in the graph.")
    elif v2 not in nodes:
        print(v2, "is not present in the graph.")
    else:
        v1_index = nodes.index(v1)
        v2_index = nodes.index(v2)
        graph[v1_index][v2_index] = 0
        graph[v2_index][v1_index] = 0   # For directed graph this line will be removed 
        

        
def print_graph():
    for i in range(node_count):
        for j in range(node_count):
            print(format(graph[i][j], "<5"), end=" ")
        print()
            
    
nodes = []
graph = []
node_count = 0
print("Before adding nodes:")
print("nodes: ", nodes)
print("graph:", graph, '\n')
add_node("A")
add_node("B")
add_node("C")
add_edge_directed_unweighted("B","C")
add_edge_directed_unweighted("A","B")
print("After adding nodes:")
print("nodes: ", nodes)
print("graph:", graph)
delete_node("A")
print("Graph after deleting:")
print("Graph: ", graph)
print_graph()
print("Nodes: ", nodes)
