import numpy as np

#1
print("Задача 1:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    for j in range(n):
        a[i][j] = 10 * (i + 1)
print(a)

#2
print("Задача 2:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for j in range(n):
    for i in range(m):
        a[i][j] = 5 * (j + 1)
print(a)

#3
print("Задача 3:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
d = int(input("Введите число d: "))
a = [[0] * n for i in range(m)]
b = input("Введите список: ").split()
for i in range(m):
    a[i][0] = int(b[i])
    for j in range(1, n):
        a[i][j] = a[i][j - 1] + d
print(a)

#4
print("Задача 4:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
print(a[k - 1])

#5
print("Задача 5:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m):
    print(a[i][k - 1], end=" ")

#6
print("Задача 6:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(1, m, 2):
    print(a[i])

#7
print("Задача 7:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for j in range(0, n, 2):
    for i in range(m):
        print(a[i][j], end=" ")
    print()

#8
print("Задача 8:")
n = int(input("Введите число n: "))
a = [[1]]
for j in range(1, n):
    l = [0] * (len(a[j - 1]) + 1)
    for i in range(len(a[j - 1])):
        l[i] += a[j - 1][i]
    for i in range(len(a[j - 1])):
        l[i + 1] += a[j - 1][i]
    a.append(l)
print(a)

#9
print("Задача 9:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
sum = 0
mult = 1
for i in range(n):
    sum += a[k - 1][i]
    mult *= a[k - 1][i]
print("Sum: ", sum)
print("Mult: ", mult)

#10
print("Задача 10:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
sum = 0
mult = 1
for i in range(m):
    sum += a[i][k - 1]
    mult *= a[i][k - 1]
print("Sum: ", sum)
print("Mult: ", mult)

#11
print("Задача 11:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m):
    mn = a[i][0]
    for j in range(n):
        mn = min(mn, a[i][j])
    print(mn)

#12
print("Задача 12:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for j in range(n):
    mx = a[0][j]
    for i in range(m):
        mx = max(mx, a[i][j])
    print(mx)

#13
print("Задача 13:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
ans = []
for i in range(m):
    mn = a[i][0]
    for j in range(n):
        mn = min(mn, a[i][j])
    ans.append(mn)
mx = ans[0]
for i in range(len(ans)):
    mx = max(mx, ans[i])
print(mx)

#14
print("Задача 14:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for k in range(m):
    for l in range(n):
        mx = a[l][k]
        for i in range(k, m):
            for j in range(0, n):
                mx = max(mx, a[i][j])
        mn = a[l][k]
        for j in range(l, n):
            for i in range(0, m):
                mn = min(mn, a[i][j])
        if mn == mx:
            print(mn)

#15
print("Задача 15:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
k1 = int(input("Введите число k1: "))
k2 = int(input("Введите число k2: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
a[k1 - 1], a[k2 - 1] = a[k2 - 1], a[k1 - 1]
print(a)

#16
print("Задача 16:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
k1 = int(input("Введите число k1: "))
k2 = int(input("Введите число k2: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m):
    a[i][k1 - 1], a[i][k2 - 1] = a[i][k2 - 1], a[i][k1 - 1]
print(a)

#17
print("Задача 17:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m):
    posmin = 0
    posmax = 0
    for j in range(n):
        if a[i][j] < a[i][posmin]:
            posmin = j
        if a[i][j] > a[i][posmax]:
            posmax = j
    a[i][posmax], a[i][posmin] = a[i][posmin], a[i][posmax]
print(a)

#18
print("Задача 18:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for j in range(n):
    posmin = 0
    posmax = 0
    for i in range(m):
        if a[i][j] < a[posmin][j]:
            posmin = j
        if a[i][j] > a[posmax][j]:
            posmax = j
    a[posmax][j], a[posmin][j] = a[posmin][j], a[posmax][j]

#19
print("Задача 19:")
m = int(input("Введите число m: "))
a = [[0] * m for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
sum = 0
for i in range(m):
    sum += a[i][i]
print(sum)

#20
print("Задача 20:")
m = int(input("Введите число m: "))
a = [[0] * m for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
sum = 0
for i in range(m):
    sum += a[i][m - 1 - i]
print(sum / m)

#21
print("Задача 21:")
m = int(input("Введите число m: "))
a = [[0] * m for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += a[j][j - i]
    print(sum)

#22
print("Задача 22:")
m = int(input("Введите число m: "))
a = [[0] * m for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m):
    mn = a[i][0]
    for j in range(i, m):
        mn = min(mn, a[j][j - i])
    print(mn)

#23
print("Задача 23:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
ans = 0
for i in range(m):
    f = True
    for j in range(n):
        if a[i][j] & 1:
            f = False
    ans = i
print(ans)

#24
print("Задача 24:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
ans = 0
for i in range(m):
    check = set()
    for j in range(n):
        check.add(a[i][j])
    if len(check) == n:
        ans += 1
print(ans)

#25
print("Задача 25:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
minp = 0
maxp = 0
for i in range(m):
    for j in range(n):
        if a[i][j] > a[maxp][j]:
            maxp = i
        if a[i][j] < a[minp][j]:
            minp = i
a[minp], a[maxp] = a[maxp], a[minp]

#26
print("Задача 26:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
minp = 0
maxp = 0
for j in range(n):
    for i in range(m):
        if a[i][j] > a[i][maxp]:
            maxp = j
        if a[i][j] < a[i][minp]:
            minp = j
for i in range(m):
    a[i][maxp], a[i][minp] = a[i][minp], a[i][maxp]

#27
print("Задача 27:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m - 1):
    for l in range(i + 1, m):
        if a[i][0] > a[l][0]:
            for i in range(n):
                a[i][j], a[l][j] = a[l][j], a[i][j]
print(a)

#28
print("Задача 28:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for j in range(n - 1):
    for l in range(j + 1, n):
        if a[i][n - 1] < a[l][n - 1]:
            for i in range(m):
                a[i][j], a[l][j] = a[l][j], a[i][j]
print(a)

#29
print("Задача 29:")
m = int(input("Введите число m: "))
n = int(input("Введите число n: "))
k = int(input("Введите число k: "))
a = [[0] * n for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
ans = []
buf = [0] * n
for i in range(m):
    if i == k - 1:
        ans.append(buf)
    ans.append(a[i])
print(ans)

#30
print("Задача 30:")
m = int(input("Введите число m: "))
a = [[0] * m for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(1, m):
    for j in range(i):
        a[i][j] = 0
print(a)

#31
print("Задача 31:")
m = int(input("Введите число m: "))
a = [[0] * m for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m):
    for j in range(i + 1, m - i - 1):
        a[i][j] = 0
print(a)

#32
print("Задача 32:")
m = int(input("Введите число m: "))
a = [[0] * m for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
for i in range(m):
    for j in range(i, m):
        a[i][j], a[j][i] = a[j][i], a[i][j]
for i in range(m):
    for j in range(m):
        print(a[i][j], end=" ")
    print()

#33
print("Задача 33:")
m = int(input("Введите число m: "))
a = [[0] * m for i in range(m)]
for i in range(m):
    a[i] = input("Введите строку №" + str(i + 1) + ": ").split()
a = np.rot90(a, 3)
print(a)
