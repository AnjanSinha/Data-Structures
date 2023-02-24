#First in First out
class Queue:
    def __init__(self):
        self.first = None
        self.last = None
        self.length = 0

    def __str__(self):
        return f"Queue: {self.first} , Length: {self.length}"
    
    def print_queue(self):
        if self.first == None:
            print("Queue is empty")
        else: 
            currentitem = self.first
            while(currentitem != None):
                print(currentitem['value'])
                currentitem = currentitem['next']

    def peek(self):
        if self.first == None:
            return "Queue is empty."
        else: 
            return self.first['value']
        
    def enqueue(self, value):
        newNode = {
            'value': value,
            'next': None
        }
        if self.length == 0:
            self.first = newNode
            self.last = newNode
        else:
            self.last['next'] = newNode
            self.last = newNode
        self.length+=1

    def dequeue(self):
        if self.first == None:
            return None
        self.first = self.first['next']
        self.length-=1
        
myQueue = Queue()
myQueue.enqueue('Joy')
myQueue.enqueue('Matt')
#print(myQueue.peek())
myQueue.enqueue('Anjan')
myQueue.enqueue('Sinha')
myQueue.print_queue()
print(myQueue)
myQueue.dequeue()
print(myQueue)
