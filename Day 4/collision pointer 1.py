def pair(ar, t):
    l, r = 0, len(ar) - 1
    while l < r:
        sum = ar[l] + ar[r]
        if sum == t:
            return "True"
        elif sum > t:
            r -= 1
        else:
            l += 1
    return "False"

def retrieveall(ar, t):
    l, r = 0, len(ar) - 1
    s = []
    while l < r:
        sum = ar[l] + ar[r]
        if sum == t:
            s.append((ar[l], ar[r]))
            l += 1
            r -= 1
        elif sum > t:
            r -=1
        else:
            l += 1
    for i in range(len(s) - 1):
        print(s[i], end=" - ") 
    print(s[-1])

n = int(input())

ar = list(map(int, input().split()))

t = int(input("Enter the target sum : "))

ch = int(input("Which method you want to try (1 or 2) : "))

if ch == 1:
    print(pair(ar, t))
elif ch == 2:
    retrieveall(ar, t)
else:
    print("Invalid Input!!")