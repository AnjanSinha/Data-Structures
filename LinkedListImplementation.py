#Creating linked list for 10-->5-->16
#myLinkedList = {
 #   'head':{
  #      'value': 10,
   #     'next': {
    #        'value':5,
     #       'next': {
      #          'value': 16,
       #         'next': None
        #    }
        #}
    #}
#}
class LinkedList:
    def __init__(self,value):
        self.head = {
            'value': value,     #Value
            'next': None    #Pointer
        }
        self.tail = self.head
        self.length = 1

    def __str__(self):
        return f"Linked List : {self.head} , Tail : {self.tail} , Length : {self.length}"

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
            'next': None
        }
        self.tail['next'] = newNode     #creating pointer for next node
        self.tail = newNode     #The tail is no longer the tail and will update it to the new appended node
        self.length +=1
    
    def prepend(self,value):
        newNode = {
            'value': value,
            'next': None
        }
        newNode ['next'] = self.head    #Creating pointer for next node which is the head for prepend method.
        self.head = newNode     #The head is no longer the head after prepend so we'll update it with our prepended node
        self.length+=1

    def insert(self,index,value):
        if ( index >= self.length):
            return self.append(value)
        newNode = {
            'value' : value,
            'next': None
        }
        leader = self.traverseToIndex(index-1)
        holdingPointer = leader['next']
        leader['next'] = newNode
        newNode['next'] = holdingPointer   
        self.length+=1

    def remove(self,index):
        leader = self.traverseToIndex(index-1)
        unWantedNode = leader['next']
        leader['next'] = unWantedNode['next']
        self.length-=1

    def traverseToIndex(self,index):
        counter = 0 
        currentNode = self.head
        while(counter != index):
            currentNode = currentNode['next']
            counter+=1
        return currentNode
    
    def reverse(self):
        if not self.head['next']:
            return self     #If there is only one element in the list then simply return that 
        first = self.head   #keeping track (reference) of the first item 
        self.tail = self.head    #As the list will reverese the first item will be the last item after reverse so updating the tail as the current head
        second = first['next']  #keeping track (reference) of the second item
        while ( second ) :  #As long as the second is not none value
            temp = second['next']   #Reference of third item
            second['next'] = first  #Second item pointer will now point to the first item
            first = second  #First item will now replaced with the second item
            second = temp   #And the second item reference will hold the third item as a reference
        self.head['next'] = None    #At last the pointer of the last item which was the first item at beginning will updated to NONE
        self.head = first   #And the head will updated to the current first item that is the last item at the beginning
    
myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.prepend(1)
myLinkedList.insert(2,45)
myLinkedList.remove(3)
myLinkedList.printList()
print(myLinkedList)
myLinkedList.reverse()
myLinkedList.printList()
print(myLinkedList)