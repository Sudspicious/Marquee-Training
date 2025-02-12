graph = {
    0: [1, 2, 3],
    1: [0, 4, 5],
    2: [0, 6],
    3: [0,7],
    4: [1],
    5: [1],
    6: [2],
    7: [3]
}
s = 0
v = set()
q = [s]
v.add(s)

while q:
    node = q.pop(0)
    print(node, end=' ')
    for i in graph(node):
        if i not in v:
            q.append(i)
            v.add(i)