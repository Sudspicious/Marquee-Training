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
        self.stack = []

    def getstack(self):
        if len(self.stack) == 0 :
            print("Stack is empty!")
        else:
            return print(self.stack[::-1])

n = int(input("Enter the number of items : "))

st = stacks(n)

for i in range(n):
    st.push(input("Push : "))

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

