"""n = list(map(int, input().split()))

s = int(input("Window Size : "))

sums = []
ma = [1]

for i in range(s):
    if i == len(n) - s:
        break
    sums.append(sum(n[i:s+i]))
    for i in range(len(sums)-1):
        if sums[i+1] > sums[i]:
            ma[0] = 0
            ma[0] = sums[i+1]

print("The maximum sum of the sub arrray : ", ma[0])
"""
def maxi(ar, s):
    cur = sum(ar[:s])
    maxi = cur
    i = 0
    while s < len(ar):
        cur = cur - ar[i] + ar[s]
        i += 1
        s += 1
        maxi = max(cur, maxi)
    return maxi

n = list(map(int, input().split()))
s = int(input("Enter the window size: "))
print(maxi(n, s))