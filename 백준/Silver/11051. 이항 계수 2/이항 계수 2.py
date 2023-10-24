def fato(n):
    global arr
    ans = 1
    if n == 1:
        return ans
    else:
        for i in range(2, n+1):
            ans *= i
            if not arr[i]:
                arr[i] = ans
        return ans

n, k = map(int, input().split())
arr = [0] * (n+1)
arr[0] = 1
arr[1] = 1
print(int(fato(n)//arr[k]//arr[n-k]%10007))