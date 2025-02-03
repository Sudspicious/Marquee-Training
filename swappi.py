a = int(input())
b = int(input())

a = a ^ b
b = b ^ a
a = a ^ b

print(a, b)
