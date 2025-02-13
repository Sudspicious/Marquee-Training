n = int(input("Enter the size of the staircase : "))

for i in range(1, n+1):
    for j in range(1, i+1):
        if i % 2 == 0:
            print(j * 2,end=" ")
        else:
            print(j * 2 - 1, end=" ")
    print()