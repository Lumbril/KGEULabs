# 2.1
import math

print("Задача1. Максимум из 2х")
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))

if x > y:
    y = x

print('Ответ: максимум - ', y, '\n')

# 2.2

print("Задача2. Максимум из 3х")
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))

if y > x:
    x = y

if z > x:
    x = z

print('Ответ: максимум - ', x, '\n')

# 2.3

print("Задача3. Среднее из 3х")
x = int(input('Введите первое число: '))
y = int(input('Введите второе число: '))
z = int(input('Введите третье число: '))
mx = x
if y > mx:
    mx = y
if z > mx:
    mx = z
mn = x
if y < mn:
    mn = y
if z < mn:
    mn = z
print('Ответ: среднее - ', x + y + z - mn - mx, '\n')

# 2.4

x = int(input('Введите скорость в км/ч: '))
y = int(input('Введите скорость в м/с: '))
y *= 3.6
if x > y:
    print('Ответ: скорость в км/ч больше\n')
else:
    print('Ответ: скорость в м/с больше\n')

# 2.5

R = int(input('Введите радиус: '))
a = int(input('Введите сторону квадрата: '))
Sr = math.pi * R ** 2
Sa = a ** 2
if Sr > Sa:
    print('Ответ: площадь круга больше\n')
else:
    print('Ответ: площаль квадрата больше\n')

# 2.6
x = int(input('Введите x: '))
if x > 0:
    print('Ответ: y=2x-10=', 2 * x - 10, '\n')
elif x == 0:
    print('Ответ: y=0\n')
else:
    print('Ответ: y=2*|x|-1=', 2 * math.abs(x) - 1, '\n')

# 2.7
x = int(input('Введите число дня: '))

if x == 1:
    print('Ответ: понедельник\n')
elif x == 2:
    print('Ответ: вторник\n')
elif x == 3:
    print('Ответ: среда\n')
elif x == 4:
    print('Ответ: четверг\n')
elif x == 5:
    print('Ответ: пятница\n')
elif x == 6:
    print('Ответ: суббота\n')
else:
    print('Ответ: воскресенье\n')

# 2.8

x = input('Введите координату х: ')
y = input('Введите координату у: ')
if x > 0 & y > 0:
    print('Ответ: первая четверть\n')
elif x > 0 & y < 0:
    print('Ответ: четвертая четверть\n')
elif x < 0 & y < 0:
    print('Ответ: третья четверть\n')
elif x < 0 & y > 0:
    print('Ответ: вторая четверть\n')
else:
    print('Ответ: вы попали на оси\n')

# 2.9

m = input('Введите координату m: ')
n = input('Введите координату n: ')

if m == n:
    m = 0
    n = 0
    print('Ответ: числа заменены', m, ' ', n)
else:
    if m > n:
        n = m
    print('Ответ: числа заменены', m, ' ', n)