#diamond alphabet pattern!
n = int(input())

for i in range(n * 2 - 1):
    d = ""
    for j in range(n - abs(n - i - 1)):
        d += chr(65 + j)

    print(" " * abs(n - i - 1) + d + d[-2::-1])
