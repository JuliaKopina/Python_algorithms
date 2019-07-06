# Определение количества различных подстрок с использованием хеш-функции. Пусть на вход функции дана строка. Требуется
# вернуть количество различных подстрок в этой строке.
# Примечание: в сумму не включаем пустую строку и строку целиком.
# Пример работы функции:
# func("papa")
# 6
# func("sova")P
# 9
# import hashlib
import hashlib


def count_substr(string):
    h_subs = set()
    for i in range(len(string)):
        for j in range(1, len(string) + 1):
            if string[i:j]:
                h_subs.add(hashlib.sha1(string[i:j].encode('utf-8')).hexdigest())
    return len(h_subs) - 1


string = input(f'Введите, строку: ')
print(f'Количество подстрок в строке: {count_substr(string)}')
