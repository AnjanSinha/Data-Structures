class DoublyLinkedList:
    def __init__(self,value):
        self.head = {
            'value': value,     #Value
            'next': None ,   #Pointer
            'prev': None
        }
        self.tail = self.head
        self.length = 1

    def __str__(self) :
        return f"Head: {self.head} , Tail: {self.tail}"

    def printList(self):
        array = []
        currentNode = self.head
        while (currentNode!= None):
            array.append(currentNode['value'])
            currentNode = currentNode['next']
        print(array)

    def append(self,value):
        newNode = {
            'value': value,
            'next': None,
            'prev': None
        }
        newNode['prev'] = self.tail
        self.tail['next'] = newNode     #creating pointer for next node
        self.tail = newNode     #The tail is no longer the tail and will update it to the new appended node
        self.length +=1
    
    def prepend(self,value):
        newNode = {
            'value': value,
            'next': None,
            'prev' : None
        }
        newNode ['next'] = self.head    #Creating pointer for next node which is the head for prepend method.
        self.head['prev'] = newNode  
        self.head = newNode     #The head is no longer the head after prepend so we'll update it with our prepended node
        self.length+=1

    def insert(self,index,value):
        if ( index >= self.length):
            return self.append(value)
        newNode = {
            'value' : value,
            'next': None,
            'prev' : None
        }
        leader = self.traverseToIndex(index-1)
        follower = leader['next']
        leader['next'] = newNode
        newNode['prev'] = leader
        newNode['next'] = follower
        follower['prev'] = newNode
        self.length+=1

    def remove(self,index):
        leader = self.traverseToIndex(index-1)
        unWantedNode = leader['next']
        leader['next'] = unWantedNode['next'] 
        follower = unWantedNode['next']
        print(follower)
        if (follower != None):
            follower['prev'] = unWantedNode['prev']

        self.length-=1

    def traverseToIndex(self,index):
        counter = 0 
        currentNode = self.head
        while(counter != index):
            currentNode = currentNode['next']
            counter+=1
        return currentNode

myLinkedList = DoublyLinkedList(10)
myLinkedList.prepend(34)
myLinkedList.insert(1,45 )
myLinkedList.append(356)
myLinkedList.append(90)
myLinkedList.remove(3)
myLinkedList.printList()
print(myLinkedList)