from collections import deque

def dfs(graph, start):
    visited = []
    stack = [start]
    
    while stack:
        n = stack.pop()
        if n not in visited:
            visited.append(n)
        _graph = graph[n].sort(reverse=True)
        for i in _graph:
            if i not in visited:
                stack.append(i)
    
    return " ".join(map(str, visited))

def bfs(graph, start):
    visited = []
    queue = deque([start])
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
        for i in graph[n]:
            if i not in visited:
                queue.append(i)
    
    return " ".join(map(str, visited))

N, M, root = map(int, input().split())

graph = [set() for _ in range(N+1)]
visited = [0 for _ in range(N+1)]

for _ in range(M):
    u, v = map(int, input().split())
    graph[u].add(v)
    
for _ in range(N+1):
    graph[_] = list(graph[_])
    graph[_].sort()
    
print(dfs(graph, root))
print(bfs(graph, root))



    