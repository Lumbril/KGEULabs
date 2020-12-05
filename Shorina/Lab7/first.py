#1
print("Задача 1:")
n = int(input("Введите число n: "))
a = []
for i in range(n):
    a.append(2 * i + 1)
print(a)

#2
print("Задача 2:")
n = int(input("Введите число n: "))
a = int(input("Введите число a: "))
d = int(input("Введите число d: "))
arr = []
for i in range(n):
    arr.append(a + i * d)
print(arr)

#3
print("Задача 3:")
n = int(input("Введите число n: "))
a = int(input("Введите число a: "))
b = int(input("Введите число b: "))
arr = [a, b]
for i in range(2, n):
    arr.append(arr[i - 1] + arr[i - 2])
print(arr)

#4
print("Задача 4:")
n = int(input("Введите число n: "))
arr = input("Введите список: ").split()
k = 0
for i in range(n):
    if int(arr[i]) & 1:
        k += 1
        print(arr[i], end="")
print(k)

#5
print("Задача 5:")
n = int(input("Введите число n: "))
arr = input("Введите список: ").split()
k = 0
for i in range(10, -1, -1):
    if not(int(arr[i]) & 1):
        k += 1
        print(arr[i], end="")
print(k)

#6
print("Задача 6:")
n = int(input("Введите число n: "))
arr = list(input("Введите список: ").split())
print(arr[::2])

#7
print("Задача 7:")
a = input("Введите список: ").split()
i = 0
while a[i] > a[9] and i < 10:
    i += 1
if i == 10:
    print(0)
else:
    print(i)

#8
print("Задача 8:")
n = int(input("Введите число n: "))
arr = list(input("Введите список: ").split())
k = int(input("Введите число k: "))
l = int(input("Введите число l: "))
sum = 0
for i in range(k - 1, l + 1):
    sum += arr[i]
print(sum)

#9
print("Задача 9:")
n = int(input("Введите число n: "))
arr = list(input("Введите список: ").split())
k = int(input("Введите число k: "))
l = int(input("Введите число l: "))
sum = 0
for i in range(k - 1, l + 1):
    sum += arr[i]
sumOb = 0
for i in range(n):
    sumOb += arr[i]
print(sumOb - sum)

#10
print("Задача 10:")
n = int(input("Введите число n: "))
arr = list(input("Введите список: ").split())
f = True
for i in range(n - 1):
    if arr[i] & 1 == arr[i + 1] & 1:
        print(i)
        f = not f
        break
if f:
    print(0)

#11
print("Задача 11:")
n = int(input("Введите число n: "))
arr = list(input("Введите список: ").split())
arr = arr[::2]
mn = arr[0]
for i in range(len(a)):
    mn = min(mn, arr[i])
print(mn)

#12
print("Задача 12:")
n = int(input("Введите число n: "))
arr = list(input("Введите список: ").split())
k = 0
for i in range(1, n - 1):
    if arr[i - 1] < a[i] and a[i] > arr[i + 1]:
        print(i)
        k += 1
print(k)

#13
print("Задача 13:")
n = int(input("Введите число n: "))
arr = list(input("Введите список: ").split())
for i in range(1, n - 1):
    if arr[i - 1] > a[i] and a[i] < arr[i + 1]:
        print(arr[i])
        break

