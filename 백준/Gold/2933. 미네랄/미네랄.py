from collections import deque

def left(h):
    for i in range(C):
        if arr[R-h][i] == 'x':
            arr[R-h][i] = '.'
            break
    return

def right(h):
    for i in range(C-1, -1, -1):
        if arr[R-h][i] == 'x':
            arr[R-h][i] = '.'
            break
    return

def bfs():
    visited = [[0]*C for _ in range(R)]
    for i in range(R):
        for j in range(C):
            if arr[i][j] == 'x':
                visited[i][j] = 1
    for i in range(C):
        if visited[R-1][i] == 1:
            queue = deque([(R-1, i)])
            while queue:
                y, x = queue.popleft()
                for dy, dx in dydx:
                    ny = y + dy
                    nx = x + dx
                    if 0<=ny<R and 0<=nx<C and visited[ny][nx]:
                        visited[ny][nx] = 0
                        queue.append((ny, nx))
    '''
        떨어져야 하는 블록까지는 구했는데 떨어지는 코드와 언제까지 떨어져야되는지 함수 구현
    '''
    breaker = 0
    for i in visited:
        if 1 in i:
            breaker = 1

    if not breaker:
        return

    else:
        while True:
            fall = [[0] * C for _ in range(R)]
            for i in range(R - 1, -1, -1):
                for j in range(C):
                    if visited[i][j] == 1:
                        fall[i + 1][j] = 1
                        arr[i + 1][j] = 'x'
                        arr[i][j] = '.'
            visited = fall
            if stop(visited):
                break

def stop(visited):
    v = [0] * C
    for i in range(R-1, -1, -1):
        for j in range(C):
            if visited[i][j] == 1 and not v[j]:
                v[j] = 1
                if i == R-1:
                    return 1
                elif arr[i+1][j] == 'x':
                    return 1
    return 0



dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]

R, C = map(int, input().split())
arr = list(list(input()) for _ in range(R))
N = int(input())
H = list(map(int, input().split()))
for i in range(len(H)):
    if not i%2:
        left(H[i])
    else:
        right(H[i])
    bfs()
for i in arr:
    for j in i:
        print(j, end='')
    print()