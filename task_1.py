# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число

import timeit
import cProfile


def sum_(n):
    sum_n = sum([i for i in range(1, n+1)])
    return sum_n

# python -m timeit -n 100 -s "import task_1"

# task_1.sum_(10)
# 100 loops, best of 5: 2.17 usec per loop

# task_1.sum_(100)
# 100 loops, best of 5: 7.28 usec per loop

# task_1.sum_(1000)
# 100 loops, best of 5: 80.7 usec per loop

# cProfile.run('sum_(10)')
# 100 и 1000 то же самое
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task_1.py:5(sum_)
# 1    0.000    0.000    0.000    0.000 task_1.py:6(<listcomp>)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.sum}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def recurs_sum(n):
    if n == 1:
        return n
    return n + recurs_sum(n - 1)

# task_1.recurs_sum(10)
# 100 loops, best of 5: 2.98 usec per loop

# task_1.recurs_sum(100)
# 100 loops, best of 5: 32.9 usec per loop

# task_1.recurs_sum(1000)
# RecursionError: maximum recursion depth exceeded in comparison

# cProfile.run('recurs_sum(10)')
# 10/1    0.000    0.000    0.000    0.000 task_1.py:29(recurs_sum)  -10
# 100/1    0.000    0.000    0.000    0.000 task_1.py:30(recurs_sum)  -100
# 993/1    0.002    0.000    0.002    0.002 task_1.py:30(recurs_sum)  -1000

def cycle_sum(n):
    sum_n = 0
    for i in range(1, n + 1):
        sum_n += i
    return sum_n

# task_1.cycle_sum(10)
# 100 loops, best of 5: 1.46 usec per loop

# task_1.cycle_sum(100)
# 100 loops, best of 5: 9 usec per loop

# task_1.cycle_sum(1000)
# 100 loops, best of 5: 117 usec per loop

# cProfile.run('cycle_sum(10)')
# 100 и 1000 то же самое
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task_1.py:50(cycle_sum)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


def progr_sum(n):
    sum_n = n * (n + 1) / 2
    return sum_n

# task_1.progr_sum(10)
# 100 loops, best of 5: 357 nsec per loop

# task_1.progr_sum(100)
# 100 loops, best of 5: 413 nsec per loop

# task_1.progr_sum(1000)
# 100 loops, best of 5: 424 nsec per loop

# cProfile.run('progr_sum(1000)')
# 100 и 1000 то же самое
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task_1.py:73(progr_sum)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def test_sum(func):
    lst = [1, 3, 6, 10, 15, 21, 28, 36, 45]
    for i, item in enumerate(lst):
        assert item == func(i + 1)
        print(f'Test {item} OK')

# test_sum(sum_)
# print(sum_(100))
# print('#' * 15)
# test_sum(recurs_sum)
# print(recurs_sum(100))
# print('#' * 15)
# test_sum(cycle_sum)
# print(cycle_sum(100))
# print('#' * 15)
# test_sum(progr_sum)
# print(progr_sum(100))


"""
Мне кажется, выбрала не очень хорошую задачу((((
Функция sum_. При увеличении значений в 10 раз, время увеличилось в 3 раза, а при увеличении значений до 1000, время
увеличилось в 10 раз
 
recurs_sum и cycle_sum. При увеличении значений в 10 раз, время у обеих функций сразу выросло в 10 раз, но при
увеличении до 1000 - cycle_sum время продолжило расти в том же темпе, а recurs_sum отказалась работать

progr_sum. Время работы не меняется. Это наверно самый оптимальный - циклов и рекурский нет, обычные арифметические
действия
"""
