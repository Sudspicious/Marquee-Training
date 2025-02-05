def check(s):
    if len(s) == 0:
        return False
    map = {']':'[','}':'{',')':'('}
    st = []
    for i in s:
        if i in map:
            top = st.pop() if st else None
            if map[i] != top:
                return False
        else:
            st.append(i)
    return len(st) == 0
s = input()
print(check(s))