# BFS Traversal for any connected graph (every node must be reachable from the root node)
from collections import defaultdict
nodes = int(input("Enter the number of nodes : "))
matrix = []
for i in range(1, nodes+1):
    row = list(map(int, input(f"Enter the elements of row {i} : ").split()))
    matrix.append(row)
graph = defaultdict(list)
for i in range(nodes):
    for j in range(nodes):
        if matrix[i][j] != 0 and i != j:
            graph[i].append(j)
print(graph)
print("Vertices numbering starts from 0")
root = int(input("Enter the root node : "))
queue = [root]
visited = [root]
while queue:
    node = queue.pop(0)
    for n in graph[node]:
        if n not in visited:
            queue.append(n)
            visited.append(n)
print("Breadth First Search Traversal :", visited)

# time complexity: O(V+E)
# space complexity: O(V)
