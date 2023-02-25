class QueueUsingStack():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def peek(self):
        if len(self.s1) == 0:
            print("Queue is empty")
        else:
            print(self.s1[len(self.s1)-1])

    def enqueue(self,value):
        for i in range(len(self.s1)):
            item = self.s1.pop()
            self.s2.append(item)
        self.s1.append(value)
        for i in range(len(self.s2)):
            item = self.s2.pop()
            self.s1.append(item)
        
    def dequeue(self):
        if len(self.s1) == 0:
            print("Queue is empty")
        else:
            self.s1.pop()

    def print_queue(self):
        for i in range(len(self.s1)-1,0,-1):
            print(f"{self.s1[i]}<<-- ",end='')
        print(self.s1[0])   

myQueue = QueueUsingStack()
myQueue.enqueue('Tree')
myQueue.enqueue('Bees')
myQueue.enqueue('Apple')
myQueue.enqueue('Cocoa')
myQueue.print_queue()
myQueue.dequeue()
myQueue.dequeue()
myQueue.print_queue()
myQueue.peek()