class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def insbeg(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def delbeg(self):
        if self.head is None:
            print("The list is empty!")
            return
        self.head = self.head.next

    def insend(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new
    
    def delend(self):
        if self.head is None or self.head.next is None:
            print("None")
            return
        pre = self.head
        fro = pre.next
        while fro.next:
            pre = pre.next
            fro = fro.next
        pre.next = None
    
    def insatany(self, data, pos):
        new = Node(data)
        if pos == 0:
            new.next = self.head
            self.head = new
            return
        cur = self.head
        temp = self.head
        l = 1
        while temp:
            l += 1
            temp = temp.next
        if pos > l:
            print("Invalid Entry!")
            return
        elif pos < l:
            for j in range(pos - 1):
                if not cur:
                    print("Position out of bounds!")
                    return
                cur = cur.next
            new.next = cur.next
            cur.next = new
        
    def delpos(self, pos):
        if pos == 0:
            self.head = self.head.next
            return
        cur = self.head
        temp = self.head
        l = 1
        while temp:
            l += 1
            temp = temp.next
        if pos > l:
            print("Invalid Entry!")
            return
        elif pos < l:
            for j in range(pos - 1):
                if not cur:
                    print("Position out of bounds!")
                    return
                cur = cur.next
            cur.next = cur.next.next
    
    def display(self):
        if self.head is None:
            print("The list is empty!")
            return
        cur = self.head
        while cur:
            print(cur.data, end = " -> ")
            cur = cur.next
        print("None")
        print()
    
    def search(self, data):
        cur, pos = self.head, 1
        while cur:
            if cur.data == data:
                print(f"Element found at position {pos}")
                return
            cur, pos = cur.next, pos + 1
        print("Element not found!")

    def midele(self):
        if self.head is None:
            print("The list is empty!")
            return
        slow = fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        print(f"The middle element is {slow.data}")
    
    def reverse(self):
        prev , cur = None, self.head
        while cur:
            cur.next, prev, cur = prev, cur, cur.next
        self.head = prev
    
    def sort(self):
        cur = self.head
        if not self.head or not self.head.next:
            print("None")
            return
        while cur.next:
            swapi = cur.next
            while swapi:
                if cur.data > swapi.data:
                    cur.data, swapi.data = swapi.data, cur.data
                swapi = swapi.next
            cur = cur.next

Li = LinkedList()

Li.insbeg(1)
Li.insbeg(2)
Li.insbeg(3)
Li.insbeg(4)
Li.insbeg(5)
Li.insbeg(6)
Li.display()
