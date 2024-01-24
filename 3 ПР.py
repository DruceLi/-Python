month_num = input("Введите номер месяца: ")
num = int(month_num)
if num in (1, 3, 5, 7, 8, 10, 12):
    print("В этом месяце 31 день")
elif num in (4, 6, 9, 11):
    print("В этом месяце 30 дней")
else:
    print("В этом месяце 28 или 29 дней")
