class Queue:
    def __init__(self):
        self.queue = []
    
    def enqueue(self, data):
        self.queue.append(data)
        print(f"{data} is added to queue!")
    
    def dequeue(self):
        print(self.queue.pop(0), "is removed!")

    def display(self):
        for i in self.queue:
            print(i, end= "")
        print()
    
    def size(self):
        print(len(self.queue), " is the length of the queue!")
    
    def dislast(self):
        q = self.queue
        j = []
        l = len(q)
        for i in q:
            if i not in j:
                j.append(i)
            elif i in j:
                j.remove(i)
        print(j[-1])

Q = Queue()
a = int(input("Enter the num of elements to add : "))
for i in range(a):
    Q.enqueue(input("En :"))

Q.dislast()