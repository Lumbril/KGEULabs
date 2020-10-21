#1
a = int(input("Задача 1:\nВведите число: "))
print(True if a >= 0 else False)
print()

#2
a = int(input("Задача 2:\nВведите число: "))
b = int(input("Введите число: "))
print(True if a & 1 and b & 1 else False)
print()

#3
a = int(input("Задача 3:\nВведите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
print(True if a > 0 and b > 0 and c > 0 else False)
print()

#4
a = int(input("Задача 4:\nВведите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
print(True if a > 0 or b > 0 or c > 0 else False)
print()

#5
a = int(input("Задача 5:\nВведите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
print(True if (a > 0 > c and b < 0) or (a < 0 and b > 0 > c) or (a < 0 < c and b < 0) else False)
print()

#6
a = int(input("Задача 6:\nВведите число: "))
b = a % 10
a /= 10
c = a % 10
a /= 10
print(True if a != b and b != c and a != c else False)
print()

#7
a = int(input("Задача 7:\nВведите число: "))
b = a % 10
a //= 10
c = a % 10
a //= 10
d = a % 10
a //= 10
print(True if d == c and a == b else False)
print()

#8
x1 = int(input("Задача 8:\nВведите число x1: "))
y1 = int(input("Введите число y1: "))
x2 = int(input("Введите число x2: "))
y2 = int(input("Введите число y2: "))
print(True if (x1 + y1) & 1 == (x2 + y2) & 1 else False)
print()

#9
x1 = int(input("Задача 9:\nВведите число x1: "))
y1 = int(input("Введите число y1: "))
x2 = int(input("Введите число x2: "))
y2 = int(input("Введите число y2: "))
print(True if x1 == x2 or y1 == y2 else False)
print()

#10
x1 = int(input("Задача 10:\nВведите число x1: "))
y1 = int(input("Введите число y1: "))
x2 = int(input("Введите число x2: "))
y2 = int(input("Введите число y2: "))
print(True if abs(x1 - x2) == abs(y1 - y2) else False)
print()

#11
a = float(input("Задача 11:\nВведите число a: "))
b = float(input("Введите число: "))
if a > b:
    a, b = b, a
print("a = ", a, " b = ", b)
print()

#12
a = int(input("Задача 12:\nВведите число: "))
b = int(input("Введите число: "))
c = int(input("Введите число: "))
if a == b:
    print("Ответ: 3")
elif a == c:
    print("Ответ: 2")
else:
    print("Ответ: 1")
print()

#13
a = int(input("Задача 13:\nВведите число: "))
if a == 0:
    print("Нулевое число")
elif a > 0:
    if a & 1:
        print("Положительное нечетное число")
    else:
        print("Положительное четное число")
else:
    if a & 1:
        print("Отрицательное нечетное число")
    else:
        print("Отрицательное четное число")
print()

#14
a = int(input("Задача 14:\nВведите число: "))
if a < 10:
    if a & 1:
        print("Нечетное однозначное число")
    else:
        print("Четное однозначное число")
elif 9 < a < 100:
    if a & 1:
        print("Нечетное двузначное число")
    else:
        print("Четное двузначное число")
else:
    if a & 1:
        print("Нечетное трехначное число")
    else:
        print("Четное трехзначное число")
print()

#15
a = int(input("Задача 15:\nВведите число: "))
years = ["", "один ", "два ", "три ", "четыре ", "пять ", "шесть ", "семь ", "восемь ", "девять "]
dec = ["Двадцать ", "Тридцать ", "Сорок ", "Пятьдесят ", "Шестьдесят "]
b = a % 10
a //= 10
print(dec[a - 2], end="")
if b == 0 or b > 4:
    print(years[b], "лет")
elif 1 < b < 5:
    print(years[b], "года")
else:
    print(years[b], "год")
print()

#16
n = int(input("Задача 16:\nВведите число: "))
a = int(input("Введите число: "))
b = int(input("Введите число: "))
if n == 1:
    print("Сложение: ", a + b)
elif n == 2:
    print("Вычитание: ", a - b)
elif n == 2:
    print("Умножение: ", a * b)
else:
    print("Деление: ", a // b)
print()

#17
vec = ["С", "З", "Ю", "В"]
ch = input("Задача 17:\nВведите направление: ")
c = vec.index(ch)
n = int(input("Введите команду: "))
c += n
c = (c + n) % n
print("Новое направление: ", vec[c])
print()

#18
x1 = int(input("Задача 18:\nВведите число x1: "))
y1 = int(input("Введите число y1: "))
x2 = int(input("Введите число x2: "))
y2 = int(input("Введите число y2: "))
dx = abs(x1 - x2)
dy = abs(y1 - y2)
print(True if (dx == 1 and dy == 2) or (dx == 2 and dy == 1) else False)
print()

#19
ch = input("Задача 19:\nВведите направление: ")
c = vec.index(ch)
n = int(input("Введите команду: "))
c += n
n = int(input("Введите команду: "))
c += n
c = (c + n) % n
print("Новое направление: ", vec[c])
print()

#20
a = int(input("Задача 20:\nВведите число: "))
x = a // 100
if x == 1:
    print("Сто ", end="")
elif x == 2:
    print("Двести ", end="")
elif x == 3:
    print("Триста ", end="")
elif x == 4:
    print("Четыреста ", end="")
elif x == 5:
    print("Пятьсот ", end="")
elif x == 6:
    print("Шестьсот ", end="")
elif x == 7:
    print("Семьсот ", end="")
elif x == 8:
    print("Восемьсот ", end="")
else:
    print("Девятьсот ", end="")
x = a // 10 % 10
if x == 1:
    if a % 10 == 0:
        print("десять ", end="")
    elif a % 10 == 1:
        print("одиннацать ", end="")
    elif a % 10 == 2:
        print("двенадцать ", end="")
    elif a % 10 == 3:
        print("тринадцать ", end="")
    elif a % 10 == 4:
        print("четырнадцать ", end="")
    elif a % 10 == 5:
        print("пятьнадцать ", end="")
    elif a % 10 == 6:
        print("шестнадцать ", end="")
    elif a % 10 == 7:
        print("семнадцать ", end="")
    elif a % 10 == 8:
        print("восемнадцать ", end="")
    elif a % 10 == 9:
        print("девятнадцать ", end="")
elif x == 2:
    print("двадцать ", end="")
    if a % 10 == 1:
        print("один", end="")
    elif a % 10 == 2:
        print("два", end="")
    elif a % 10 == 3:
        print("три", end="")
    elif a % 10 == 4:
        print("четыре", end="")
    elif a % 10 == 5:
        print("пять", end="")
    elif a % 10 == 6:
        print("шесть", end="")
    elif a % 10 == 7:
        print("семь", end="")
    elif a % 10 == 8:
        print("восемь", end="")
    elif a % 10 == 9:
        print("девять", end="")
elif x == 3:
    print("тридцать ", end="")
    if a % 10 == 1:
        print("один", end="")
    elif a % 10 == 2:
        print("два", end="")
    elif a % 10 == 3:
        print("три", end="")
    elif a % 10 == 4:
        print("четыре", end="")
    elif a % 10 == 5:
        print("пять", end="")
    elif a % 10 == 6:
        print("шесть", end="")
    elif a % 10 == 7:
        print("семь", end="")
    elif a % 10 == 8:
        print("восемь", end="")
    elif a % 10 == 9:
        print("девять", end="")
elif x == 4:
    print("сорок ", end="")
    if a % 10 == 1:
        print("один", end="")
    elif a % 10 == 2:
        print("два", end="")
    elif a % 10 == 3:
        print("три", end="")
    elif a % 10 == 4:
        print("четыре", end="")
    elif a % 10 == 5:
        print("пять", end="")
    elif a % 10 == 6:
        print("шесть", end="")
    elif a % 10 == 7:
        print("семь", end="")
    elif a % 10 == 8:
        print("восемь", end="")
    elif a % 10 == 9:
        print("девять", end="")
elif x == 5:
    print("пятьдесят ", end="")
    if a % 10 == 1:
        print("один", end="")
    elif a % 10 == 2:
        print("два", end="")
    elif a % 10 == 3:
        print("три", end="")
    elif a % 10 == 4:
        print("четыре", end="")
    elif a % 10 == 5:
        print("пять", end="")
    elif a % 10 == 6:
        print("шесть", end="")
    elif a % 10 == 7:
        print("семь", end="")
    elif a % 10 == 8:
        print("восемь", end="")
    elif a % 10 == 9:
        print("девять", end="")
elif x == 6:
    print("шестьдесят ", end="")
    if a % 10 == 1:
        print("один", end="")
    elif a % 10 == 2:
        print("два", end="")
    elif a % 10 == 3:
        print("три", end="")
    elif a % 10 == 4:
        print("четыре", end="")
    elif a % 10 == 5:
        print("пять", end="")
    elif a % 10 == 6:
        print("шесть", end="")
    elif a % 10 == 7:
        print("семь", end="")
    elif a % 10 == 8:
        print("восемь", end="")
    elif a % 10 == 9:
        print("девять", end="")
elif x == 7:
    print("семьдесят ", end="")
    if a % 10 == 1:
        print("один", end="")
    elif a % 10 == 2:
        print("два", end="")
    elif a % 10 == 3:
        print("три", end="")
    elif a % 10 == 4:
        print("четыре", end="")
    elif a % 10 == 5:
        print("пять", end="")
    elif a % 10 == 6:
        print("шесть", end="")
    elif a % 10 == 7:
        print("семь", end="")
    elif a % 10 == 8:
        print("восемь", end="")
    elif a % 10 == 9:
        print("девять", end="")
elif x == 8:
    print("восемьдесят ", end="")
    if a % 10 == 1:
        print("один", end="")
    elif a % 10 == 2:
        print("два", end="")
    elif a % 10 == 3:
        print("три", end="")
    elif a % 10 == 4:
        print("четыре", end="")
    elif a % 10 == 5:
        print("пять", end="")
    elif a % 10 == 6:
        print("шесть", end="")
    elif a % 10 == 7:
        print("семь", end="")
    elif a % 10 == 8:
        print("восемь", end="")
    elif a % 10 == 9:
        print("девять", end="")
elif x == 9:
    print("девяносто ", end="")
    if a % 10 == 1:
        print("один", end="")
    elif a % 10 == 2:
        print("два", end="")
    elif a % 10 == 3:
        print("три", end="")
    elif a % 10 == 4:
        print("четыре", end="")
    elif a % 10 == 5:
        print("пять", end="")
    elif a % 10 == 6:
        print("шесть", end="")
    elif a % 10 == 7:
        print("семь", end="")
    elif a % 10 == 8:
        print("восемь", end="")
    elif a % 10 == 9:
        print("девять", end="")
print()

#21
animals = ["крысы", "коровы", "тигра", "зайца", "дракона", "змеи", "лошади", "овцы", "обезьяны", "курицы", "собаки", "свиньи"]
colors = ["зелен", "красн", "желт", "бел", "черн"]
a = int(input("Задача 21:\nВведите год: "))
b = abs(a - 1984) % 12
c = abs(a - 1984) % 5
print("год ", end="")
if animals[b] == "тигра" or animals[b] == "зайца" or animals[b] == "дракона":
    print(colors[c] + "ого", animals[b])
else:
    print(colors[c] + "ой", animals[b])
print()

#22
a = int(input("Задача 22:\nВведите день: "))
b = int(input("Введите месяц: "))
days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
if a == 1:
    b = (b - 1 + 12) % 12
    a = days[b]
    print(a, b)
else:
    print(a - 1, b)
print()

#23
a = int(input("Задача 23:\nВведите год: "))
if (a % 100 != 0 and a % 4 == 0) or (a % 400 == 0):
    print("365")
else:
    print("366")
