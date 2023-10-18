N, M = map(int, input().split())
arr = []
result = []
for i in range(1, N+1):
    arr.append(i)

for i in range(1<<N):
    k = []
    for j in range(N):
        if i & (1<<j):
            k.append(arr[j])
    result.append(k)


for i in sorted(result):
    if len(i) == M:
        print(*i)