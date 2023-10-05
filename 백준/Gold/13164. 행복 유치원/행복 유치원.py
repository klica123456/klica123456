N, K = map(int, input().split())
arr = list(map(int, input().split()))
minus = []
for i in range(1, N):
    minus.append(arr[i]-arr[i-1])
minus.sort()
ans = 0
for i in range(N-K):
    ans += minus[i]
print(ans)