import random

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