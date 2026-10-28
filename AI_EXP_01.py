from collections import deque

def bfs(graph, start):
    visited = set()
    queue = deque([start])
    visited.add(start)

    print("BFS Traversal:", end=" ")

    while queue:
        vertex = queue.popleft()
        print(vertex, end=" ")

        for neighbor in graph[vertex]:
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

# Create graph
graph = {}

n = int(input("Enter the number of vertices: "))

for i in range(n):
    vertex = input(f"Enter vertex {i + 1}: ")
    neighbors = input(
        f"Enter adjacent vertices of {vertex} (space-separated): "
    ).split()
    graph[vertex] = neighbors

# Input starting vertex after graph is created
start = input("Enter the starting vertex: ")

print("\nGraph:", graph)

# Check if start vertex exists
if start in graph:
    bfs(graph, start)
else:
    print("Starting vertex not found in the graph.")