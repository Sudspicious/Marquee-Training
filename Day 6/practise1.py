ar = []

import numpy as np

for i in range(3):
    y = list(map(int, input().split()))
    ar.append(y)

c = []

for i in ar:
    for j in i:
        c.append(j)

z = set(c)

if len(z) != len(c):
    exit("Duplicate elements detected!")

d = 0
r = 0
co = 0

arr = np.array(ar)
trans = arr.transpose()

for i in arr:
    r += sum(i)
for i in trans:
    co += sum(i)
for i in arr:
    d += i[1]


for i in arr:
    print(i)

if co == 45 and r == 45 and d == 15:
    print("It is a perfect sudoku!")
else:
    print("It is not a perfect sudoku!")

print("The sum of the rows is : ", r, " by average : ", r/3)
print("The sum of the columns is : ", co, " by average : ", co/3)
print("The sum of the diagonals is : ", d)