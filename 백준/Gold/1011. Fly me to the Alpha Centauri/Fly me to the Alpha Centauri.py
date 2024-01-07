import sys

input = sys.stdin.readline

for _ in range(int(input())):
    x, y = map(int, input().split()) # x : 현재 위치, y : 목표 위치
    dist = y - x
    # 속력을 늘려도 1씩 늘릴 수 있고, 줄여도 1씩 줄일 수 있다.
    # 아마 dp?
    ans = 0
    k = 0
    while k**2 <= dist:
        k += 1
    dist = dist - (k-1)**2
    ans += 2 * (k-1) - 1
    for i in range(k-1, 0, -1):
        q = 0
        if dist == 0:
            break
        q = dist // i
        ans += q
        dist -= q * i
    print(ans)