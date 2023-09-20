G = int(input()) # 게이트의 수
P = int(input()) # 비행기의 수
visited = [0] * (G+1)
for i in range(G+1):
    visited[i] = (0, i)
ans = 0
for i in range(P): # 앞으로 들어올 비행기
    n = int(input())
    check = 0
    a, b = visited[n]
    for j in range(b, 0, -1):
        a, b = visited[j]
        if a != -1:
            visited[n] = (-1, j)
            visited[j] = (-1, b)
            ans += 1
            check = 1
            break
    if not check:
        break
print(ans)