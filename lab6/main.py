a = float(input("Введите значение a: "))
b = float(input("Введите значение b: "))
c = float(input("Введите значение c: "))
discr = b**2 - 4*a*c
print("Дискриминант = "+str(discr))
if discr < 0:
    print("корней нет")
elif discr == 0:
    x = (-b / (2*a))
else:
    x1 = (-b+discr ** 0.5)
    x2 = (-b-discr ** 0.5)
    print("x1 = " + str(x1))
    print("x2 = " + str(x2))
