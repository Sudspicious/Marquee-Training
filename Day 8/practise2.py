def valid_parenthesis(string):
    stack = []
    mapp = {
        ')': '(',
        ']': '[',
        '}': '{'
    }
    for i in string:
        if i in mapp:
            if stack and stack[-1] == mapp[i]:
                stack.pop()
            else:
                return False
        else:
            stack.append(i)
    return not stack

str = input("Enter the string: ")
print(valid_parenthesis(str))