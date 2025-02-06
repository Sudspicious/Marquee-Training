s = input("Enter the string : ")
m = []
for i in s:
    if i.isalnum():
        m.append(i.lower())

c = len(m)

l, r = 0, c - 1

co = 0

mid = int(c/2)

while l < r:
    if m[l] == m[r]:
        co += 1
    l += 1
    r -= 1
if co == mid:
    print("Palindrome!")
else:
    print("Not a Palindrome!")
        