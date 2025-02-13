n = int(input())
while n != 0:
    s = list(map(int,input().split()))
    d = list(map(int,input().split()))
    f = list(map(int,input().split()))
    c = list(map(int,input().split()))

    ff = []
    fc = []

    for i in range(0, len(f)):
        ff.append(s[i] - (d[i] * f[i]))
        fc.append(s[i] - (d[i] * c[i]))
    
    sf = sum(ff)
    sc = sum(fc)

    if sf > sc:
        print("Flash")
    elif sf < sc:
        print("Cisco")
    elif sf == sc:
        print("Tie")
    n -= 1