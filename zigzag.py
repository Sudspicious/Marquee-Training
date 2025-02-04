class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def insend(self, data):
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
    
    def zigzag(self):
        cur = self.head
        l = []
        
        while cur:
            l.append(cur.data)
            cur = cur.next
        
        le = len(l)
        mid = le // 2
        s = [l[mid]]
        
        left, right = mid - 1, mid + 1
        
        while left >= 0 or right < le:
            if left >= 0:
                s.append(l[left])
                left -= 1
            if right < le:
                s.append(l[right])
                right += 1

        print("Zigzag Order:", " -> ".join(map(str, s)), "-> None")



new = SLL()

n = int(input("Enter the number of nodes: "))

for _ in range(n):
    value = int(input("Enter value: "))
    new.insend(value)
new.display()

new.zigzag()