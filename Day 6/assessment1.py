l = list(map(int, input("Enter the elements of the list : ").split()))
""" 
n = len(l) + 1
t = n * (n + 1) // 2

print("The missing element is : ", end = " ")
print(t - sum(l))
l.append(t - sum(l))
print("The elements of the list are : ", end = " ")
l.sort()
print(l)"""

n = len(l)
rsum = (n + 1) * (n + 2) // 2
asum = sum(l)

if rsum - asum == n + 1:
    print("The are no missing elements in the list!")
else:
    print(rsum - asum)