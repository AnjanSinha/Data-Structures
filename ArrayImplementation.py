class MyArray():
    def __init__(self):
        self.length = 0
        self.data = {}

    def __str__(self):
        return f"MyArray Length : {self.length}, Data : {self.data}"

    def get(self,index):
        return self.data[index]

    def push(self,item):
        self.data[self.length] = item
        self.length+=1
        return self.length

    def pop(self):
        lastItem =  self.data[self.length-1]
        del self.data[self.length-1]
        self.length-=1
        return lastItem

    def delete(self,index):
        item = self.data[index]
        self.shiftItems(index)
        return item

    def shiftItems(self,index):     #O(n) operation
        for i in range(index,self.length - 1):
            self.data[i] = self.data[i+1]
        del self.data[self.length-1]
        self.length-=1

    def insert(self,index,item):        #O(n) operation
        self.length+=1
        for i in range(self.length-1,index,-1):
            self.data[i] = self.data[i-1]
        self.data[index] = item

arr = MyArray()

arr.push("Anjan")
arr.push("Sinha")
arr.push("Place")
arr.push("Haldia")
arr.delete(1)
arr.insert(1,'Prasad')
arr.insert(2,'Sinha')
print(arr)