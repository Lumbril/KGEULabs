import os

#1
print("Задача 1:")
s = input("Введите строку: ")
f = True
for i in s:
    if i in ['\\', '/', ':', '*', '?', '"', '>', '<', '|', '+']:
        f = False
if s[len(s) - 1] == ' ':
    f = False
if s.count('.') == 2:
    f = False
if f:
    f = open(s, 'w')
    f.write('asdas')
    f.close()
    print(True)
else:
    print(False)

#2
print("Задача 2:")
s = input("Введите имя файла: ")
n = input("Введите число n: ")
f = open(s, 'w')
for i in range(n):
    f.write(2 * (i + 1))
f.close()

#3
print("Задача 3: ")
s = input("Введите имена файлов через пробел: ").split()
lst = os.listdir(path='.')
k = 0
for i in s:
    if i in lst:
        k += 1
print(k)

#4
print("Задача 4: ")
s = input("Введите имя файла: ")
if not s in os.listdir(path='.'):
    print(-1)
else:
    f = open(s, 'r')
    ans = []
    for line in f:
        ans += line.split()
    f.close()
    print(len(ans))

#5
print("Задача 5: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
print(ans[0], ans[1], ans[len(ans) - 2], ans[len(ans) - 1])

#6
print("Задача 6: ")
s1 = input("Введите имя первого файла: ")
s2 = input("Введите имя второго файла: ")
f = open(s1, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
f = open(s2, 'w')
ans = ans[::-1]
for i in ans:
    f.write(i, ' ')
f.close()

#7
print("Задача 7: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
f = open('a.txt', 'w')
for i in range(0, len(ans), 2):
    f.write(ans[i])
f.close()
f = open('b.txt', 'w')
for i in range(1, len(ans), 2):
    f.write(ans[i])
f.close()

#8
print("Задача 8: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
f = open(s, 'w')
for i in ans:
    f.write(int(i) ** 2)
f.close()

#9
print("Задача 9: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
minpos = 0
maxpos = 0
for i in range(len(ans)):
    if ans[minpos] > ans[i]:
        minpos = i
    if ans[maxpos] < ans[i]:
        maxpos = i
ans[maxpos], ans[minpos] = ans[minpos], ans[maxpos]
f = open(s, 'w')
for i in ans:
    f.write(i)
f.close()

#10
print("Задача 10: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
ans = ans[:len(ans) / 2]
f = open(s, 'w')
for i in ans:
    f.write(i)
f.close()

#11
print("Задача 11: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
ans = ans[::2]
f = open(s, 'w')
for i in ans:
    f.write(i)
f.close()

#12
print("Задача 12: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
buf = []
for i in ans:
    if int(i) < 0:
        buf.append(i)
for i in buf:
    f.write(i)
f.close()

#13
print("Задача 13: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
ans += ans
for i in ans:
    f.write(i)
f.close()

#14
print("Задача 14: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
buf = []
for i in range(len(ans)):
    buf.append(ans[i])
    if i & 1:
        buf.append(ans[i])
for i in buf:
    f.write(i)
f.close()

#15
print("Задача 15: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
for i in range(len(ans)):
    if not i & 1:
        ans[i] = '00'
for i in ans:
    f.write(i)
f.close()

#16
print("Задача 16: ")
s = input("Введите имя первого файла: ")
f = open(s, 'r')
a1 = []
for line in f:
    a1 += line.split()
f.close()
s1 = input("Введите имя второго файла: ")
f = open(s1, 'r')
a2 = []
for line in f:
    a2 += line.split()
f.close()
f = open(s2, 'w')
for i in a1:
    f.write(i)
f.close()
f = open(s1, 'w')
for i in a2:
    f.write(i)
f.close()

#17
print("Задача 17: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
s = input("Введите новое имя файла: ")
f = open(s, 'w')
for i in ans:
    f.write(i)
f.close()

#18
print("Задача 17: ")
s1 = input("Введите имя 1 файла: ")
s2 = input("Введите имя 2 файла: ")
s3 = input("Введите имя 3 файла: ")
b1 = os.path.getsize(s1)
b2 = os.path.getsize(s2)
b3 = os.path.getsize(s3)
k = max(b1, b2, b3)
l = min(b1, b2, b3)
f1 = ''
f2 = ''
if b1 == k:
    f1 = open(s1, 'r')
elif b2 == k:
    f1 = open(s2, 'r')
else:
    f1 = open(s3, 'r')
if b1 == l:
    f2 = open(s1, 'r')
elif b2 == l:
    f2 = open(s2, 'r')
else:
    f2 = open(s3, 'r')
ans1 = []
for line in f1:
    ans1 += line.split()
f1.close()
ans2 = []
for line in f2:
    ans2 += line.split()
f2.close()
if b1 == k:
    f2 = open(s1, 'r')
elif b2 == k:
    f2 = open(s2, 'r')
else:
    f2 = open(s3, 'r')
if b1 == l:
    f1 = open(s1, 'r')
elif b2 == l:
    f1 = open(s2, 'r')
else:
    f1 = open(s3, 'r')
for i in ans1:
    f1.write(i)
f1.close()
for i in ans2:
    f2.write(i)
f2.close()

#19
print("Задача 19: ")
s1 = input("Введите имя 1 файла: ")
s2 = input("Введите имя 2 файла: ")
f1 = open(s1, 'r')
f2 = open(s2, 'r')
ans1 = []
for line in f1:
    ans1 += line.split()
f1.close()
ans2 = []
for line in f2:
    ans2 += line.split()
f2.close()
buf1 = ans1 + ans2
buf2 = ans2 + ans1
f = open(s1, 'w')
for i in buf1:
    f.write(i)
f.close()
f = open(s2, 'w')
for i in buf2:
    f.write(i)
f.close()

#20
print("Задача 20: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    ans += line.split()
f.close()
pol = open('pol.txt', 'w')
otr = open('otr.txt', 'w')
for i in range(len(ans), -1, -1):
    if int(ans[i]) > 0:
        pol.write(ans[i])
    if int(ans[i]) < 0:
        otr.write(ans[i])
pol.close()
otr.close()

#21
print("Задача 21: ")
s1 = input("Введите имя 1 файла: ")
s2 = input("Введите имя 2 файла: ")
s3 = input("Введите имя 3 файла: ")
f1 = open(s1, 'r')
a1 = []
for line in f1:
    a1 += line.split()
f1.close()
f2 = open(s2, 'w')
a2 = []
for line in f2:
    a2 += line.split()
f2.close()
ans = []
i = 0
j = 0
while i < len(a1) and j < len(a2):
    if a1[i] > a2[j]:
        ans += a2[j]
        j += 1
    else:
        ans += a1[i]
        i += 1
while i < len(a1):
    ans += a1[i]
    i += 1
while j < len(a2):
    ans += a2[j]
    j += 1
f = open(s3, 'w')
for i in ans:
    f.write(i)
f.close()

#22
print("Задача 22: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
s = f.read(1)
ans = ''
while s != ' ':
    ans += s
    s = f.read(1)
f.close()
f = open(s, 'w')
f.write(ans)
f.close()

#23
print("Задача 22: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = '31/12/9999'
for line in f:
    x = line.split()
    for i in x:
        a, b, c = i.split('/')
        if ans.split('/')[2] < c and 3 <= b <= 5:
            ans = i
        elif ans.split('/')[2] == c and 3 <= b <= 5:
            if ans.split('/')[1] < b:
                ans = i
            elif ans.split('/')[1] == b:
                if ans.split('/')[1] < a:
                    ans = i
f.close()
print(ans)

#24
print("Задача 22: ")
s = input("Введите имя файла: ")
f = open(s, 'r')
ans = []
for line in f:
    if line.split('/')[1] in [1, 2, 12]:
        ans.append(x)
s = input("Введите имя для нового файла")
f = open(s, 'w')
ans = ans[::-1]
for i in ans:
    f.write(i)
f.close()
