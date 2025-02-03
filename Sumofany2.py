num = input()
l = []
for i in num:
    l.append(int(i))
l.sort()
a = (l[0] * 10) + l[3]
b = (l[1] * 10) + l[2]
print(a+b)