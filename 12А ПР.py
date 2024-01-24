n = int(input('Введите натуральное число n: '))

def isPrime(n, step=2):
    if n == step:
        return True
    if n % step == 0:
        return False
    return isPrime(n, step+1)

if isPrime(n):
    print("Yes")
else:
    print("No")
