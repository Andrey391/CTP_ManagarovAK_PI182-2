def getNum():
    return 37
def get_k():
    return 12
count = {}
rApp = {}
for i in range(getNum()):
    count[j] = rApp[i] = 0
higNumber = roundNow = reds = blacks = 0
while (True):
    roundNow += 1
    inputt = int(input())
    if inputt < 0:
        break
    count[inputt] += 1
    rApp[inputt] = roundNow
    higNum = max(count.values())
    for i in range(getNum()):
        if count[i] == higNum:
            print(i, end = ' ')
    print()
    for i in range(getNumbers()):
        if rApp[i] == 0 or roundNow-roundAppear[i]>get_k():
            print(i, end = ' ')
    print()
    if inpt != 0:
        if inputt <= 10 or (inputt > 18 and inpt <= 28):
            if inputt % 2 == 1: reds += 1
            else:             blacks += 1
        else:
            if inputt % 2 == 0: reds += 1
            else:             blacks += 1
    print(reds,blacks,'\n')