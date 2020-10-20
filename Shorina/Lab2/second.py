# 4.1
print("Задача 1: \nЧисла от A до B: ")
a = int(input("Введите А: "))
b = int(input("Введите В: "))
a += 1
print("Ответ: ", end="")
while a < b:
    print(a, end=" ")
    a += 1
print()
print()

# 4.2
print("Задача 2: \nЧисла от А до В в порядке убывания: ")
a = int(input("Введите А: "))
b = int(input("Введите В: "))
b -= 1
print("Ответ: ", end="")
while b > a:
    print(b, end=" ")
    b -= 1
print()
print()

# 4.3
print("Задача 3: \nНатуральные числа от 1 до N: ")
n = int(input("Введите N: "))
i = 1
while i < n:
    print(i, end=" ")
    i += 1
print()
print()

# 4.4
print("Задача 4: \nНахождение квадрата > n")
n = int(input("Введите N: "))
i = 1
while i * i <= n:
    i += 1
print("Ответ: ", i)
print()

# 4.5
print("Задача 5: \nРассчет премии ")
a = int(input("Введите премию: "))
if a < 5000:
    print("Премия: ", a * .12)
elif a > 5000:
    print("Премия: ", a * .1)
print()

# 4.6
print("Задача 6: \nОпределение чет/нечет числа ")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
if a & 1 == 1:
    print("Первое число ", a, "нечет")
else:
    print("Второе число ", b, "нечет")
print()

# 4.7
print("Задача 7:\n Определение дня когда общее расстояние > 100км")
a = 10
i = 1
s = 10
while s < 100:
    a *= 1.1
    s += a
    i += 1
print("Ответ: ", i)
print()

# 4.8
print("Задача 8:\n Средняя оценка за семестр")
i = 1
s = 0
while i <= 6:
    s += int(input("Введите оценку: "))
    i += 1
print("Ответ: ", s / 6)
print()

# 4.9
print("Задача 9:\n Сумма всех нечет чисел от 1 до 99: ")
i = 1
s = 0
while i <= 99:
    s += i
    i += 2
print(s)