
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
    hi = []
    for i in cur:
        g.append(set(i))
    for i in g:
        hi.append(len(i))
        ma = max(hi)
    print(ma)

n = input()
s = len(n)//2

cater(n,s)
        