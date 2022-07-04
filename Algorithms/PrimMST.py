# Prim's Algorithm for minimum spanning tree in a undirected graph
INF = 9999999
V = int(input("Enter the number of nodes : "))
G = []
for i in range(1, V+1):
    row = list(map(int, input(f"Enter the elements of row {i} : ").split()))
    G.append(row)
# create a array to track selected vertex
# selected will become true otherwise false
selected = [False] * V
# set number of edge to 0
no_edge = 0
# the number of egde in minimum spanning tree will be always less than(V - 1), where V is number of vertices in graph
# choose 0th vertex and make it true
selected[0] = True
# print for edge and weight
print("Edge : Weight")
cost=0
while (no_edge < V - 1):
    # For every vertex in the set S, find the all adjacent vertices, calculate the distance from the vertex selected at step 1.
    # if the vertex is already in the set S, discard it otherwise choose another vertex nearest to selected vertex at step 1.
    minimum = INF
    x = 0
    y = 0
    for i in range(V):
        if selected[i]:
            for j in range(V):
                if ((not selected[j]) and G[i][j]!=0):  
                    # not in selected and there is an edge
                    if minimum > G[i][j]:
                        minimum = G[i][j]
                        x = i
                        y = j
    print(str(x) + " - " + str(y) + " : " + str(G[x][y]))
    cost+=G[x][y]
    selected[y] = True
    no_edge += 1
print("Total cost of the MST is :",cost)