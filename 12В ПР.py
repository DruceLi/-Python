def getMax():
    x = int(input('Ввод числа: '))
    if (x==0):
        return 0
    y = getMax()
    if (x > y):
        return x
    return y

print(str(getMax()))
