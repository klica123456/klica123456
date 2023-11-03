import sys # R 빨강, G 초록, B 파랑, P 보라, Y 노랑

from collections import deque
# 몇 연쇄가 되는지 출력
input = sys.stdin.readline
dydx = [(1, 0), (-1, 0), (0, 1), (0, -1)]
def bfs(s, y, x):
    q = deque([(y, x)])
    while q:
        y, x = q.popleft()
        for dy, dx in dydx:
            ny = y + dy
            nx = x + dx
            if 0<=nx<6 and 0<=ny<12 and not visited[ny][nx] and arr[ny][nx] == s:
                q.append((ny, nx))
                k.append((ny, nx))
                visited[ny][nx] = 1


arr = [list(input().rstrip()) for _ in range(12)]
ans = 0
while True:
    g = 0
    visited = [[0] * 6 for _ in range(12)]
    for i in range(12):
        for j in range(6):
            if not visited[i][j] and arr[i][j] != '.':
                visited[i][j] = 1
                k = [(i, j)]
                bfs(arr[i][j], i, j)
                if len(k) >= 4:
                    g = 1
                    for y, x in k:
                        arr[y][x] = '.'

    arr2 = [['.']*6 for _ in range(12)]

    for i in range(6):
        L = []
        for j in range(12):
            if arr[j][i] != '.':
                L.append(arr[j][i])
        for c in range(len(L)):
            arr2[11-c][i] = L[len(L)-c-1]

    arr = arr2
    if g == 0:
        print(ans)
        break
    else:
        ans += 1