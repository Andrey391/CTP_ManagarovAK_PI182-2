from random import randint
N = randint(0, 100)
K = int(input("Угадайте целое число от 1 до 100:"))
while K != N:
    if K<=5:
        print("Вы проиграли. Было загадано:", N)
        break
    K=int(input("Повторите попытку:"))
    if K < N:
        print("Ваше число меньше, чем задумал компьютер")
    elif K > N:
        print("Ваше число больше, чем задумал компьютер")

    else:
        print("Вы угадали")

print(N)