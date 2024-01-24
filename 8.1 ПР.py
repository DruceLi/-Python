n = [
        [1, 3, 5],
        [5, 7, 8],
        [11, 23, 2],
    ]

k = 2

print(list(map(lambda x: x / n[k][k], n[k])))
