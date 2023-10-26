import sys

input = sys.stdin.readline

K, N = map(int, input().split())
arr = []
for _ in range(K):
    arr.append(int(input()))
start = 1
end = max(arr)+1
while start < end:
    mid = (start+end)//2
    cnt = sum(j//mid for j in arr)
    if cnt >= N:
        start = mid+1
    else:
        end = mid
print(end-1)
