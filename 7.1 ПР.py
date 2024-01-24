def check_func(num):
    for n in str(num):
        if n == '0' or num % int(n):
            return False
    return True


n = int(input('Ведите n: '))

for i in range(1, n + 1):
    if check_func(i):
        print(i)
