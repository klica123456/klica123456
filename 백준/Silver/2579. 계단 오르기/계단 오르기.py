import sys
input = sys.stdin.readline

N = int(input())
dp = [0]*(N+1)
arr = [0]
for _ in range(N):
    arr.append(int(input()))
for i in range(1, N+1):
    if i == 1:
        dp[i] = arr[i]
    elif i == 2:
        dp[i] = dp[1] + arr[i]
    else:
        dp[i] = max(arr[i]+dp[i-2], arr[i-1]+arr[i]+dp[i-3])
print(dp[N])