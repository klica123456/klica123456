import sys
from collections import deque
from itertools import permutations

input = sys.stdin.readline

dzdydx = [(1, 0, 0), (-1, 0, 0), (0, 1, 0), (0, -1, 0), (0, 0, 1), (0, 0, -1)]

def rotate(new_arr, n, k, num):
    if n == 0 or n == 4:
        new_arr[num] = arr[num]
        return
    if k == n+1:
        return
    if k == 0:
        new_arr[num] = arr[num]
        rotate(new_arr, n, k + 1, num)
    else:
        new_arr2 = [[0] * 5 for _ in range(5)]
        for i in range(5):
            for j in range(5):
                new_arr2[j][4-i] = new_arr[num][i][j]
        new_arr[num] = new_arr2
        rotate(new_arr, n, k+1, num)

def bfs(sz, sy, sx, ez, ey, ex):
    global cnt
    queue = deque([(sz, sy, sx)])
    visited = [[[0]*5 for _ in range(5)] for _ in range(5)]
    visited[sz][sy][sx] = 1
    while queue:
        z, y, x = queue.popleft()
        for dz, dy, dx in dzdydx:
            nz = z + dz
            ny = y + dy
            nx = x + dx
            if 0<=nz<5 and 0<=ny<5 and 0<=nx<5 and not visited[nz][ny][nx] and res[nz][ny][nx] == 1:
                visited[nz][ny][nx] = visited[z][y][x] + 1
                if [nz, ny, nx] == [ez, ey, ex]:
                    cnt = visited[nz][ny][nx]-1
                    return
                queue.append((nz, ny, nx))
                

start = [(0, 0, 0), (0, 0, 4), (0, 4, 0), (0, 4, 4)]
end = [(4, 4, 4), (4, 4, 0), (4, 0, 4), (4, 0, 0)]
arr = list(list(list(map(int, input().split())) for _ in range(5)) for _ in range(5))
ans = 10e9
res = []
for i in range(4):
    for j in range(4):
        for k in range(4):
            for a in range(4):
                for b in range(4):
                    cnt = 0
                    new_arr = [[[0] * 5 for _ in range(5)] for _ in range(5)]
                    rotate(new_arr, i, 0, 0)
                    rotate(new_arr, j, 0, 1)
                    rotate(new_arr, k, 0, 2)
                    rotate(new_arr, a, 0, 3)
                    rotate(new_arr, b, 0, 4)
                    for li in permutations([0, 1, 2, 3, 4], 5):
                        res = []
                        for u in li:
                            res.append(new_arr[u])
                        for s in range(4):
                            sz, sy, sx = start[s]
                            ez, ey, ex = end[s]
                            if res[sz][sy][sx] == 0 or res[ez][ey][ex] == 0:
                                continue
                            bfs(sz, sy, sx, ez, ey, ex)
                            if cnt == 12:
                                print(12)
                                exit()
                            if cnt:
                                ans = min(cnt, ans)

if ans == 10e9:
    print(-1)
else:
    print(ans)