# 3.1

print("Задача 1: \nЧисла от 1 до 15: ", end="")
for i in range(1, 16):
    print(i, end=" ")
print("\n")

# 3.2
print("Задача 2: \nЧетные числа от 2 до 20: ", end="")
for i in range(1, 11):
    print(i * 2, end=" ")
print("\n")

# 3.3
print("Задача 3: \nПеревод доллара в рубли от 1 до 20: ")
for i in range(1, 21):
    print(i, " - ", i * 75)
print()

# 3.4
print("Задача 4: \nТаблица стоимости конфет")
k = int(input("Введите стоимость 1кг: "))
print("кг|руб")
for i in range(2, 11):
    print(i, "|", i * k)
print("\n")

# 3.5
print("Задача 5: \nСумма чисел от 1 до 100: ", end="")
sum = 0
for i in range(1, 101):
    sum += i
print(sum)
print()

# 3.6
print("Задача 6: \nСр. ариф. от 1 до 100: ", end="")
print(sum / 100)
print()

# 3.7
print("Задача 7:")
n = int(input("Введите n: "))
s = 0
for i in range(1, n + 1):
    s += 1 / (i ** 5)
print("Ответ: ", s)
print()

# 3.8
print("Задача 8:")
n = int(input("Введите n: "))
s = 0
for i in range(1, n + 1):
    s += (2 * i - 1)/(i + 1)
print("Ответ: ", s)
print()

# 3.9
print("Задача 9:")
n = int(input("Введите n: "))
p = 1
for k in range(1, n + 1):
    p *= (1 + 1 / k)
print("Ответ: ", p)
