# Посчитать четные и нечетные цифры введенного натурального числа. Например, если введено число 34560, в нем 3 четные
# цифры (4, 6 и 0) и 2 нечетные (3 и 5)

import sys


sum_memory = 0
n = int(input('Введите число: '))
sum_memory += sys.getsizeof(n)
print(sum_memory)

even, odd = 0, 0

while n > 0:
    if n % 2 == 0:
        even += 1
    else:
        odd += 1
    n = n // 10
print(sys.getsizeof(even))
sum_memory += sys.getsizeof(even)
print(sys.getsizeof(odd))
sum_memory += sys.getsizeof(odd)

print(f'Четных цифр: {even}, нечетных цифр: {odd}')
print(f'Выделено памяти под переменные: {sum_memory}')

# Не понравилась мне такая затея - слишком много getsizeof (запутаться можно)