# В одномерном массиве найти сумму элементов, находящихся между минимальным и максимальным элементами. Сами минимальный
# и максимальный элементы в сумму не включать

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

if min_elem > max_elem:
    min_elem, max_elem = max_elem, min_elem

sum_elem = 0
for i in range(min_elem + 1, max_elem):
    sum_elem += array[i]

print(f'Сумма элементов между минимальным и максимальным элементами: {sum_elem}')