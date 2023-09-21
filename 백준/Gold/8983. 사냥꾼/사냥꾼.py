M, N, L = map(int, input().split()) # M 사대의 수, N, 동물의 수, L 사정거리
mx_axis = list(map(int, input().split())) # 사대 M개의 x좌표 값
ans = 0
for _ in range(N):
    a, b = map(int, input().split())
    if b > L:
        continue
    for i in mx_axis:
        if abs(i-a)+b <= L:
            ans += 1
            break
print(ans)