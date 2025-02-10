def fib(n):
    if n <= 0:
        return "Input should be a positive integer."
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)

n = int(input("Enter the length of the series : "))
print("Fibonacci series:", end= " ")
for i in range(1, n + 1):
    print(fib(i), end= " ")
