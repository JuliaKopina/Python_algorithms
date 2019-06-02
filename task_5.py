# Найти максимальный элемент среди минимальных элементов столбцов матрицы

import random

matrix = [[random.randint(10, 99) for _ in range(10)] for _ in range(5)]
for line in matrix:
    print(line)

min_column = matrix[0]

for line in matrix:
    for idx, item in enumerate(line):
        if min_column[idx] > item:
            min_column[idx] = item

max_elem = min_column[0]

print('\n''Минимальные элементы столбцов матрицы:')
for item in min_column:
    print(f'{item: > 4}', end='')
    if item > max_elem:
        max_elem = item

print('\n'f'Максимальный элемент среди минимальных элементов: {max_elem}')