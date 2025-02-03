class node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class dll:
    def __init__(self):
        self.head = None

    def ins_beg(self, data):
        new = node(data)
        new.next = self.head
        new.next.prev = new
        self.head = new
    
    def ins_end(self, data):
        new = node(data)
        if self.head is None:
            new.next = self.head
            new.next.prev = new
            self.head = new
        cur = self.head
        while cur is not None:
            cur = cur.next
        new.next = None
        cur.next = new
        new.prev = cur

    def display(self):
        if self.head is None:
            print("The Linked List is Empty!!!")
            return
        cur = self.head
        print('None', end = " <-> ")
        while cur is not None:
            print(cur.data, end=' <->')
            cur = cur.next
        print("None")

new = dll()

a = int(input("Enter the number of nodes you want : "))

for i in range(a):
    new.insertatbeg(int(input()))
    new.display()
