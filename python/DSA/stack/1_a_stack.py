class Stack:
    def __init__(self, max_size=5):
        self.max_size = max_size
        self.stack = []
        
    def push(self, element):
        if len(self.stack) < self.max_size:
            self.stack.append(element)
            print(f"Inserted {element}")
        else:
            print(f"Stack is full. Max size is {self.max_size}")
    
    def top(self):
        if len(self.stack) > 0:
            print("Top element: ", self.stack[len(self.stack)-1])
        else:
            print("Stack is empty")
    
    def pop(self):
        if len(self.stack) > 0:
            print("removed element: ",  self.stack.pop())
        else:
            print("Stack is empty")
            return None



elements = [1, 2, 3, 4, 5, 6]

print("Stack with no Max Size passed")
s1 = Stack()
for element in elements:
    s1.push(element)

s1.top()  
s1.pop()  
s1.top()  


print("Stack with Max Size passed")
s2 = Stack(max_size=10)
for element in elements:
    s2.push(element)

s2.top()  
s2.pop()  
s2.top() 