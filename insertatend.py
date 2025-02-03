class node:
    def __init__(self, data):
        self.data = data
        self.next = None

class sll:
    def __init__(self):
        self.head = None

    def insertatend(self, data):
        new = node(data)
        if self.head is None:
            self.head = new
        else:
            cur = self.head
            while cur.next is not None:
                cur = cur.next
            cur.next = new
            new.next = None

    def display(self):
        if self.head is None:
            print("The Linked List is Empty!!!")
        else:
            cur = self.head
            while cur is not None:
                print(cur.data, end=' -> ')
                cur = cur.next
            print("None")

new = sll()

a = int(input("Enter the number of nodes you want : "))

for i in range(a):
    new.insertatend(int(input()))

new.display()
