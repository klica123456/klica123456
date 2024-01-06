import sys

input = sys.stdin.readline

def dfs():
    global ans
    l = 0
    stack = []
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 0:
                l += 1
                stack.append((i, j))
                visit[i][j] = 2
                while stack:
                    y, x = stack.pop()
                    for dy, dx in dydx:
                        ny = y + dy
                        nx = x + dx
                        if 0<=ny<N and 0<=nx<N and visit[ny][nx] == 0:
                            stack.append((ny, nx))
                            visit[ny][nx] = 2
    ans = max(ans, l)



N = int(input())
stack = []
res = list(list(map(int, input().split())) for _ in range(N))
visit = list([0]*N for _ in range(N))
ans = 1
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

for k in range(1, max(map(max, res))+1):
    for i in range(N):
        for j in range(N):
            if visit[i][j] == 2:
                visit[i][j] = 0
            if res[i][j] == k:
                visit[i][j] = 1

    dfs()

print(ans)