try:
    x= int(input())
    if 2 >= x >= (10**9):
        raise ValueError()
except ValueError:
    print("Значение не корректно")
counter = 0
for i in range(1, x + 1):
    if x % i == 0:
        counter += 1
if counter == 2:
    print("Простое число")
elif counter == 1:
    print("Составное число")