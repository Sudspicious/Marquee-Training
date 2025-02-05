class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class stack:
    def __init__(self):
        self.head = None
    
    def push(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new

    def pop(self):
        if self.head is None:
            print("The stack is empty!")
            return
        if self.head.next is None:
            self.head = None
            return
        self.head = self.head.next

    def peek(self):
        if self.head is None:
            print("The stack is empty!")
            return
        return(self.head.data)
    
    def isempty(self):
        return self.head is None

    def getstack(self):
        if self.head is None:
            print("The stack is empty!")
            return
        cur = self.head
        while cur:
            print(cur, end= " -> ")
            cur = cur.next
        print("None")

    
st = stack()

a = int(input("Enter the number of items in stack! : "))

for i in range(a):
    st.push(input("Push: "))

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
            print("")
            st.push(input("Push : "))
            print("")

        elif ch2 == 2:
            print("")
            st.pop()
            print("")

        elif ch2 == 3:
            print("")
            st.peek()
            print("")

        elif ch2 == 4:
            print("")
            st.getstack()
            print("")

        elif ch2 == 5:
            print("")
            st.size()
            print("")

        elif ch2 == 6:
            print("")
            st.isempty()
            print("")

        else:
            print("")
            print("Invalid entry!!!")
    elif choice == "n":
        print("The code is closed!")
    else:
        print("Invalid choice!")
    choice = input("Do you want to perform anymore actions ? (Y or N) : ").strip().lower()
