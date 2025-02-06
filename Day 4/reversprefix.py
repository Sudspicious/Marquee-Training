a = input("Word : ")
c = input("Char : ")

l1 = []

j = 0

for i in a:
    if i is not c:
        l1.append(i)
    else:
        l1.append(i)
        break
    j += 1
i = 0
h = j
while i <= j:
    l1[i], l1[j] = l1[j], l1[i]
    i += 1
    j -= 1
for i in range(h+1, len(a)):
    l1.append(a[i])
for i in l1:
    print(i, end="")
