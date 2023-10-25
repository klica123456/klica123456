import sys
from collections import deque

input = sys.stdin.readline

N, L = map(int, input().split())
arr = list(map(int, input().split()))
queue = deque()
for i in range(N):
    while queue and queue[-1][1] > arr[i]:
        queue.pop()
    queue.append((i, arr[i]))
    if queue[0][0] < i-L+1:
        queue.popleft()
    print(queue[0][1], end=' ')