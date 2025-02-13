class stacks:
    
    def __init__(self, size):
        self.stack = []
        self.size = size

    def push(self, data):
        if len(self.stack) <= self.size:
            self.stack.append(data)
            print(f"{data} is added to the stack!")
        else:
            print("Stack Overflow!")


    def pop(self):
        if len(self.stack) > 0:
            return print(f"{self.stack.pop()} is removed from the stack!")
        else:
            print("Stack Underflow!")
    
    def peek(self):
        if len(self.stack) == 0 :
            print("Stack is empty!")
        else:
            return print(f"{self.stack[-1]} is at the top of the stack!")
    
    def size(self):
        if len(self.stack) == 0 :
            print("Stack is empty!")
        else:
            return print(f"{len(self.stack)} is the length of the stack!")
    
    def isempty(self):
        if len(self.stack) == 0:
            print("Stack is empty!!")
        else:
            print("Stack has some elements!!")

    def getstack(self):
        if len(self.stack) == 0 :
            print("Stack is empty!")
        else:
            return print(self.stack[::-1])
    
    def findnexG(self):
        st = self.stack
        m = []
        l = len(st)
        if l == 0:
            print("Stack is empty!")
            return
        for i in range(l):
            for j in range(i+1, l):
                if st[j] > st[i]:
                    m.append(st[i+1])
                elif st[j] == st[i]:  
                    m.append(0)
                else:
                    m.append(st[i])
        print(m)

    def revwilorsl(self):
        st = self.stack
        l = len(st)
        j = stacks(l)
        for i in st:
            j.push(i)
        print(j.getstack())

    def remdup(self):
        st = self.stack
        l = len(st)
        j = []
        for i in st:
            if i not in j:
                j.append(i)
        print(j)

    def pushzeroes(self):
        st = self.stack
        l = len(st)
        c = 0
        s = []
        for i in range(l):
            if st[i] != 0:
                s.append(st[i])
            else:
                c += 1
        for i in range(c):
            s.append(0)
        print(s)

n = int(input("Enter the number of items : "))

st = stacks(n)

for i in range(n):
    st.push(int(input("Push : ")))

choice = input("Do you want to perform anymore actions ? (Y or N) : ").strip().lower()
while choice != "n":
    if choice == "y":
        print("What operation do you want to do ?")
        print("1. Push More")
        print("2. Pop")
        print("3. Peek")
        print("4. GetStack")
        print("5. Size")
        print("6. EmptyStack")
        ch2 = int(input("Choice : ").strip())
        if ch2 == 1:
            st.push(input("Push : "))
            print("")

        elif ch2 == 2:
            st.pop()
            print("")

        elif ch2 == 3:
            st.peek()
            print("")

        elif ch2 == 4:
            st.getstack()
            print("")

        elif ch2 == 5:
            st.size()
            print("")

        elif ch2 == 6:
            st.isempty()
            print("")

        else:
            print("Invalid entry!!!")
    elif choice == "n":
        print("The code is closed!")
    else:
        print("Invalid choice!")
    choice = input("Do you want to perform anymore actions ? (Y or N) : ").strip().lower()

st.revwilorsl()
st.remdup() 
st.pushzeroes()
#st.findnexG()
