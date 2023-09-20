def bfs(p):
    l = [p]
    while l:
        y, x = l.pop(0)
        visited[y][x] = 1
        if arr[y][x]:
            arr[y][x] = 'C'
            continue
        else:
            arr[y][x] = 'C'
            for i in dydx:
                dy, dx = i
                ny = y + dy
                nx = x + dx
                if 0<=ny<N and 0<=nx<N and not visited[ny][nx]:
                    visited[ny][nx] = 1
                    l.append((ny, nx))




dydx = [(1,1), (1,0), (1,-1), (-1, 1), (-1,0), (-1,-1), (0,1), (0,-1)]
T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(input()) for _ in range(N)]
    q = []
    visited = [[0]*N for _ in range(N)]
    ans = 0
    for i in range(N):
        for j in range(N):
            if arr[i][j] == '.':
                cnt = 0
                for k in dydx:
                    y, x = k
                    if 0<= i+y < N and 0<= j+x < N and arr[i+y][j+x] == '*':
                        cnt += 1
                arr[i][j] = cnt
                if not cnt:
                    q.append((i, j))
    for i in q:
        a, b = i
        if not arr[a][b]:
            ans += 1
            bfs((a, b))

    for i in range(N):
        for j in range(N):
            if arr[i][j] != 'C' and arr[i][j] != '*':
                ans += 1
    print(f"#{tc} {ans}")


