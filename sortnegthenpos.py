l = list(map(int, input().split(" ")))

le = len(l)

"""for i in range(0, le - 1):
    for j in range(i + 1, le):
        if l[j] < 0:
            l[j], l[i] = l[i], l[j]
            break

print(l)"""

new = []

for i in l:
    if i < 0:
        new.insert(0, i)
    elif i >= 0:
        new.append(i)

print(new)