def permOut(usag, string, result, last, in, rtLeft):
    
    for k in usag:
        if (usag[k] - 1 > rtLeft):
            continue
        result[in] = k
        usages[k] += 1
        if last == in:
            print(''.join(result), end=' ')
        else:
            isRepeated = usages[k] > 1
            permOut(usag, string, result, last, in+1, rLeft - isRepeated)
    
        usag[k] -= 1
    

def start(n, string):

        usag = {}
        result = []
        for _ in range(n):
            result += ' '
        for char in string:
            usag[char] = 0
        permOut(usag, string, result, n-1, 0, n - len(string))
        print()

k = int(in("Введите k: "))
string = in("Введите символы: ")

start(n, string)