per_cent = {'ТКБ': 5.6, 'СКБ': 5.9, 'ВТБ': 4.28, 'СБЕР': 4.0}
money = int(input('Введите сумму - '))
deposit = list()
dict_value = list(dict.values(per_cent))
for i in range(len(dict_value)):
    deposit += [int(dict_value[i]*money/100)]
print(deposit)
print("Максимальная сумма, которую вы можете заработать — ", max(deposit))

