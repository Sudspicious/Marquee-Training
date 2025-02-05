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
    
    def dislast(self):
        st = self.stack
        l = len(st)
        j = []
        for i in st:
            if i not in j:
                j.append(i)
            elif i in j:
                j.remove(i)
        print(f"{j[-1]} is the final element!")

n = int(input("Enter the number of items : "))

st = stacks(n)

for i in range(n):
    st.push(input("Push : "))

st.dislast()