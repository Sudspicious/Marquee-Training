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
    
    def del_beg(self):
        if self.head is None:
            print("The list is empty!")
            return
        self.head = self.head.next

    def ins_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return
        curr = self.head
        while curr.next:
            curr = curr.next
        curr.next = new_node

    def del_end(self):
        if self.head is None or self.head.next is None:
            print("None")
            return
        pre = self.head
        fro = pre.next
        while fro.next:
            pre = pre.next
            fro = fro.next
        pre.next = None

    def ins_pos(self, pos, data):
        new_node = Node(data)
        if pos == 0:
            new_node.next = self.head
            self.head = new_node
            return
        curr = self.head
        temp = self.head
        l = 1
        while temp:
            l += 1
            temp = temp.next
        if pos > l:
            print("Invalid Entry!")
            return
        elif pos < l:
            for _ in range(pos - 1):
                if not curr:
                    print("Position out of bounds!")
                    return
                curr = curr.next
            new_node.next = curr.next
            curr.next = new_node

    def search(self, data):
        curr, pos = self.head, 1
        while curr:
            if curr.data == data:
                print(f"Element found at position {pos}.")
                return
            curr, pos = curr.next, pos + 1
        print("Element not found!")

    def mid_elem(self):
        if not self.head:
            print("Linked List is empty!")
            return
        slow, fast = self.head, self.head
        while fast and fast.next:
            slow, fast = slow.next, fast.next.next
        print(f"Middle element: {slow.data}")

    def reverse(self):
        prev, curr = None, self.head
        while curr:
            curr.next, prev, curr = prev, curr, curr.next
        self.head = prev

    def sort(self):
        cur = self.head
        if not self.head or not self.head.next:
            return
        while cur.next:
            forw = cur.next
            while forw:
                if cur.data > forw.data:
                    cur.data, forw.data = forw.data, cur.data
                forw = forw.next
            cur = cur.next

    def display(self):
        curr = self.head
        while curr:
            print(curr.data, end=' -> ')
            curr = curr.next
        print("None")

new = SLL()
n = int(input("Enter the number of nodes: "))
for _ in range(n):
    choice, value = input("Insert at Beginning (B) or End (E): ").strip().lower(), int(input("Enter value: "))
    new.ins_beg(value) if choice == "b" else new.ins_end(value) if choice == "e" else print("Invalid choice!")
new.display()
new.sort()
new.display()

choice = input("Do you want to insert more (Y), search (S), Delete (D) or exit (N)? ").strip().lower()
while choice != "n":
    if choice == "y":
        new.ins_pos(int(input("Enter position: ")), int(input("Enter value: ")))
        ch = input("Do you want to sort more ? (Y) or (N) : ").strip().lower()
        new.display()
    elif choice == "d":
        ch = input("Where do you want to delete? (B, E, or A) : ").strip().lower()
        if ch == "b":
            new.del_beg()
        elif ch == "e":
            new.del_end()
        elif ch == "a":
            new.del_any()
        else:
            print("Invalid Entry!!")
        new.display()
    elif choice == "s":
        new.search(int(input("Enter value to search: ")))
    elif choice == "n":
        print("The code is closed!")
    else:
        print("Invalid choice!")
    choice = input("Do you want to insert more (Y), search (S), Delete (D) or exit (N)? ").strip().lower()
