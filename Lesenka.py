Python 3.12.1 (tags/v3.12.1:2305ca5, Dec  7 2023, 22:03:25) [MSC v.1937 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> N = int(input("Введите N "))
Введите N 9
>>> if N > 9:
...     print('Так не пойдет, ожидаю число <= 9')
... else:
...     for i in range(1, N + 1):
...         print(*range(1, i + 1), sep='')
... 
1
12
123
1234
12345
123456
1234567
12345678
123456789
