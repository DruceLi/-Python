def func(lst):
    lst[0], lst[-1] = lst[-1], lst[0]
    return lst

m = int(input('Введите длину массива: '))
A = []
for _ in range(m):
    A.append(input('Введите элемент массива: '))

print(A)
print(func(A))
