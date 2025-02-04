class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def ins_beg(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def ins_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node
    
    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print("None")
    
    def is_palindrome(self):
        slow, fast = self.head, self.head
        stack = []
        while fast and fast.next:
            stack.append(slow.data)
            slow, fast = slow.next, fast.next.next
        if fast:
            slow = slow.next
        while slow:
            if slow.data != stack.pop():
                print("Not a Palindrome")
                return
            slow = slow.next
        print("Palindrome")

    def rotate(self, n):
        if not self.head or n == 0:
            return
        last, l = self.head, 1
        while last.next:
            last = last.next
            l += 1
        n = n % l
        if n == 0:
            return
        prev, curr = None, self.head
        for _ in range(l - n):
            prev, curr = curr, curr.next
        prev.next = None
        last.next = self.head
        self.head = curr

    def primeornot(self):
        s = ''
        cur = self.head
        while cur:
            s = s + str(cur.data)
            cur = cur.next
        c = 0
        prime = int(s)
        for i in range(1, prime+1):
            if prime % i == 0:
                c += 1
        if c == 2:
            print("The Linked List is a Prime number!")
        else:
            print("The Linked List is not a Prime number!")

new = SLL()

n = int(input("Enter the number of nodes: "))

for _ in range(n):
    choice, value = input("Insert at Beginning (B) or End (E): ").strip().lower(), int(input("Enter value: "))
    new.ins_beg(value) if choice == "b" else new.ins_end(value) if choice == "e" else print("Invalid choice!")

new.display()

new.is_palindrome()
ch = input("Do you want to rotate the linked list! (Y or N)").strip().lower()
if ch == "y":
    k = int(input("Enter the number of nodes to rotate : "))
    if k < n:
        new.rotate(k)
    else:
        print("Enter a valid value!")

    new.display()


new.primeornot()
