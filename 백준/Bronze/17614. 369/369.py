a= int(input())
b = 0
for i in range(1, a + 1):
    s = str(i)
    d = s.count("3") + s.count("6") + s.count("9")
    b = b + d
print(b)