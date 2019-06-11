# Написать два алгоритма нахождения i-го по счёту простого числа. Функция нахождения простого числа должна принимать на
# вход натуральное и возвращать соответствующее простое число. Проанализировать скорость и сложность алгоритмов

import timeit
import cProfile


def prime_sieve(n):
    sieve = [i for i in range(n ** 2)]
    sieve[1] = 0
    for i in range(2, len(sieve)):
        if sieve[i] != 0:
            j = i + i
            while j < len(sieve):
                sieve[j] = 0
                j += i
    res = [i for i in sieve if i != 0]
    return res[n - 1]

# python -m timeit -n 100 -s "import task_2"

# task_2.prime_sieve(10)
# 100 loops, best of 5: 60.5 usec per loop

# task_2.prime_sieve(20)
# 100 loops, best of 5: 324 usec per loop

# task_2.prime_sieve(30)
# 100 loops, best of 5: 739 usec per loop

# task_2.prime_sieve(100)
# 100 loops, best of 5: 9.43 msec per loop

# cProfile.run('prime_sieve(10)')
# 170    0.000    0.000    0.000    0.000 {built-in method builtins.len}   -10
# 789    0.000    0.000    0.000    0.000 {built-in method builtins.len}   -20
# 1897    0.000    0.000    0.000    0.000 {built-in method builtins.len}   -30
# 24299    0.003    0.000    0.003    0.000 {built-in method builtins.len}  -100
# 2853707    0.425    0.000    0.425    0.000 {built-in method builtins.len}  -1000

def prime(n):
    i = 2
    counter = 0
    while True:
        for j in range(2, i + 1):
            if i % j == 0:
                if i == j:
                    counter += 1
                break
        if counter == n:
            break
        i += 1
    return i

# python -m timeit -n 100 -s "import task_2"

# task_2.prime(10)
# 100 loops, best of 5: 31.7 usec per loop

# task_2.prime(20)
# 100 loops, best of 5: 109 usec per loop

# task_2.prime(30)
# 100 loops, best of 5: 224 usec per loop

# task_2.prime(100)
# 100 loops, best of 5: 2.83 msec per loop

# task_2.prime(1000)
# 100 loops, best of 5: 499 msec per loop

# cProfile.run('prime(10)'), ('prime(20)') и ('prime(30)')
# 1    0.000    0.000    0.000    0.000 <string>:1(<module>)
# 1    0.000    0.000    0.000    0.000 task_2.py:33(prime)
# 1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime(100)')
# 1    0.000    0.000    0.003    0.003 <string>:1(<module>)
# 1    0.003    0.003    0.003    0.003 task_2.py:33(prime)
# 1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# cProfile.run('prime(1000)')
# 1    0.000    0.000    0.513    0.513 <string>:1(<module>)
# 1    0.513    0.513    0.513    0.513 task_2.py:33(prime)
# 1    0.000    0.000    0.513    0.513 {built-in method builtins.exec}
# 1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

def test_prime(func):
    list_in = [2, 3, 4, 5, 6, 7, 8]
    list_out = [3, 5, 7, 11, 13, 17, 19]
    for i, item in enumerate(list_out):
        assert item == func(list_in[i])
        print(f'Test {item} OK')

# print(prime_sieve(100))
# print(prime(100))
# test_prime(prime_sieve)
# print('#' * 15)
# test_prime(prime)

"""
Функция prime работает быстрее, чем prime_sieve. Prime_sieve на 1000 не дал результатов (может не хватило терпения
дождаться, но было ощущение, что он просто подвис
"""