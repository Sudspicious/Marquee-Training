def fact(n):
    if n == 100:
        return "Stack Overflow!"
    elif n == 0 or n == 1:
        return 1
    else:
        return n*fact(n-1)

n = int(input("Enter the value to find factorial : "))
print("The factorial series : ", end= " ")
if n < 0 :
    print("Invalid !!!")
else:    
    print(fact(n))
    