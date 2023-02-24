#Last in First Out
class Stack:
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

    def print_stack(self):
        if self.top == None:
            print("Stack is empty")
        else:
            currentPointer = self.top
            while(currentPointer!= None):
                print(currentPointer['value'])
                currentPointer = currentPointer['next']

    def peek(self):
        if self.top == None:
            return None
        return self.top['value']
    
    def push(self,value):
        newNode = {
            'value': value,
            'next': None
        }
        if self.length == 0:
            self.top = newNode
            self.bottom = newNode
        else:
            holdingpointer = self.top
            self.top = newNode
            self.top['next'] = holdingpointer
        self.length +=1 
    
    def pop(self):
        if self.top == None:
            return None
        if self.bottom == self.top :
            self.bottom = None
  
        self.top = self.top['next']
        self.length -=1
        
            
myStack = Stack()
myStack.push('Google')
##myStack.push('Facebook')
#myStack.push('Amazon')

myStack.print_stack()
myStack.pop()
myStack.print_stack()
print(myStack.bottom)