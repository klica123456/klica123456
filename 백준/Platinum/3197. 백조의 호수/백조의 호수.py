import sys

from collections import deque

input = sys.stdin.readline

def dfs():
    while s1:
        y, x = s1.popleft()
        for dy, dx in dydx:
            ny = y+dy
            nx = x+dx
            if 0<=ny<N and 0<=nx<M and not visited[ny][nx]:
                if arr[ny][nx] == 'L':
                    return 1
                elif arr[ny][nx] == '.':
                    visited[ny][nx] = 1
                    s1.append((ny, nx))
                elif arr[ny][nx] == 'X':
                    s2.add((ny, nx))
    return 0

dydx = [(0, 1), (0, -1), (1, 0), (-1, 0)]

N, M = map(int, input().split())
visited = [[0]*M for _ in range(N)]
arr = [list((input().strip())) for _ in range(N)]
q = 0

day = 0
for i in range(N):
    for j in range(M):
        if arr[i][j] == 'L':
            q = (i, j)
            break
    if q:
        break
s1 = deque([q])
visited[q[0]][q[1]] = 1
s2 = set()
q1 = set()
q2 = set()
for i in range(N):
    for j in range(M):
        if arr[i][j] == '.' or arr[i][j] == 'L':
            for dy, dx in dydx:
                ny = dy+i
                nx = dx+j
                if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 'X':
                    q1.add((ny, nx))
q2 = q1
q1 = set()

while True:
    if dfs():
        print(day)
        break
    s1 = deque(list(s2))
    s2 = set()

    for y, x in q2:
        arr[y][x] = '.'
        for dy, dx in dydx:
            ny = y+dy
            nx = x+dx
            if 0<=ny<N and 0<=nx<M and arr[ny][nx] == 'X':
                q1.add((ny, nx))
    day += 1
    q2 = q1
    q1 = set()