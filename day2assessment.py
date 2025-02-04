# The function should return the minimal length of a contigous sub array such that its sum is greater than or equal to s

#constraints
#size of ar is in the range 1, 100
#arr should consists of only positive integer
#s should be a positive integers only
#
#test cases
# 1, 3, 5, 7, 9 - 100 - 0
# 2, 3, 1, 2, 4, 3 - 7 - 2
# 1, 4, 3, 2, 6, 8 - 8 - 1
# 10, 20, 25, 15 - 70 - 0
#

li = list(map(int, input("Give the elements of the array : ").split()))
ta = int(input("Enter the target amount! : "))
c = 0
l = len(li)

def findmin(a, ta):
    if ta <= 0 or sum(a) < ta:
        return 0
    for i in a:
        if i > ta:
            return 1
    l = []
    for i in range(0, len(a) - 1):
        for j in range(i+1, len(a)):
            if sum(a[i:j],) 
    print(c)

print(findmin(li, ta))
