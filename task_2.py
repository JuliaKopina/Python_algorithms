# В массиве случайных целых чисел поменять местами минимальный и максимальный элементы
# Вариант 1

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
# мне кажется, что я тут что-то упустила.... Но все, сил больше нет читать документацию)))


SIZE = 10
MIN_ITEM = -100
MAX_ITEM = 100
array = [random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE)]
print(array)

idx_min = 0
idx_max = 0

for i in range(len(array)):
    if array[i] < array[idx_min]:
        idx_min = i
    elif array[i] > array[idx_max]:
        idx_max = i

array[idx_min], array[idx_max] = array[idx_max], array[idx_min]
print(array)

print(locals())
print(f'Выделено памяти под переменные: {get_size(locals())}')

# SIZE = 10: памяти 184
# SIZE = 100: памяти 544
# SIZE = 1000: памяти 4600
# SIZE = 10000: памяти 43900
# SIZE = 100000: памяти 412324
# SIZE = 1000000: памяти 4348824
# SIZE = 10000000: памяти 40764120
