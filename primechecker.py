def primechecker(n, c=0):
    if n < 2: return False
    for i in range(2, n+1):
        if n % i == 0: c += 1
    if c == 1: return True
    else: return False  
print(primechecker(int(input("Enter a number: "))))