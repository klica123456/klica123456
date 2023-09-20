# 되는 것 중에 최소값을 더하고 아니면 큰 순서대로 차례대로 연결
# 안된다 해도 다음으로 넘어가서 연결해줌
# 코어갯수가 가장 많은 것이 우선 -> 그 다음 가장 작은 선의 길이
# k는 코어를 탐색해본 갯수, c는 연결된 코어 갯수
# 전선과 코어가 중간에 있으면 무시
dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]

def check(y, x):
    direction = [0, 0, 0, 0]
    for d in range(4):
        now_y, now_x = y, x
        length = 0
        while 0 < now_y < N-1 and 0 < now_x < N-1:
            length += 1
            now_y += dy[d]
            now_x += dx[d]
            if arr[now_y][now_x]:
                break
        else:
            direction[d] = length
    return direction

def connect(y, x, d):
    while 0 < y < N-1 and 0 < x < N-1:
        y += dy[d]
        x += dx[d]
        arr[y][x] ^= 1


def track(k, c, wire):
    global min_v, l
    if k == cnt:
        if l < c:
            l = c
            min_v = wire
        elif l == c:
            if min_v > wire:
                min_v = wire
        return
    y, x = core[k][0], core[k][1]
    direction = check(y, x)
    for d in range(4):
        if direction[d] == 0:
            continue
        connect(y, x, d)
        track(k+1, c+1, wire+direction[d])
        connect(y, x, d)
    track(k+1, c, wire)



T = int(input())

for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    cnt = 0
    core = []
    for i in range(N):
        for j in range(N):
            if arr[i][j] == 1:
                if i == 0 or j == 0 or i == N-1 or j == N-1:
                    arr[i][j] = 2
                else:
                    core.append([i, j])
                    cnt += 1
    min_v = 10000000000000
    l = 0
    track(0, 0, 0)
    print(f"#{tc} {min_v}")