from collections import Counter
from functools import reduce
# 1

print("Задача 1:")
dictionary_1 = {'a': 300, 'b': 400}
dictionary_2 = {'c': 500, 'd': 600}
dictionary_1.update(dictionary_2)
print(dictionary_1)

# 2
print("Задача 2:")
dict = {}
for i in range(1, 11):
    dict.update({i: i ** 3})
print(dict)

# 3
def search_max(dict):
    mx = -1
    for i in dict:
        mx = max(mx, dict[i])
    return mx
print("Задача 3:")
my_dict = {'a': 500, 'b': 5874, 'c': 560, 'd': 400, 'e': 5874, 'f': 20}
for j in range(3):
    for i in my_dict:
        if my_dict[i] == search_max(my_dict):
            print(i, ': ', my_dict.pop(i))
            break

# 4
def swap(a):
    ans = {}
    for i in a:
        ans.update({i[1]: i[0]})
    return ans
print("Задача 4:")
dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
dict = swap(dict.items())
print(dict)

# 5
print("Задача 5:")
dict1 = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
dict2 = {6: 'e', 7: 'd', 8: 'c', 9: 'b', 10: 'a'}
new_dict = {}
key = []
for i in dict1:
    key.append(dict1[i])
value = []
for i in dict2:
    value.append(dict2[i])
for i in range(len(key)):
    new_dict.update({key[i]: value[i]})
print(new_dict)

#6
print("Задача 6:")
str = 'pythonist'
dict = {}
for i in str:
    dict.update({i: str.count(i)})
print(dict)

#7
print("Задача 7:")
str = input('Введите строку: ')
dict = {}
for i in str:
    dict.update({i: str.count(i)})
print(dict)

#8

#9
print("Задача 9:")
city = input("Введите название городов: ").split()
country_city = []
city_in_country = {}
for i in range(5):
    x = input('Введите страну: ')
    y = input('Введите города в стране: ').split()
    for j in country_city:
        if j in y:
            city_in_country.update({j: x})
print(city_in_country)

#10
print("Задача 10:")
words = input('Введите текст: ').split()
ans = {}
for i in words:
    ans.update({i: words.count(i)})
print(ans)

#11
def inverse(a):
    ans = {}
    for i in a:
        ans.update({a[i]: i})
    return ans
print("Задача 11:")
dict = {1: 'a', 2: 'b', 3: 'c', 4: 'd', 5: 'e'}
dict = inverse(dict)
print(dict)

#12
print("Задача 12:")
school = {'1a': 10,
          '1b': 20,
          '2a': 30,
          '2b': 30,
          '3a': 20,
          '3b': 10,
          '4a': 15,
          '4b': 16,
          '4c': 25
          }
x = input('Введите класс: ')
y = input('Введите новое кол-во учеников')
school[x] = y
x = input('Введите новый класс: ')
y = input('Введите новое кол-во учеников')
school.update({x: y})
x = input('Введите класс для удаления: ')
school.pop(x)
ans = 0
for i in school:
    ans += school[i]
print(ans)

#13
def max_dct(*dicts):
    return dict(reduce(lambda a, b: Counter(a) | Counter(b), dicts))

print('Задача 13:')
d1 = {1: 11, 2: 33, 3: 10, 4: 10, 5: 2, 6: 90}
d2 = {1: 12, 3: 7, 4: 1, 5: 2, 7: 112}
d3 = max_dct(d1, d2)

#14
print('Задача 14:')
d = {'Group1': {'909890 В В В аовлав': {"Алгоритмизация и программирование": [5, 4, 3, 5],
                        'Информатика': [5, 4, 3, 5], 'Физкультура': [5, 4, 3, 5]},
                '909890 В ы В аовлав': {"Алгоритмизация и программирование": [5, 4, 3, 5],
                        'Информатика': [5, 4, 3, 5], 'Физкультура': [5, 4, 3, 5]},
                '909890 В ф В аовлав': {"Алгоритмизация и программирование": [5, 4, 3, 5],
                        'Информатика': [5, 4, 3, 5], 'Физкультура': [5, 4, 3, 5]}},
     'Group2': {'909890 В аф фы аовлав': {"Алгоритмизация и программирование": [5, 4, 3, 5],
                        'Информатика': [5, 4, 3, 5], 'Физкультура': [5, 4, 3, 5]},
                '909890 В йцу  аовлав': {"Алгоритмизация и программирование": [5, 4, 3, 5],
                        'Информатика': [5, 4, 3, 5], 'Физкультура': [5, 4, 3, 5]},
                '909890 В ауца ыв аовлав': {"Алгоритмизация и программирование": [5, 4, 3, 5],
                        'Информатика': [5, 4, 3, 5], 'Физкультура': [5, 4, 3, 5]}}}
for key in d:
    print(key + ': ')
    for key1 in d[key]:
        print('\t' + key1 + ': ')
        for key2 in d[key][key1]:
            print('\t\t' + key2 + ': '
                  + str(d[key][key1][key2][0]) + ' '
                  + str(d[key][key1][key2][1]) + ' '
                  + str(d[key][key1][key2][2]) + ' '
                  + str(d[key][key1][key2][3]))

#15
print('Задача 15:')
a = {1, 2, 3, 4, 5, 6}
b = {1, 2, 5, 6, 8, 10}
f = open('отчет.txt', 'w')
buff = a.copy()
f.write('Объединение: ' + str(buff.union(b)))
buff = a.copy()
f.write('\nПересечение: ' + str(buff.intersection(b)))
buff = a.copy()
f.write('\nРазность: ' + str(buff.difference(b)))
buff = a.copy()
f.write('\nПринадлежность: ' + str(buff.issuperset(b)))
f.close()
