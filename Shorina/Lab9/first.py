#1
print("Задача 1:")
a = str(input("Введите символ: "))
print(ord(a))

#2
print("Задача 2:")
n = int(input("Введите число n: "))
print(chr(n))

#3
print("Задача 3:")
c = str(input("Введите символ: "))
print(chr(ord(c) - 1), chr(ord(c) + 1))

#4
print("Задача 4:")
n = int(input("Введите число n: "))
for i in range(n):
    print(chr(ord('A') + i), end=" ")

#5
print("Задача 5:")
n = int(input("Введите число n: "))
for i in range(n):
    print(chr(ord('z') - i), end=" ")

#6
print("Задача 6:")
c = str(input("Введите символ: "))
if 'a' <= c <= 'z' or 'A' <= c <= 'Z':
    print('lat')
elif 'а' <= c <= 'я' or 'А' <= c <= 'Я':
    print('rus')
else:
    print('digit')

#7
print("Задача 7:")
c = str(input("Введите строку: "))
print(ord(c[0]), ord(c[len(c - 1)]))

#8
print("Задача 8:")
n = int(input("Введите число n: "))
c = str(input("Введите символ: "))
s = c * n
print(s)

#9
print("Задача 9:")
c = str(input("Введите строку: "))
print(c[len(c) - 1:: -1])

#10
print("Задача 10:")
c = str(input("Введите строку: "))
s = ""
for i in range(len(c)):
    s += c[i] + " "
print(s)

#11
print("Задача 11:")
c = str(input("Введите строку: "))
n = int(input("Введите число n: "))
s = ""
for i in range(len(c)):
    s += c[i] + "*" * n
s = s[:len(s) - 3]
print(s)

#12
print("Задача 12:")
c = str(input("Введите строку: "))
ans = 0
for i in range(len(c)):
    if '0' <= c[i] <= '9':
        ans += 1
print(ans)

#13
print("Задача 13:")
c = str(input("Введите строку: "))
ans = 0
for i in range(len(c)):
    if 'A' <= c[i] <= 'Z':
        ans += 1
print(ans)

#14
print("Задача 14:")
c = str(input("Введите строку: "))
ans = 0
for i in range(len(c)):
    if 'a' <= c[i] <= 'z' or 'а' <= c[i] <= 'я':
        ans += 1
print(ans)

#15
print("Задача 15:")
c = str(input("Введите строку: "))
c = c.lower()
print(c)

#16
print("Задача 16:")
c = str(input("Введите строку: "))
c = c.swapcase()
print(c)

#17
print("Задача 17:")
c = str(input("Введите строку: "))
f = True
ff = 0
for i in range(len(c)):
    if not '0' <= c[i] <= '9':
        f = False
    if c[i] == '.':
        ff += 1
if f and ff == 1:
    print(2)
elif f and ff == 0:
    print(1)
else:
    print(0)

#18
print("Задача 18:")
c = str(input("Введите строку: "))
c = '+' + c
ans = 0
str = ""
i = 0
while i < len(c):
    if c[i] == '+':
        i += 1
        k = i
        while k < len(c) and '0' <= c[k] <= '9':
            str += c[k]
            k += 1
        i = k
        ans += int(str)
        str = ""
    elif c[i] == '-':
        i += 1
        k = i
        while k < len(c) and '0' <= c[k] <= '9':
            str += c[k]
            k += 1
        i = k
        ans -= int(str)
        str = ""
    else:
        i += 1
print(ans)

#19
print("Задача 19:")
n = int(input("Введите число n: "))
c = str(input("Введите строку: "))
if len(c) < n:
    c = '.' * (n - len(c)) + c
else:
    c = c[:n]
print(c)

#20
print("Задача 20:")
n1 = int(input("Введите число n1: "))
n2 = int(input("Введите число n2: "))
s1 = str(input("Введите строку s1: "))
s2 = str(input("Введите строку s2: "))
ans = s1[:n1] + s2[(len(s2) - n2):]
print(ans)

#21
print("Задача 21:")
c = str(input("Введите символ: "))
s = str(input("Введите строку: "))
ans = ""
for i in range(len(s)):
    ans += s[i]
    if s[i] == c:
        ans += s[i]
print(ans)

#22
print("Задача 22:")
c = str(input("Введите символ: "))
s = str(input("Введите строку s: "))
s0 = str(input("Введите строку s0: "))
ans = ""
for i in range(len(s)):
    if s[i] == c:
        ans += s0 + c
    else:
        ans += s[i]
print(ans)

#23
print("Задача 23:")
c = str(input("Введите символ: "))
s = str(input("Введите строку s: "))
s0 = str(input("Введите строку s0: "))
ans = ""
for i in range(len(s)):
    ans += s[i]
    if s[i] == c:
        ans += s0
print(ans)

#24
print("Задача 23:")
s = str(input("Введите строку s: "))
s0 = str(input("Введите строку s0: "))
if s0 in s:
    print(True)
else:
    print(False)
