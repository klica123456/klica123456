import sys

input = sys.stdin.readline

e1 = '0'+input()
e2 = '0'+input()
n1 = len(e1)-1
n2 = len(e2)-1
LCS = [[0]*n2 for _ in range(n1)]
for i in range(n1):
    for j in range(n2):
        if i == 0 or j == 0:
            LCS[i][j] = 0
        elif e1[i] == e2[j]:
            LCS[i][j] = LCS[i-1][j-1] + 1
        else:
            LCS[i][j] = max(LCS[i][j-1], LCS[i-1][j])
print(max(LCS[-1]))