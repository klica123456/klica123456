M, N, L = map(int, input().split()) # M 사대의 수, N, 동물의 수, L 사정거리
mx_axis = list(map(int, input().split())) # 사대 M개의 x좌표 값
mx_axis.sort()
animal = [tuple(map(int, input().split())) for _ in range(N)]
animal.sort()
ans = 0
k = 0
for a, b in animal:
    if b > L:
        continue
    for i in range(k, len(mx_axis)):
        if abs(mx_axis[i]-a)+b <= L:
            k = i
            ans += 1
            break
print(ans)

