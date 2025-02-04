class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    
class CLL:
    def __init__(self):
        self.head = None
    
    def insbeg(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            new.next = self.head
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new
        new.next = self.head
        self.head = new

    def insend(self, data):
        new = Node(data)
        if not self.head:
            self.head = new
            new.next = self.head
            return
        cur = self.head
        while cur.next != self.head:
            cur = cur.next
        cur.next = new
        new.next = self.head

    def find(self):
        cur = self.head
        l = []
        while cur.next != self.head.nex:
            l.append(cur.data)
            cur = cur.next
        l.append(cur.data)
        ma = max(l)
        mi = min(l)
        print("Maximum of the CLL: ", ma)
        print("Minimum of the CLL: ", mi)
        maxdif = ma - mi
        print(maxdif)
    
    def primewith1(self):
        cur = self.head
        co = 0
        print("")
        while cur.next != self.head:
            c = 0
            for i in range(1, cur.data + 1):
                if cur.data % i == 0:
                    c += 1
            co += 1
            if c == 2:
                if cur.data % 10 == 1:
                    print(f"The value {co}. {cur.data} is a Prime number which ends with one!")
                else:
                    print(f"The value {co}. {cur.data} is a Prime number which doesnt end with one!")
            cur = cur.next

    
    def display(self):
        if self.head is None:
            print("The linked list is empty!!!")
            return
        cur = self.head 
        while cur.next != self.head:
            print(cur.data, end=" -> ")
            cur = cur.next
        print(cur.data)
    
    def redtoone(self, jump):
        cur = self.head
        l = []
        while cur.next != self.head.next:
            l.append(cur.data)
            cur = cur.next
        l.append(cur.data)
        n = len(l)
        i = 0
        while i in range(0,n):
            if n == 1:
                print(l)
                return
            if i >= n:
                l[i-n] = None
            else:
                l[i] = None
            i += jump
        print(l)

new = CLL()

n = int(input("Enter the number of nodes : "))

for _ in range(n):
    choice, value = input("Insert at Beginning (B) or End (E): ").strip().lower(), int(input("Enter value: "))
    new.insbeg(value) if choice == "b" else new.insend(value) if choice == "e" else print("Invalid choice!")

new.display()

print("")

ch = input("Do you want to get the maximum or minimum of the CLL! (Y or N) : ").strip().lower()

if ch == "y":
    new.find()
elif ch != "y" and ch != "n":
    print("Enter a proper value!")
print("")

ch = input("Do you want to check whether the element is a prime with 1 or not! (Y or N) : ").strip().lower()

if ch == "y":
    new.primewith1()
elif ch != "y" and ch != "n":
    print("Enter a proper value!")
print("")

ch = input("Do you want to reduce to a single element ! (Y or N) : ").strip().lower()

if ch == "y":
    jump = int(input("Enter the strength of the roulette : "))
    if jump < n:
        new.redtoone(jump)
    else:
        print("Enter a valid value!!!")
elif ch != "y" and ch != "n":
    print("Enter a proper value!")
print("")
