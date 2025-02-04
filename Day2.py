class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def ins_beg(self, data):
        new = Node(data)
        new.next = self.head
        self.head = new
    
    def ins_end(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            return
        cur = self.head
        while cur.next:
            cur = cur.next
        cur.next = new
    
    def display(self):
        cur = self.head
        while cur:
            print(cur.data, end=' -> ')
            cur = cur.next
        print("None")
    
    def is_palindrome(self):
        if self.head is None:
            print("Linked List is empty!")
            return
        cur = self.head
        st = []
        while cur:
            st.append(cur.data)
            cur = cur.next
        if st == st[::-1]:
            print("It is a palindrome!")
        else:
            print("It is not a palindrome!")

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

    def pairs(self, target):
        if self.head:
            cur = self.head
            while cur.next:
                forw = cur.next
                while forw:
                    if (cur.data + forw.data) == target:
                        print(f"The pair is [{cur.data}, {forw.data}]")
                    forw = forw.next
                cur = cur.next

new = SLL()

n = int(input("Enter the number of nodes: "))

for _ in range(n):
    choice, value = input("Insert at Beginning (B) or End (E): ").strip().lower(), int(input("Enter value: "))
    new.ins_beg(value) if choice == "b" else new.ins_end(value) if choice == "e" else print("Invalid choice!")

new.display()

ch = input("Do you want to check whether the linked list is palindrome or not! (Y or N)").strip().lower()
if ch == "y":
    new.is_palindrome()
elif ch != "y" and ch != "n":
    print("Enter a proper value!")

ch = input("Do you want to rotate the linked list! (Y or N)").strip().lower()
if ch == "y":
    k = int(input("Enter the number of nodes to rotate : "))
    if k < n:
        new.rotate(k)
    else:
        print("Enter a valid value!")
elif ch != "y" and ch != "n":
    print("Enter a proper value!")
    new.display()

ch = input("Do you want to check whether the linked list has prime numbers or not! (Y or N)").strip().lower()
if ch == "y":
    k = int(input("Enter the number of nodes to rotate : "))
    if k < n:
        new.primeornot()
    else:
        print("Enter a valid value!")

ch = input("Do you want to check a pair which adds up to a target value! (Y or N)").strip().lower()
if ch == "y":
    target = int(input("Enter target value : "))
    new.pairs(target)
elif ch != "y" and ch != "n":
    print("Enter a proper value!")
