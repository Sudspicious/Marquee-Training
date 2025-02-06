
def cater(ar, H):
    cur = []
    s = H
    st = ""
    st += ar[:s]
    l = len(ar)
    i = 0
    while s <= l:
        cur.append(st)
        st =""
        s += 1
        i += 1
        st += ar[i:s]
    g = []
    for i in cur:
        g.append(set(i))
    for i in g:
        if len(i) == H:
            print(i, end="is a good string!!")
            print(" ")

n = input()

s = int(input("Enter window size : "))

cater(n,s)
        