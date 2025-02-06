def redtroavg(ar, n):
    avg = []
    i = 0
    j = n - 1
    for m in range(int(n/2)):
        sum = (ar[i] + ar[j])/2
        avg.append(sum)
        ar[i] = None
        ar[j] = None
        i += 1
        j -= 1
    mi = min(avg)

    print(f"The minimum of the array is : {mi}!")


n = int(input("Enter the number of elements : "))

if n % 2 == 0:

    ar = list(map(int, input().split()))

    ar = sorted(ar)

    redtroavg(ar, n)

else:

    print("Not valid for this sum!")
