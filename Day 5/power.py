def pow(x, n):
    for i in range(n):
        f = x
    return f

n = int(input("Enter the number : "))
p = int(input("Enter the power  : "))
if n >= 1 and p >= 1:
    print(f"The power of the element is : {pow(n, p)}")
else:
    print("Invalid entry!")