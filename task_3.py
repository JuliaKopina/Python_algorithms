# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы

import random

SIZE = 10
MIN_ITEM = 0
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]

min_elem = 0
max_elem = 0

for i in range(SIZE):
    if array[i] < array[min_elem]:
        min_elem = i
    elif array[i] > array[max_elem]:
        max_elem = i

print(array)
print(f'Максимальный элемент в массиве - {array[max_elem]};\n'
      f'минимальный элемент - {array[min_elem]}')

b = array[min_elem]
array[min_elem] = array[max_elem]
array[max_elem] = b

for i in range(SIZE):
    print(array[i], end=' ')