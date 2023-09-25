N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr_plus = []
arr_minus = []
for i in arr:
    if i > 0:
        arr_plus.append(i)
    else:
        arr_minus.append(i)
arr_minus.sort()
arr_plus.sort(reverse=True)
N_minus = len(arr_minus)
N_plus = len(arr_plus)
cnt_plus = 0
cnt_minus = 0
ans_plus1 = 0
ans_minus1 = 0
ans_plus2 = 0
ans_minus2 = 0
if N_minus == 0:
    for i in range(0, N_plus, M):
        ans_plus1 += arr_plus[i] * 2
    print(ans_plus1 - arr_plus[0])
    exit(0)
if N_plus == 0:
    for i in range(0, N_minus, M):
        ans_minus1 += abs(arr_minus[i]) * 2
    print(ans_minus1 - abs(arr_minus[0]))
    exit(0)
if len(arr_plus)%M == 0:
    cnt_plus = 1
if len(arr_minus)%M == 0:
    cnt_minus = 1

for i in range(0, N_plus, M):
    ans_plus1 += arr_plus[i]*2
for i in range(0, N_minus, M):
    ans_minus1 += abs(arr_minus[i])*2
# for i in range(N_plus-1, -1, -M):
#     if i-M+1 >= 0:
#         ans_plus2 += arr_plus[i-M+1]*2
#     else:
#         ans_plus2 += arr_plus[0] * 2
# for i in range(N_minus-1, -1, -M):
#     if i-M+1 >= 0:
#         ans_minus2 += abs(arr_minus[i-M+1])*2
#     else:
#         ans_minus2 += abs(arr_minus[0])*2
# print(ans_plus1, ans_minus1, ans_plus2, ans_minus2)

if cnt_plus and cnt_minus:
    if arr_plus[0] > abs(arr_minus[0]):
        ans = ans_plus1 + ans_minus1 - arr_plus[0]
    else:
        ans = ans_plus1 + ans_minus1 - abs(arr_minus[0])
elif not cnt_plus and cnt_minus:
    if arr_plus[0] > abs(arr_minus[0]):
        ans = ans_minus1 + ans_plus1 - arr_plus[0]
    else:
        print(1)
        ans = ans_plus1 + ans_minus1 - abs(arr_minus[0])
elif cnt_plus and not cnt_minus:
    if arr_plus[0] > abs(arr_minus[0]):
        ans = ans_plus1 + ans_minus1 - arr_plus[0]
    else:
        ans = ans_plus1 + ans_minus1 - abs(arr_minus[0])
else:
    if arr_plus[0] > abs(arr_minus[0]):
        ans = ans_minus1 + ans_plus1 - arr_plus[0]
    else:
        ans = ans_minus1 + ans_plus1 - abs(arr_minus[0])
print(ans)

