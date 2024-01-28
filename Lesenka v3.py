def lesenka(N):
    if N > 9:
        print('Так не пойдет, ожидаю число <= 9')
    else:
        for i in range(1, N + 1):
            print(*range(1, i + 1), sep='')

lesenka(int(input("Введите N ")))
