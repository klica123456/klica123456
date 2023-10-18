import sys

input = sys.stdin.readline
N, M = map(int, input().rsplit())
memory = [0] + list(map(int, input().split()))
cost = [0] + list(map(int, input().split()))
dp = [[0] * (sum(cost) + 1) for _ in range(N+1)]
result = 1e9
for i in range(1, N+1):
    for j in range(sum(cost)+1):
        now_memory = memory[i]
        now_cost = cost[i]
        if j < now_cost:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j-now_cost] + now_memory, dp[i-1][j])
        if dp[i][j] >= M:
            result = min(result, j)

if M != 0:
    print(result)
else:
    print(0)