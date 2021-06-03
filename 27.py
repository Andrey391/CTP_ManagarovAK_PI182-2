k = int(input("Введите число k: ").strip())
val = map(int, input("Введите k чисел, разделённые пробелом:\n> ").strip().split(" "))

vec = []

for el in values:
    for j in range(6):
        if j >= len(vec) or j == 5:
            break
        
        if el > vec[j]:
            vec.insert(j, el)
            break

    if j == 5 or j == len(vec):
        vec.append(el)

    if len(vec) > 5:
        vec.pop(0)

    for item in vec: print(item, end=" ")
    print()