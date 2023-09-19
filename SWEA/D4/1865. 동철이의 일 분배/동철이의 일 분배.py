def track(k, ans):
    global max_v
    if k == N:
        if max_v < ans:
            max_v = ans
        return
    if ans <= max_v:
        return
    else:
        for i in range(N):
            if not visited[i]:
                visited[i] = 1
                track(k+1, ans*arr[k][i]/100)
                visited[i] = 0
 
T = int(input())
for tc in range(1, T+1):
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]
    max_v = 0
    visited = [0]*N
    track(0, 1)
    print(f"#{tc} {format(max_v*100, '.6f')}")