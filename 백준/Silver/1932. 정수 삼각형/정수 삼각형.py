import sys
input = sys.stdin.readline
n = int(input())
dp = [list(map(int, input().split())) for _ in range(n)]
ans = [[0] * n for n in range(1, n+1)]
ans[0][0] = dp[0][0]
for i in range(1, n):
    for j in range(len(dp[i])):
        if j == 0:
            ans[i][j] = ans[i-1][j] + dp[i][j]
        elif j == len(dp[i])-1:
            ans[i][j] = ans[i-1][j-1] + dp[i][j]
        else:
            ans[i][j] = max(ans[i-1][j-1], ans[i-1][j]) + dp[i][j]
print(max(ans[n-1]))