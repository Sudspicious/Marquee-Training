ar = list(map(str, input().split()))
i = 0
while i in range(len(ar)):
    m = ar[i]

    c = len(m)

    l, r = 0, c - 1

    co = 0

    mid = int(c/2)

    while l < r:
        if m[l] == m[r]:
            co += 1
        l += 1
        r -= 1
    if co == mid:
        print(ar[i], " is the first palindrome!")
        break
    else:
        i += 1