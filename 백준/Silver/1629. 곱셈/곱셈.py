def multi(a, b):
    if b == 1:
        return a%C
    else:
        temp = multi(a, b//2)
        if b%2:
            return (temp * temp * a % C)
        else:
            return (temp * temp % C)



import sys

A, B, C = map(int, sys.stdin.readline().split())
print(multi(A, B))