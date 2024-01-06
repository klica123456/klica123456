import sys

input = sys.stdin.readline

def dfs(v, visited = []):
    visited.append(v) # 시작 정점 방문
    for w in graph[v]:
        if not w in visited: # 방문 하지 않았으면
            visited = dfs(w, visited)
    return visited


def bfs():
    q = [V]
    visit = [V]
    k = [V]
    while q:
        s = q.pop(0)
        for i in graph[s]:
            if i not in visit:
                visit.append(i)
                q.append(i)
                k.append(i)
    print(*k)


N, M, V = map(int, input().split())

graph = list([] for _ in range(N+1))


for _ in range(M):
    x, y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)

for i in graph:
    i.sort()

print(*dfs(V))
bfs()