#14
print("Задача 14:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = list(input("Введите список: ").split())
c = []
for i in range(n):
    c.append(max(a[i], b[i]))
print(c)

#15
print("Задача 15:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = []
for i in range(n):
    if not a[i] & 1:
        b.append(a[i])
print(len(b))
print(b)

#16
print("Задача 16:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = a[1::2] + a[::2]
print(b)

#17
print("Задача 17:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = []
c = []
for i in range(n):
    if a[i] < 0:
        c.append(a[i])
    else:
        b.append(a[i])
print(len(b), b)
print(len(c), c)

#18
print("Задача 18:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = list(input("Введите список: ").split())
c = []
l = 0
r = 0
while l < 5 and r < 5:
    if a[l] < b[r]:
        c.append(a[l])
        l += 1
    else:
        c.append(b[r])
        r += 1
while l < 5:
    c.append(a[l])
    l += 1
while r < 5:
    c.append(b[r])
    r += 1

#19
print("Задача 19:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
k = int(input("Введите число k: "))
for i in range(n):
    a[i] += k
print(a)

#20
print("Задача 20:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
minpos = 0
maxpos = 0
for i in range(n):
    if a[minpos] > a[i]:
        minpos = i
    if a[maxpos] < a[i]:
        maxpos = i
a[maxpos], a[minpos] = a[minpos], a[maxpos]
print(a)

#21
print("Задача 21:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
for i in range(1, n, 2):
    a[i], a[i - 1] = a[i - 1], a[i];
print(a)

#22
print("Задача 22:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
minpos = 0
maxpos = 0
for i in range(n):
    if int(a[minpos]) > int(a[i]):
       minpos = i
    if int(a[maxpos]) < int(a[i]):
        maxpos = i
if minpos > maxpos:
    minpos, maxpos = maxpos, minpos
for i in range(minpos + 1, maxpos):
    a[i] = 0
print(a)

#23
print("Задача 23:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
for i in range(n - 1):
    a[i] = a[i + 1]
a[n - 1] = 0
print(a)

#24
print("Задача 24:")
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
a = list(input("Введите список: ").split())
a.pop(k - 1)
print(a)

#25
print("Задача 25:")
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
l = int(input("Введите число l: "))
a = list(input("Введите список: ").split())
a = a[:k - 1] + a[l:]
print(len(a))
print(a)

#26
print("Задача 26:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
i = 0
while i < len(a):
    if int(a[i]) & 1:
        a.pop(i)
    else:
        i += 1
print(len(a))
print(a)

#27
print("Задача 27:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
i = 0
while i < len(a):
    if i + 1 < len(a) and a[i] == a[i + 1]:
        a.pop(i + 1)
    else:
        i += 1
print(len(a))
print(a)

#28
print("Задача 28:")
n = int(input("Введите число n: "))
print("Введите список: ", end="")
a = {}
for i in range(n):
    x = int(input())
    if a.get(x) != None:
        a[x] += 1
    else:
        a[x] = 1
num = 0
mx = -1
for key in a:
    if a[key] > mx:
        mx = a[key]
        num = key
print(num)

#29
print("Задача 29:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
a = a[n // 2:] + a[:n // 2]
print(a)

#30
print("Задача 30:")
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
a = list(input("Введите список: ").split())
for j in range(k):
    t = a[n - 1]
    for i in range(n - 1, 0, -1):
        a[i] = a[i - 1]
    a[0] = t
print(a)

#31
print("Задача 31:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = {}
for i in range(n):
    if b.get(a[i]) != None:
        b[a[i]] += 1
    else:
        b[a[i]] = 1
i = 0
while i < len(a):
    if b[a[i]] < 3:
        a.pop(i)
    else:
        i += 1
print(len(a))
print(a)

#32
print("Задача 32:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
i = 0
while i < len(a):
    if i + 1 < len(a) and a[i] == a[i + 1]:
        a.pop(i)
    else:
        i += 1
print(len(a))
print(a)

#33
print("Задача 33:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = {}
for i in range(n):
    if b.get(a[i]) != None:
        b[a[i]] += 1
    else:
        b[a[i]] = 1
i = 0
while i < len(a):
    if b[a[i]] == 2:
        a.pop(i)
    else:
        i += 1
print(len(a))
print(a)

#34
print("Задача 34:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
minpos = 0
maxpos = 0
for i in range(n):
    if int(a[minpos]) > int(a[i]):
       minpos = i
    if int(a[maxpos]) < int(a[i]):
        maxpos = i
if minpos > maxpos:
    minpos, maxpos = maxpos, minpos
a = a[:minpos] + ['0'] + a[minpos: maxpos + 1] + ['0'] + a[maxpos + 1:]
print(a)

#35
print("Задача 35:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = list(range(0, n * 2))
for i in range(n):
    b[i] = a[i]
for i in range((n // 2) * 2 - 1, -1, -2):
    n += 1
    for j in range(n - 1, i, -1):
        b[j] = b[j - 1]
print(b[:n])

#36
print("Задача 36:")
n = int(input("Введите число n: "))
a = list(input("Введите список: ").split())
b = []
c = []
i = 0
while i < n - 1:
    p = 1
    while i < n - 1 and a[i] == a[i + 1]:
        p += 1
        i += 1
    b.append(p)
    c.append(a[i])
    i += 1
if a[n - 1] != a[n - 2]:
    b.append(1)
    c.append(a[n - 1])
print(b)
print(c)
