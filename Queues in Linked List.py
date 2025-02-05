class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = None

    def enqueue(self, data):
        new = Node(data)
        if self.front:
            cur = self.front
            while cur.next:
                cur = cur.next
            cur.next = new
            new.next = None
        else:
            self.front = new
            new.next = None
    
    def dequeue(self):
        if self.front:
            cur = self.front
            self.front = cur.next
            cur = None
        else:
            print("Queue Underflow!")

    def size(self):
        if self.front:
            c = 0
            cur = self.front
            while cur.next:
                c += 1
                cur = cur.next
            print(f"The size of the queue is : {c}")
        else:
            print("The queue is empty!")
        
    def display(self):
        if self.front:
            cur = self.front
            while cur:
                print(cur.data, end=" ")
                cur = cur.next
        else:
            print("The queue is empty!")
    
    def isempty(self):
        if self.front is None:
            print("The queue is empty!")
            return

Q = Queue()

n = int(input("The size of the queue : "))

for i in range(n):
    Q.enqueue(input("En : "))

choice = input("Do you want to perform anymore actions ? (Y or N) : ").strip().lower()
while choice != "n":
    if choice == "y":
        print("What operation do you want to do ?")
        print("1. Enqueue")
        print("2. Dequeue")
        print("3. Size")
        print("4. Display")
        print("5. Size")
        print("6. Isempty")
        ch2 = int(input("Choice : ").strip())
        if ch2 == 1:
            print("")
            Q.enqueue(input("Push : "))
            print("")

        elif ch2 == 2:
            print("")
            Q.dequeue()
            print("")

        elif ch2 == 3:
            print("")
            Q.size()
            print("")

        elif ch2 == 4:
            print("")
            Q.display()
            print("")

        elif ch2 == 5:
            print("")
            Q.isempty()
            print("")

        else:
            print("")
            print("Invalid entry!!!")
    elif choice == "n":
        print("The code is closed!")
    else:
        print("Invalid choice!")
    choice = input("Do you want to perform anymore actions ? (Y or N) : ").strip().lower()

