def maxi(ar, s):
    cur = sum(ar[:s])
    h = s
    maxi = cur
    i = 0
    while s < len(ar):
        cur = cur - ar[i] + ar[s]
        i += 1
        s += 1
        maxi = max(cur, maxi)
    return "The maximum average from the sub array is :" + maxi/h

n = list(map(int, input().split()))
s = int(input("Enter the window size: "))
print(maxi(n, s))