# 5.1
import math

print("Задача 1: \nНахождение y: ")
x = int(input("Введите х: "))
if x <= -1:
    print("\ty = ", 1 / x ** 2)
elif -1 < x <= 2:
    print("\ty = ", x ** 2)
else:
    print("\ty = 4")
print()

# 5.2
print("Задача 2:")
x = int(input("Введите х: "))
y = int(input("Введите y: "))
z = 0
if x + y < 2:
    z = math.sqrt(x ** 2 + y ** 2)
elif x + y == 3 or x + y == 8:
    z = 2 * x * y
elif x + y >= 10:
    z = x - y
else:
    z = 2 * x + 3 * y
print("\tОтвет: ", 3 * (z ** 2) - 2 * z + 5)
print()

# 5.3
def sumNumber(a):
    s = 0
    while a != 0:
        s += a % 10
        a //= 10
    return s

print("Задача 3:")
s = 0
k = 1
while k <= 200:
    if sumNumber(k) == 13:
        s += 1
    k += 1
print("Ответ: ", s)
print()

# 5.4
print("Задача 4:")
a = int(input("Введите 3х-значное число: "))
p = 1
while a != 0:
    p *= a % 10
    a //= 10
print("\tОтвет: ", p)
print()

# 5.5
print("Задача 5:")
a = int(input("Введите число: "))
p = 1
k = 0
while a != 0:
    if a % 10 & 1 == 1:
        p *= a % 10
        k += 1
    a //= 10
print("\tОтвет: кол-во нечет чисел = ", k, end=" ")
if k == 0:
    print("произведение = 0")
else:
    print("произведение = ", p)
print()

# 5.6
print("Задача 6:")
a = int(input("Введите 3х-значное число: "))
p = 0
while a != 0:
    if a % 10 == 1:
        p = 1
    a //= 10
print("\tОтвет: число 1 ", ("присутствует" if p == 1 else "отсутсвует"))
print()

# 5.7
print("Задача 7:")
a = int(input("Введите число: "))
p = 0
while a != 0:
    p += 1
    a //= 10
print("\tОтвет: кол-во цифр = ", p)
print()

# 5.8
print("Задача 8:")
m = int(input("Введите число m: "))
s = 0
k = 0
while s <= m:
    s += k ** 2
    k += 1
print("\tОтвет: кол-во первых чисел - ", k)

# 5.10
print("Задача 10:")
a = int(input("Введите 3х-значное число: "))
p = 1
s = 0
while a != 0:
    p *= a % 10
    s += a % 10
    a //= 10
print("\tОтвет: сумма - ", s, " произведение - ", p)