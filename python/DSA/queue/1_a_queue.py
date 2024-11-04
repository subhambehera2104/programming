class queue:
    def __init__(self, max_size = 10):
        self.max_size = max_size
        self.queue = []
    def enqueue(self, element): # Push operation
        if len(self.queue) < self.max_size :
            self.queue.append(element)
        else: 
            return False
        return element
    def dequeue(self): # POP operation
        if len(self.queue) > 0:
            return self.queue.pop(0)

    def front(self):
        if len(self.queue) > 0:
            return self.queue[0]
        else:
            print("Queue is empty")

q = queue()
print(f"Inserted {q.enqueue(1)}")
print(f"Inserted {q.enqueue(2)}")
print(f"Inserted {q.enqueue(3)}")
print(f"Removed element is {q.dequeue()}")
print(f"Top element is {q.front()}")
print(f"Removed element is {q.dequeue()}")
print(f"Top element after pop is {q.front()}")