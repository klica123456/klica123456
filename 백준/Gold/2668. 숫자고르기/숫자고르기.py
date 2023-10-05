N = int(input())
p = [i for i in range(1, N+1)]
visited = [0] * N
k = []
for i in range(1, N+1):
    a = int(input())
    k.append(a)
p_visited = [0] * N
arr2 = []
for i in p:
    if p_visited[i-1]:
        continue
    visited = [0] * N
    arr1 = []
    breaker = 0
    if i == k[i-1]:
        visited[i-1] = 1
        arr2.append(i)
        continue
    visited[i-1] = 1
    l = k[i-1]
    arr1.append(i)
    while True:
        if i == l:
            break
        if visited[l-1]:
            breaker = 1
            break
        if not visited[l-1]:
            visited[l-1] = 1
            arr1.append(l)
            l = k[l-1]
    if breaker:
        continue
    else:
        for i in arr1:
            p_visited[i-1] = 1
            arr2 += [i]

print(len(arr2))
for i in sorted(arr2):
    print(i)