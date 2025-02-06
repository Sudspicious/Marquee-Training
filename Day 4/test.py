ar = "zaz"
l = len(ar)
c = 0
for i in ar:
    if i not in ar:
        c += 1
if c < l-1 or c > l:
    print("False")
elif c == l:
    print("True")