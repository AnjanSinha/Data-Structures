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
            'value': value,
            'next': None
        }
        self.tail = self.head
        self.length = 1

    def __str__(self) :
        return f"LinkedList: {self.head}, Tail: {self.tail}, Length: {self.length}"

    def append(self,value):
        newNode = {
            'value': value,
            'next': None
        }
        self.tail['next'] = newNode
        self.tail = newNode
        self.length +=1
        
myLinkedList = LinkedList(10)
myLinkedList.append(5)
myLinkedList.append(16)
print(myLinkedList)