from math import *
#1
def DigitCountSum(k):
    s = 0
    c = 0
    while k != 0:
        c += 1
        s += k % 10
        k //= 10
    return c, s
print("Задача 1:")
for i in range(5):
    buf = DigitCountSum(int(input("Введите число: ")))
    print("Кол-во цифр - ", buf[0], " сумма - ", buf[1])
print()

#2
def AddRightDigit(d, k):
    d *= 10
    d += k
    return d
print("Задача 2:")
for i in range(2):
    x = int(input("Введите число: "))
    y = int(input("Введите цифру которое нужно добавить: "))
    print("Результат: ", AddRightDigit(x, y))
print()

#3
def AddLeftDigit(d, k):
    while len(str(d)) > len(str(k)):
        k *= 10
    k += d
    return k
print("Задача 3:")
for i in range(2):
    x = int(input("Введите число: "))
    y = int(input("Введите цифру которое нужно добавить: "))
    print("Результат: ", AddLeftDigit(x, y))
print()

#4
def Swap(x, y):
    return y, x
print("Задача 4:")
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = float(input("Введите число d: "))
a, b = Swap(a, b)
c, d = Swap(c, d)
b, c = Swap(b, c)
print("A - ", a, " B - ", b, " C - ", c, " D - ", d)
print()

#5
def Minmax(x, y):
    if x > y:
        x, y = y, x
    return x, y
print("Задача 5:")
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
c = float(input("Введите число c: "))
d = float(input("Введите число d: "))
a, b = Minmax(a, b)
c, d = Minmax(c, d)
b, d = Minmax(b, d)
a, c = Minmax(a, c)
print("Минимум - ", a, " максимум - ", d)
print()

#6
def SortDec3(a, b, c):
    mn = min(a, b, c)
    mx = min(a, b, c)
    mid = a + b + c - mn - mx
    return mx, mid, mn
print("Задача 6:")
for i in range(2):
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))
    a, b, c = SortDec3(a, b, c)
    print(a, " ", b, " ", c)
print()

#7
def ShiftRight3(a, b, c):
    return c, a, b
print("Задача 7:")
for i in range(2):
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))
    a, b, c = ShiftRight3(a, b, c)
    print(a, " ", b, " ", c)
print()

#8
def ShiftLeft3(a, b, c):
    return b, c, a
print("Задача 8:")
for i in range(2):
    a = float(input("Введите число a: "))
    b = float(input("Введите число b: "))
    c = float(input("Введите число c: "))
    a, b, c = ShiftLeft3(a, b, c)
    print(a, " ", b, " ", c)
print()

#9
def IsSquare(k):
    k = sqrt(k)
    if int(k) == k:
        return True
    else:
        return False
print("Задача 9:")
for i in range(10):
    a = float(input("Введите число: "))
    print(IsSquare(a))
print()

#10
def DigitCount(k):
    ans = 0
    while k != 0:
        ans += 1
        k //= 10
    return ans
print("Задача 10:")
for i in range(5):
    a = int(input("Введите число: "))
    print(DigitCount(a))
print()

#11
def DigitN(k, n):
    arr = []
    while k != 0:
        arr.append(k % 10)
        k //= 10
    if len(arr) < n:
        return -1
    else:
        return arr[n - 1]
print("Задача 11:")
for i in range(5):
    a = int(input("Введите число: "))
    b = int(input("Введите число: "))
    print(DigitN(a, b))
print()

#12
def Fact(n):
    res = 1
    for i in range(1, n):
        res *= i
    return res
print("Задача 12:")
for i in range(5):
    a = int(input("Введите число: "))
    print(Fact(a))
print()

#13
def Fact2(n):
    fact = 1
    while n > 1:
        fact *= n
        n -= 2
    return fact
print("Задача 13:")
for i in range(5):
    a = int(input("Введите число: "))
    print(Fact2(a))
print()

#14
def NOD2(a, b):
    while b > 0:
        a %= b
        a, b = b, a
    return a
print("Задача 14:")
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
c = int(input("Введите число c: "))
d = int(input("Введите число d: "))
print("НОД(A, B) = ", NOD2(a, b))
print("НОД(A, C) = ", NOD2(a, c))
print("НОД(A, D) = ", NOD2(a, d))
print()

#15
def IncTime(h, m, s, t):
    res = 3600 * h + 60 * m + s + t
    h = res // 3600
    res %= 3600
    m = res // 60
    res %= 60
    s = res
    return h, m, s
print("Задача 15:")
h = int(input("Введите число h: "))
m = int(input("Введите число m: "))
s = int(input("Введите число s: "))
t = int(input("Введите число t: "))
ans = IncTime(h, m, s, t)
print("Часы: ", ans[0], " минуты: ", ans[1], " секунды: ", ans[2])
print()

#16
def Calc(a, b, op):
    if op == 1:
        return a - b
    elif op == 2:
        return a * b
    elif op == 2:
        return a / b
    else:
        return a + b
print("Задача 16:")
a = float(input("Введите число a: "))
b = float(input("Введите число b: "))
for i in range(3):
    op = int(input("Введите число op: "))
    print(Calc(a, b, op))
