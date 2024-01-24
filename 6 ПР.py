list = [1, 2, 3]
list_sum = sum(list)

list_multiply = 1
for num in list:
    list_multiply *= num
print(f"Сумма: {list_sum}, произведение: {list_multiply}")

list_count = len(list)
mean = list_sum / list_count
list = [x if x != 0 else mean for x in list]
print(list)
