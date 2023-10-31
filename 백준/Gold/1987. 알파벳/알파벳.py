def dfs(arr, v, already, depth):
    global ans
    # visited랑 알파벳의 already랑 겹치기 때문에 필요 없음

    r, c = v
    stack = set()
    stack.add((r, c, already+arr[r][c], depth))

    while stack:
        y, x, nowalready, nowdepth = stack.pop()
        ans = max(ans, nowdepth)

        for i in range(4):
            ny, nx = y+dr[i], x+dc[i]
            if 0 <= ny < R and 0 <= nx < C and arr[ny][nx] not in nowalready:
                stack.add((ny, nx, nowalready + arr[ny][nx], nowdepth+1))
    return


R, C = map(int, input().split())
arr = [list(input()) for _ in range(R)]


ans = 0
dr = [0, 0, 1, -1]
dc = [1, -1, 0, 0]


dfs(arr, (0, 0), '', 1)


print(ans)