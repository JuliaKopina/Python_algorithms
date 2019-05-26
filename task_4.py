# Напишите программу, доказывающую или проверяющую, что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число

n = int(input('Введите число: '))

left = 0
for i in range(1, n+1):
    left += i

right = n * (n + 1) // 2

if left == right:
    print(f'{left} = {right} - равенство верно')
else:
    print(f'{left} не равно {right} - равенство неверно')


