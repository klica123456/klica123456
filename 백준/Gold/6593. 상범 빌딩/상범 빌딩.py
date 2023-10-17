def bfs(i, j, k):
    visited[i][j][k] = 1
    queue.append((i, j, k))
    while queue:
        i, j, k = queue.pop(0)
        for dz, dy, dx in dzdydx:
            nz = i + dz
            ny = j + dy
            nx = k + dx
            if 0<=nz<L and 0<=ny<R and 0<=nx<C:
                if arr[nz][ny][nx] == '.' and not visited[nz][ny][nx]:
                    visited[nz][ny][nx] = visited[i][j][k] + 1
                    queue.append((nz, ny, nx))
                elif arr[nz][ny][nx] == 'E' and not visited[nz][ny][nx]:
                    return print(f'Escaped in {visited[i][j][k]} minute(s).')
    return print('Trapped!')

dzdydx = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, 0, 1), (0, -1, 0), (0, 0, -1)]

while True:
    L, R, C = map(int, input().split()) # L은 층, R은 행, C는 열
    if L == 0 and R == 0 and C == 0:
        break
    arr = list(list(list(input()) for _ in range(R+1)) for _ in range(L))
    visited = list(list([0]*C for _ in range(R)) for _ in range(L))
    queue = []
    for i in range(L):
        arr[i].remove([])
    for i in range(L):
        for j in range(R):
            for k in range(C):
                if arr[i][j][k] == 'S':
                    bfs(i, j, k)
                    break