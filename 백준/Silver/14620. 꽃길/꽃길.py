# 씨앗을 심을 수 있는 곳을 탐색
# 씨앗심을 때 꽃이 죽지 않도록 상하좌우도 탐색
def bfs(k, min_v):
    global ans
    if k == 3:
        if ans > min_v:
            ans = min_v
        return
    for i in range(1, N-1):
        for j in range(1, N-1):
            v = 0
            for dy, dx in dydx:
                y = i + dy
                x = j + dx
                if not ground_visited[y][x]:
                    v = 1
                else:
                    v = 0
                    break
            if v:
                for dy, dx in dydx:
                    y = i + dy
                    x = j + dx
                    ground_visited[y][x] = 1
                    min_v += g_price[y][x]
                bfs(k+1, min_v)
                for dy, dx in dydx:
                    y = i + dy
                    x = j + dx
                    ground_visited[y][x] = 0
                    min_v -= g_price[y][x]


dydx = [(1, 0), (-1, 0), (0, 1), (0, -1), (0, 0)]
N = int(input())
g_price = [list(map(int, input().split())) for _ in range(N)]
ground_visited = [[0]*N for _ in range(N)]
ans = 1e9
bfs(0, 0)
print(ans)