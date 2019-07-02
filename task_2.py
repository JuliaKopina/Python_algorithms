# Отсортируйте по возрастанию методом слияния одномерный вещественный массив, заданный случайными числами на промежутке
# [0; 50). Выведите на экран исходный и отсортированный массивы.
import random


def merge(left, right):
    sort_arr = []
    i, j = 0, 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            sort_arr.append(left[i])
            i += 1
        else:
            sort_arr.append(right[j])
            j += 1
    sort_arr += left[i:] + right[j:]
    return sort_arr


def merge_sort(array):
    if len(array) < 2:
        return array
    elif len(array) == 2:
        if array[0] > array[1]:
            array[0], array[1] = array[1], array[0]
        return array
    else:
        arr_1 = array[:len(array) // 2]
        arr_2 = array[len(array) // 2:]
        return merge(merge_sort(arr_1), merge_sort(arr_2))


array = [round(random.uniform(0, 49.99), 2) for _ in range(10)]
print(f'Исходный массив: {array}')
print(f'Отсортированный массив: {merge_sort(array)}')
