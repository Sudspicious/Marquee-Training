class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def insertatbeg(self, data):
        new = node(data)
        new.next = self.head
        self.head = new

    def display(self):
        if self.head is None:
            print("The Linked List is Empty!!!")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=' ->')
                cur = cur.next
            print("None")
    
    def binarytoint(self):
        s = ''
        cur = self.head
        while cur:
            s = s + str(cur.data)
            cur = cur.next
        print(int(s, 2))
    
    def binofsum(self):
        s = 0
        cur = self.head
        while cur:
            s += cur.data
            cur = cur.next
        print(bin(s)[2:])

new = sll()

a = int(input("Enter the number of nodes you want : "))

for i in range(a):
    new.insertatbeg(int(input()))

new.display()

new.binarytoint()

new.binofsum()
