# Stack program using dequecollection library

from collections import deque  #the collections is biggest library and deque is class of collectios library
# deque full form is dubyended queue
class Stack(): 
    def __init__(self):
        self.stack = deque() #This line code like self.stack = []
    def push(self, element):
        self.stack.append(element) 
    def pop(self):
        return self.stack.pop() #in this scope pop() is function of deque
    def top(self):
        return self.stack[len(self.stack)-1] #print the top element

s = Stack()
s.push(1)
s.push(3)
s.push(2) 
print(f"Top element is {s.top()}")
print(f"Removed element is {s.pop()}")
print(f"Now top element is {s.top()}")