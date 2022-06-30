# Kruskal's Algorithm for minimum spanning tree in a undirected graph
V = int(input("Enter the number of nodes : "))  # Number of nodes
G = []  # Graph
for i in range(1, V+1):  # Initializing the adjacency matrix
    # Input the elements of each rows of adjacency matrix
    row = list(map(int, input(f"Enter the elements of row {i} : ").split()))
    G.append(row)  # Appending the row to the matrix
d = {}  # Dictionary to store the parent of each node
for i in range(V):  # Initializing the dictionary
    for j in range(i, V):  # Initializing the dictionary
        if G[i][j] != 0:  # If the edge exists
            if G[i][j] not in d:  # If the edge is not in the dictionary
                d[G[i][j]] = [[i, j]]  # Add the edge to the dictionary
            else:  # If the edge is in the dictionary
                d[G[i][j]].append([i, j])  # Add the edge to the dictionary
d = dict(sorted(d.items()))  # Sorting the dictionary
print("Edge : Weight")
arr = []  # Array to store the edges
cost = []  # Array to store the weights of the edges
for i in d:  # For each edge
    for j in range(len(d[i])):  # For each node
        if d[i][j][0] not in arr and d[i][j][1] not in arr:  # If the node is not in the array
            arr.append(d[i][j][0])  # Add the node to the array
            arr.append(d[i][j][1])  # Add the node to the array
            cost.append(i)  # Add the weight of the edge to the array
            print(str(d[i][j][0])+" - "+str(d[i][j][1])+" : "+str(i))
        elif d[i][j][0] in arr and d[i][j][1] not in arr:  # If the one node is in the array
            arr.append(d[i][j][1])
            cost.append(i)
            print(str(d[i][j][0])+" - "+str(d[i][j][1])+" : "+str(i))
        elif d[i][j][0] not in arr and d[i][j][1] in arr:  # If the one node is in the array
            arr.append(d[i][j][0])
            cost.append(i)
            print(str(d[i][j][0])+" - "+str(d[i][j][1])+" : "+str(i))
        else:  # If both nodes are in the array
            continue
print("Total cost of the MST is :", sum(cost))  # Total cost of the MST
