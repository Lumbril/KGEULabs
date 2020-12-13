#1
print("Задача 1:")
s = input("Введите строку s: ")
s0 = input("Введите строку s0: ")
print(s.count(s0))

#2
print("Задача 2:")
s = input("Введите строку s: ")
s0 = input("Введите строку s0: ")
s = s.replace(s0, '', 1)
print(s)

#3
print("Задача 3:")
s = input("Введите строку s: ")
s1 = input("Введите строку s1: ")
s2 = input("Введите строку s2: ")
s = s[::-1]
s1 = s1[::-1]
s2 = s2[::-1]
s = s.replace(s1, s2, 1)
s = s[::-1]
print(s)

#4
print("Задача 4:")
s = input("Введите строку s: ")
if s.count(' ') == 1:
    print('')
else:
    s = s[s.find(' ') + 1:s.find(' ', s.find(' ') + 1)]
    print(s)

#5
print("Задача 5:")
s = input("Введите строку s: ")
if s.count(' ') == 1:
    print('')
else:
    s = s[s.find(' ') + 1:s.rfind(' ', s.find(' ') + 1)]
    print(s)

#6
print("Задача 6:")
s = input("Введите строку s: ")
s = ' '.join(s.split())
print(s.count(' ') + 1)

#7
print("Задача 7:")
s = input("Введите строку s: ")
s = s.split()
k = 0
for i in s:
    if i[0].lower() == i[len(i) - 1].lower():
        k += 1
print(k)

#8
print("Задача 8:")
s = input("Введите строку s: ")
s = s.split()
k = 0
for i in s:
    if 'А' in i:
        k += 1
print(k)

#9
print("Задача 9:")
s = input("Введите строку s: ")
s = ' '.join(s.split())
print(s)

#10
print("Задача 10:")
s = input("Введите строку s: ")
s = s.split()
mn = len(s[0])
for i in s:
    mn = min(mn, len(s[i]))
print(mn)

#11
print("Задача 11:")
s = input("Введите строку s: ")
s = s.split()
for i in s:
    x = i[0]
    i = i.replace(x, '.')
    i = i.replace('.', x, 1)
    print(i, end=" ")

#12
print("Задача 12:")
s = input("Введите строку s: ")
s = s.split()
s = sorted(s)
print(s)

#13
print("Задача 13:")
s = input("Введите строку s: ")
k = 0
for i in s:
    if i in ['.', ',', '!', '?', ':', ';']:
        k += 1
print(k)

#14
print("Задача 14:")
s = input("Введите строку s: ")
k = 0
for i in s:
    if i in ['а', 'е', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я']:
        k += 1
print(k)

#15
print("Задача 15:")
s = input("Введите строку s: ")
l = s.rfind('/')
r = s.rfind('.')
print(s[l + 1:r])

#16
print("Задача 16:")
s = input("Введите строку s: ")
l = s.rfind('.')
print(s[l + 1:])

#17
print("Задача 17:")
s = input("Введите строку s: ")
if s.count('/') == 1:
    print('/')
else:
    l = s.find('/')
    r = s.find('/', l + 1)
    print(s[l + 1: r])

#18
print("Задача 18:")
s = input("Введите строку s: ")
ans = ""
for i in range(len(s)):
    if 'А' <= s[i] <= 'Я' or 'а' <= s[i] <= 'я':
        ans += chr(ord(s[i]) + 1)
print(ans)

#19
print("Задача 19:")
s = input("Введите строку s: ")
k = int(input("Введите число k: "))
ans = ""
for i in range(len(s)):
    if 'А' <= s[i] <= 'Я' or 'а' <= s[i] <= 'я':
        ans += chr(ord(s[i]) + k)
print(ans)

#20
print("Задача 20:")
s = input("Введите строку s: ")
k = int(input("Введите число k: "))
ans = ""
for i in range(len(s)):
    if 'А' <= s[i] <= 'Я' or 'а' <= s[i] <= 'я':
        ans += chr(ord(s[i]) - k)
print(ans)

#21
print("Задача 21:")
s = input("Введите строку s: ")
psp = []
f = True
buf = {')':'(', ']':'[', '}':'{'}
if s[0] in [')', ']', '}']:
    print(0)
else:
    for i in range(len(s)):
        if s[i] in ['(', '[', '{']:
            psp.append(s[i])
        if s[i] in [')', ']', '}']:
            x = psp.pop()
            y = buf[s[i]]
            if x != y:
                print(i)
                f = False
                break
    if f:
        if len(psp) == 0:
            print(0)
        else:
            print(-1)
