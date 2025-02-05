ar = list(map(int, input().split()))
l = 0
for i in ar:
    if i == 0:
        l += 1

for i in range(l):
    ar.remove(0)
    ar.append(0)

print(ar)
