# 1
n = int(input("Задача 1:\nВведите число: "))
sum = 0
for i in range(1, 2 * n, 2):
    sum += i
    print(sum)
print()

# 2
n = int(input("Задача 2:\nВведите число: "))
sum = 0
k = 1
for i in range(1, n + 1):
    sum += k * (1 + i / 10)
    k *= -1
print("%.4f" % sum)
print()

# 3
a = float(input("Задача 3:\nВведите число: "))
n = int(input("Введите число: "))
if n == 1:
    print(a)
elif n == 2:
    print(1 + a)
else:
    sum = a
    for i in range(1, n - 1):
        sum *= 2
    sum += 2 * (n - 2)
    print(sum)
print()

# 4
n = int(input("Задача 4:\nВведите число: "))
fact = 1
for i in range(n):
    fact *= (i + 1)
print(fact)
print()

# 5
print("Задача 5:")
e = 1
fact = 1.0
for i in range(1, 11):
    fact *= i
    e += 1 / fact
print(e)
print()

# 6
x = int(input("Задача 6:\nВведите число: "))
n = float(input("Введите число: "))
fact = 1.0
ans = 1
for i in range(1, n + 1):
    fact *= i
    ans += (x ** 2 / fact)
print(ans)
print()

# 7
n = int(input("Задача 7:\nВведите число: "))
a1 = 1
a2 = 2
print(a1)
print(a2)
for i in range(2, n):
    k = (a1 + 2 * a2) / 3
    a1 = a2
    a2 = k
    print(a2)
print()

# 8
n = int(input("Задача 8:\nВведите число: "))
a1 = 1
a2 = 2
a3 = 3
print(a1)
print(a2)
print(a3)
for i in range(3, n):
    k = (a1 + a2 - 2 * a3)
    a1 = a2
    a2 = a3
    a3 = k
    print(a3)
print()

# 9
a = int(input("Задача 9:\nВведите число: "))
b = int(input("Введите число: "))
for i in range(a, b + 1):
    for j in range(i):
        print(i, end=" ")
    print()
print()

# 10
n = int(input("Задача 10:\nВведите число: "))
fact = 1
while n > 1:
    fact *= n
    n -= 2
print(fact)
print()

# 11
a = int(input("Задача 11:\nВведите число: "))
sum = 0
k = 1
while sum < a:
    sum += 1 / k
    k += 1
print(k, sum)
print()

# 12
n = int(input("Задача 12:\nВведите число: "))
f = False
while n > 0:
    if (n % 10) & 1:
        f = True
    n //= 10
print(f)
print()

# 13
n = int(input("Задача 13:\nВведите число: "))
f1 = 1
f2 = 1
while f1 + f2 < n:
    k = f1 + f2
    f1 = f2
    f2 = k
if f1 + f2 == n:
    print(True)
else:
    print(False)
print()

# 14
n = int(input("Задача 14:\nВведите число: "))
sum = 0
while n > 0:
    x = int(float(input("Введите число: ")) + .5)
    sum += x
    print(x)
    n -= 1
print(sum)
print()

# 15
n = int(input("Задача 15:\nВведите число: "))
sum = 0
i = 1
while n > 0:
    x = int(input("Введите число: "))
    if x & 1:
        sum += 1
        print(i)
    n -= 1
    i += 1
print(sum)
print()

# 16
k = int(input("Задача 16:\nВведите число: "))
n = int(input("Введите число: "))
f = False
while n > 0:
    x = int(input("Введите число: "))
    if x < k:
        f = True
    n -= 1
print(f)
print()

# 17
n = int(input("Задача 17:\nВведите число: "))
arr = input().split()
arr.append(int(arr[n - 1]) + 1)
i = 0
while i < n:
    if arr[i] != arr[i + 1]:
        print(arr[i], end=" ")
    i += 1
print()

# 18
n = int(input("Задача 18:\nВведите число: "))
arr = input().split()
sum = 0
l = 0
r = n - 1
lf = False
rf = False
while l < r:
    if int(arr[l] == 0):
        lf = True
    if int(arr[r] == 0):
        rf = True
    if lf:
        sum += arr[l]
    if rf:
        sum += arr[r]
    l += 1
    r -= 1
print(sum)
print()

# 19
k = int(input("Задача 19:\nВведите число: "))
n = int(input("Введите число: "))
sum = 0
i = 0
while i < k * n:
    i += 1
    x = int(input())
    sum += x
print(sum)
print()

# 20
k = int(input("Задача 20:\nВведите число: "))
n = int(input("Введите число: "))
sum = 0
i = 0
j = 0
while j < k:
    i += 1
    x = int(input())
    sum += x
    if i == n:
        print(sum)
        j += 1
        i = 0
print()

# 21
k = int(input("Задача 21:\nВведите число: "))
n = int(input("Введите число: "))
for i in range(k):
    arr = input().split()
    pos = 0
    for j in range(n):
        if arr[i] == 2:
            pos = i
            break
    print(pos)
print()

# 22
n = int(input("Задача 22:\nВведите число: "))
k = int(input("Введите число: "))
sum = 0
for i in range(k):
    arr = input().split()
    print(len(arr))
    sum += len(arr)
print(sum)
print()

# 23
k = int(input("Задача 23:\nВведите число: "))
val = 0
f = True
for j in range(k):
    arr = input().split()
    arr.pop()
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            f = not f
            break
    if f:
        val += 1
    f = not f
print(val)
print()

# 24
k = int(input("Задача 24:\nВведите число: "))
val = 0
f = True
for j in range(k):
    arr = input().split()
    arr.pop()
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            f = not f
            break
    if f:
        print(1)
    else:
        f = not f
        for i in range(1, len(arr)):
            if arr[i] > arr[i - 1]:
                f = not f
                break
        if f:
            print(-1)
        else:
            f = not f
            print(0)
print()

#25
n = int(input("Задача 25:\nВведите число: "))
res = 0
f = True
a = 0
b = 0
for i in range(n):
    x = float(input())
    if not ((b < a) and (a > r)) and not ((b > a) and (a < x) and (i > 2) and f):
        res = i
        f = False
print(res)
print()

#26
k = int(input("Задача 26:\nВведите число: "))
sum = 0
for j in range(k):
    arr = input().split()
    arr.pop()
    res = 0
    f = True
    a = 0
    b = 0
    for i in range(len(arr)):
        x = arr[i]
        if not ((b < a) and (a > r)) and not ((b > a) and (a < x) and (i > 2) and f):
            res = i
            f = False
    if res == 0:
        sum += 1
print(sum)
print()
