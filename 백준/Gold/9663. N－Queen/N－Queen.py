def r(x):
    for i in range(x):
        if cnt[x] == cnt[i] or abs(cnt[x] - cnt[i]) == abs(x-i):
            return False
    return True

def s(k):
    global ans
    if n == k:
        ans += 1
        return
    for i in range(n):
        if not cnt[k]:
            cnt[k] = i
            if r(k):
                s(k+1)
            cnt[k] = 0


n = int(input())
cnt = [0] * n
ans = 0
s(0)
print(ans)