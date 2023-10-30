import sys

input = sys.stdin.readline

def dfs(start):

    if len(temp) == M:
        print(*temp)
        return

    remember_me = 0
    for i in range(start, N):
        if remember_me != arr[i]:
            temp.append(arr[i])
            remember_me = arr[i]
            dfs(i)
            temp.pop()

N, M = map(int, input().split())

arr = sorted(list(map(int, input().split())))

temp = []

dfs(0)