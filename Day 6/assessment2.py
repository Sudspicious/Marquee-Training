str = input("Enter the String : ")
l = []
for i in str:
    if i.isdigit():
        l.append(int(i))
    elif i == "P":
        l.append(10)
s = 0
for i in l:
    s += i
print("The sum of only the digits is : ",s)