# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа) для каждого
# предприятия. Программа должна определить среднюю прибыль (за год для всех предприятий) и отдельно вывести наименования
# предприятий, чья прибыль выше среднего и ниже среднего

from collections import namedtuple, defaultdict


def total_year(org):
    return org.qrt1 + org.qrt2 + org.qrt3 + org.qrt4


Company = namedtuple('Company', 'name qrt1 qrt2 qrt3 qrt4')
firm = []

num = int(input('Введите количество предприятий: '))
for i in range(num):
    name = (input(f'Введите название {i + 1}-ого предприятия: '))
    qrt1 = (int(input('Введите прибыль за 1-ый квартал: ')))
    qrt2 = (int(input('Введите прибыль за 2-ой квартал: ')))
    qrt3 = (int(input('Введите прибыль за 3-ий квартал: ')))
    qrt4 = (int(input('Введите прибыль за 4-ый квартал: ')))
    firm.append(Company(name, qrt1, qrt2, qrt3, qrt4))
# print(firm)

aver_profit = sum([total_year(org) for org in firm]) / len(firm)
print(f'Средняя прибыль за год для всех предприятий: {aver_profit}')

stat = defaultdict(list)
for org in firm:
    stat[total_year(org) > aver_profit].append(org.name)
print(f'Предприятия с прибылью выше среднего: {stat[True]}')
print(f'Предприятия с прибылью ниже среднего: {stat[False]}')
