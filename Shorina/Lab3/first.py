# 1
import math
import random

print("\tОтвет: колво КБ - ", int(input("Задача 1:\nВведите кол-во бит: ")) // 1024, "\n")

# 2
print("\tОтвет: колво отрезков B - ", int(input("Задача 2:\nВведите А: ")) // int(input("Введите B: ")), "\n")

#3
print("Задача 3:")
a = int(input("Введите 3х-значное число: "))
p = 1
s = 0
while a != 0:
    p *= a % 10
    s += a % 10
    a //= 10
print("\tОтвет: сумма - ", s, " произведение - ", p)
print()

#4
print("Задача 4:")
a = int(input("Введите 3х-значное число: "))
print("\tОтвет: ", end="")
while a != 0:
    print(a % 10, end="")
    a //= 10
print()
print()

#5
print("Задача 5:")
a = int(input("Введите 3х-значное число: "))
b = a % 100
a = b * 10 + a // 100
print("\tОтвет: ", a)
print()

#6
print("Задача 6:")
a = int(input("Введите 3х-значное число: "))
print("\tОтвет: ", (a // 100) * 100 + (a % 10) * 10 + ((a % 100) // 10))
print()

#7
print("Задача 7:")
a = int(input("Введите 3х-значное число: "))
x = a // 100
y = (a % 100) // 10
z = a % 10
mx = max(x, y, z)
mn = min(x, y, z)
mid = x + y + z - mx - mn
print("\tОтвет: ", mx * 100 + mid * 10 + mn)
print()

#8
print("Задача 8:")
a = int(input("Введите число > 999: "))
print("\tОтвет: ", a // 100 % 10)
print()

#9
print("Задача 9:")
a = int(input("Введите кол-во секунд: "))
print("\tОтвет: секунд - ", a % 60)
print()

#10
print("Задача 10:")
a = int(input("Введите кол-во секунд: "))
print("\tОтвет: минут - ", a // 60 % 60)
print()

#11
print("Задача 11:")
n = int(input("Введите максимальное число: "))
k = int(input("Введите кол-во попыток: "))
secret = random.randint(1, n)
x = int(input("Угадайте число: "))
while True:
    if x == secret:
        print("Вы выйграли!")
        break
    else:
        k -= 1
        if k == 0:
            print("Попытки закончились")
            break
        else:
            if x > secret:
                x = int(input("Загаданное число меньше, введите заново: "))
            if x < secret:
                x = int(input("Загаданное число больше, введите заново: "))
print()

#12
print("Задача 12:")
a = int(input("Введите число в 2ой СС: "))
ans = 0
i = 0
while a != 0:
    ans += math.pow(2, i) * (a % 10)
    i += 1
    a //= 10
print("\tОтвет: число в 10ой СС - ", ans)
print()

#13
print("Задача 13:")
a = int(input("Введите первое число в 2ой СС: "))
b = int(input("Введите второе число в 2ой СС: "))
ans = 0
i = 0
while a != 0:
    ans += math.pow(2, i) * (a % 10)
    i += 1
    a //= 10
a = ans
ans = 0
i = 0
while b != 0:
    ans += math.pow(2, i) * (b % 10)
    i += 1
    b //= 10
b = ans
a += b
ans = ""
while a != 0:
    ans = str(int(a % 2)) + ans
    a //= 2
print("\tОтвет: сумма - ", ans)
print()

#14
print("Задача 14:")
a = int(input("Введите число: "))
while a >= 10:
    buff = a
    sum = 0
    while buff != 0:
        sum += buff % 10
        buff //= 10
    a = sum
print("\tОтвет: ", a)
print()

#15
print("Задача 15:")
file = open('luckyNumbers.txt', 'w')
for a in range(0, 10):
    for b in range(0, 10):
        for c in range(0, 10):
            for d in range(0, 10):
                for e in range(0, 10):
                    for f in range(0, 10):
                        if a + b + c == d + e + f:
                            ans = str(a) + str(b) + str(c) + str(d) + str(e) + str(f)
                            file.write(ans + '\n')
file.close()
print()

#16
print("Задача 16:\n\tОтвет: Подходящие числа - ", end="")
for a in range(1, 10000000):
    buff = a
    sumf = 0
    while buff != 0:
        sumf += math.factorial(buff % 10)
        buff //= 10
    if a == sumf:
        print(a, end=" ")

#17
print("\tОтвет: ", hex(int(input("Задача 17: \nВведите 2чное число: "), 2))[2:])
print()

#18
print("\tОтвет: ", int(input("Задача 17: \nВведите 16чное число: "), 16))
print()

#19
print("Задача 19:")
a = int(input("Введите число: "))
b = int(input("Введите основание(2-9): "))
ans = ''
while a != 0:
    ans = str(a % b) + ans
    a //= b
print('Ответ: ', ans)
print()

#20
print("Задача 20:")
a = int(input('Введите номер дня: '))
days = ['Воскресенье', 'Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота']
print('Ответ: ', days[(a + 2) % 7])
print()

#21
print("Задача 21:")
a = int(input('Введите номер дня: '))
n = int(input('Введите номер начального дня: '))
print('Ответ: ', days[(a + (n % 7)) % 7])
print()

#22
print("Задача 22:")
a = int(input('Введите год: '))
value = a // 100
if a % 100 != 0:
    value += 1
print("Ответ: век - ", value)
print()

#11.1
print("Задача 11:")
n = int(input("Введите максимальное число: "))
k = int(input("Введите кол-во попыток: "))
secret = random.randint(1, n)
x = int(input("Угадайте число: "))
f = True
while k != 0:
    k -= 1
    if x == secret:
        print('Вы выйграли!')
        f = False
        k == 0
    elif x > secret and k != 0:
        x = int(input("Загаданное число меньше, введите заново: "))
    elif k != 0:
        x = int(input("Загаданное число больше, введите заново: "))
if f:
    print("Попытки закончились")
print()
