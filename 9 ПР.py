with open(r"C:\Users\Asus\Desktop\Прохоренко_ЗИТ23м_vvod.txt", encoding="utf-8") as f:
    matrix_in = [list(map(int, line.rstrip().split())) for line in f]


matrix_out = [[matrix_in[j][i]
               for j in range(len(matrix_in))] for i in range(len(matrix_in[0]))]


with open(r"C:\Users\Asus\Desktop\Прохоренко_ЗИТ23м_vivod.txt", 'wb') as f:
        # f.write('123'.encode("utf-8"))
     for line in matrix_out:
        x = ' '.join(map(str, line)) + '\n'
        f.write(x.encode("utf-8"))
