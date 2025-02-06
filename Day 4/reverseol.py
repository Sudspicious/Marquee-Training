a = input()

ar = list(a)
f, r = 0, len(ar) - 1

while f < r:
    if ar[f].isalpha() and ar[r].isalpha():
        ar[f], ar[r] = ar[r], ar[f]
        f += 1
        r -= 1
    elif not ar[f].isalpha():
        f += 1
    elif not ar[r].isalpha():
        r -= 1

print("".join(ar))
