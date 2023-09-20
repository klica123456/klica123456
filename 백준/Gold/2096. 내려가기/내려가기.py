N = int(input())
dp_max = [0, 0, 0]
dp_min = [0, 0, 0]
for i in range(N):
    arr = list(map(int, input().split()))
    dp_max = [arr[0]+max(dp_max[:2]), arr[1]+max(dp_max), arr[2]+max(dp_max[1:])]
    dp_min = [arr[0]+min(dp_min[:2]), arr[1]+min(dp_min), arr[2]+min(dp_min[1:])]
print(f"{max(dp_max)} {min(dp_min)}")