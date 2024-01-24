from math import atan, e, log

x = eval(input('Введите x: '))
y = eval(input('Введите y: '))
z = eval(input('Введите z: '))

res = (e**(abs(x-y)) * abs(x-y)**(x+y)) / (atan(x) + atan(z)) + (x**6 + log(y)**2)**(1/3)

print(round(res, 4))
