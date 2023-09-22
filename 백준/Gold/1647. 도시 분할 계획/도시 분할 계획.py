import sys

input = sys.stdin.readline

def find_set(x):
    while x != p[x]:
        x = p[x]
    return x

def union(x, y):
    x = find_set(x)
    y = find_set(y)
    if x < y:
        p[y] = x
    else:
        p[x] = y

N, M = map(int, input().split())
edge = []
for _ in range(M):
    s, e, w = map(int, input().split())
    edge.append((w, s-1, e-1))
edge.sort()
p = [i for i in range(N)]
cnt = 0
total = 0

for w, s, e in edge:
    if find_set(s) != find_set(e):
        cnt += 1
        union(s, e)
        total += w
        end = w

print(total-end)

