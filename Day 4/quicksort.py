def qs(l):
    a = len(l)
    p = l[a//2]
    left = [i for i in l if i < p]
    mid = [i for i in l if i == p]
    right = [i for i in l if i > p]
    