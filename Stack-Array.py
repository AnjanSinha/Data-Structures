class Stack:
    def __init__(self):
        self.array= []

    def print_stack(self):
        print(f"Stack: {self.array} , Length: {len(self.array)}")

    def peek(self):
        if len(self.array)== 0:
            return None
        return self.array[-1]
        
    def push(self,value):
        self.array.append(value)
        
    def pop(self):
        del self.array[-1]

myStack = Stack()
myStack.push('Amazon')
myStack.push('Google')
myStack.push('Discord')
print(myStack.peek())
myStack.print_stack()
myStack.pop()
myStack.print_stack()
print(myStack.peek())