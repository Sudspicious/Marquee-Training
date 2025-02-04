def is_prime(num):
    if num <= 1:
        return False
    if num == 2:
        return True
    i = 2
    while i * i <= num:
        if num % i == 0:
            return False
        i += 1
    return True

a = int(input("Enter the starting range : "))
b = int(input("Enter the ending range   : "))

for i in range(a, b + 1):
    if is_prime(i):
        count = 0
        for j in str(i):
            if is_prime(int(j)):
                count += 1
            if count == len(str(i)):
                print(i, end=", ")