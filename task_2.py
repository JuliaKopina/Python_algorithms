# Написать программу сложения и умножения двух шестнадцатеричных чисел. При этом каждое число представляется как массив,
# элементы которого — цифры числа. Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’,
# ‘F’] соответственно. Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’]

from collections import deque

hex_number = ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F')

dec_number = {'0': 0, '1': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9,
              'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}


def convert(hex_num):
    hex_num_deq = deque(hex_num)
    return hex_num_deq


def sum_hex(num1, num2):
    num1 = num1.copy()
    num2 = num2.copy()

    if len(num2) > len(num1):
        num1, num2 = num2, num1

    num2.extendleft('0' * (len(num1) - len(num2)))

    result = deque()
    overflow = 0
    for i in range(len(num1) - 1, -1, -1):
        first_num = dec_number[num1[i]]
        second_num = dec_number[num2[i]]

        result_num = first_num + second_num + overflow

        if result_num >= 16:
            overflow = 1
            result_num -= 16
        else:
            overflow = 0

        result.appendleft(hex_number[result_num])

    if overflow == 1:
        result.appendleft('1')

    return result


if __name__ == '__main__':
    a = input('Введите первое число (0-9, A-F): ')
    b = input('Введите второе число (0-9, A-F): ')

    a = convert(a)
    b = convert(b)

    print(list(a))
    print(list(b))

    print(f'Сумма чисел: {list(sum_hex(a, b))}')

# 496FA4
# 84B5D
# 51bb01
