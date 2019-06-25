# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
# Вариант 2

import sys
import random


def get_size(obj):
    size = 0
    for j in obj:
        if j.startswith('_') or j.startswith('random') or j.startswith('sys') or j.startswith('get_size'):
            continue
        else:
            size += sys.getsizeof(obj[j])
    return size


SIZE = 10000000
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

min_num = min(array)
max_num = max(array)
idx_min = array.index(min_num)
idx_max = array.index(max_num)

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

print(locals())
print(f'Выделено памяти под переменные: {get_size(locals())}')

# SIZE = 10: памяти 198
# SIZE = 100: памяти 558
# SIZE = 1000: памяти 4614
# SIZE = 10000: памяти 43914
# SIZE = 100000: памяти 412336
# SIZE = 1000000: памяти 4348836
# SIZE = 10000000: памяти 40764132