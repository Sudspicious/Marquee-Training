def dfs(graph, s):
    v = set()
    st = [s]
    while st:
        node = st.pop()
        v.add(node)
        print(node, end=' ')
        for i in reversed(graph[node]):
            if i not in v:
                st.append(i)
                v.add(i)
graph = {
    0 : [1, 4],
    1 : [0, 2],
    2 : [1, 3],
    3 : [2, 4],
    4 : [3, 0]
}
dfs(graph, 0)