n = int(input())

primes = []

for i in range(3, n):
    c = 0
    for j in range(1, i + 1):
        if i % j == 0:
            c += 1
    if c == 2:
        primes.append(i)
print(primes)

for i in primes:
    if n % 2 == 0 and n % i != 0:
        val = "Yes"
    else:
        val = "No"
print(val)        