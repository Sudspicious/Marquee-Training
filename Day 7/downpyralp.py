n = int(input())

for i in range(n):
    d = ""
    for j in range(n-i):
        d += chr(65 + j) + " "
    print(" "*i + d)