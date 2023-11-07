import sys

input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
n = min(arr[0]+arr[1], arr[0]+arr[4], arr[1]+arr[5], arr[4]+arr[5])
cnt = N**3

if N == 1:
    print(sum(arr)-max(arr))

else:
    if arr[3] <= arr[2]:
        mi = min(arr[3]+arr[0]+arr[1], arr[3]+arr[1]+arr[5],
                 arr[3]+arr[4]+arr[5], arr[3]+arr[4]+arr[0])
        m = min(arr[3]+arr[0], arr[3]+arr[1], arr[3]+arr[4], arr[3]+arr[5])
    else:
        mi = min(arr[2] + arr[0] + arr[1], arr[2] + arr[1] + arr[5],
                 arr[2] + arr[4] + arr[5], arr[2] + arr[4] + arr[0])
        m = min(arr[2]+arr[0], arr[2]+arr[1], arr[2]+arr[4], arr[2]+arr[5])
    k = min(m, n)
    print(mi*4+k*(N-1)*4+k*(N-2)*4+(N-2)**2*min(arr)*5+(N-2)*4*min(arr))