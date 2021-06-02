x1 = int(input())
x2 = int(input())
k = 1
c = x1
while k < x2:
    c *= x1
    k += 1
print(c)