
try:
    x= int(input())
    if 1 >= x >= (10**9):
        raise ValueError()
except ValueError:
    print("Значение не корректно")
factorial = 1

for i in range(2, x + 1):
    factorial *= i

print(factorial)