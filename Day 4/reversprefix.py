a = input("Word : ")
c = input("Char : ")

l1 = []
l2 = []

j = 0

for i in a:
    if i is not c:
        l1.append(i)
    else:
        l1.append(i)
        break
    j += 1
l2 = l1[::-1]
for i in range(j+1, len(a)):
    l2.append(a[i])
print(l2)
