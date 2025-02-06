n = list(map(int, input().split()))

s = int(input("Window Size : "))

sums = []

for i in range(s):
    if i == len(n) - s:
        break
    sums.append(sum(n[i:s+i]))

print("The maximum sum of the sub arrray : ", max(sums))
