def addsort(l1, l2):
    a = len(l1)
    b = len(l2)
    L = []
    i, j = 0, 0
    while i < a and j < b:
        if l1[i] < l2[j]:
            L.append(l1[i])
            i += 1
        elif l1[i] > l2[j]:
            L.append(l2[j])
            j += 1
        elif l1[i] == l2[j]:
            L.append[l1[i]]
            L.append[l2[j]]
            i += 1
            j += 2
    while i < a:
        L.append(l1[i])
        i += 1
    while j < b:
        L.append(l2[j])
        j += 1
    for i in range(a + b - 1):
        print(L[i], end= " - ")
    print(L[-1])

n = list(map(int, input().split()))
m = list(map(int, input().split()))

addsort(n, m)
