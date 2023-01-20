class hashtable():
    def __init__(self,size):
        self.data = [None]*size    #Initializing an array of size 'size'

    def __str__(self) :
        return str(self.data)   #This method returns is used to print the class object in a 

    def _hash(self,key):    #Making a manual hash function that generates a hash for us
        hash = 0
        for i in range (len(key)):
            hash = (hash + ord(key[i])*i) % len(self.data)  #ord(key[i]) gives the unicode code point of the character key[i]  and here creating a unique address within the limited array.     
        return hash

    def set(self,key,value):    #functin for setting key value pair
        hash_address = self._hash(key)  #to store the key value pair we need to find out where to put it by using hash function
        if (not self.data[hash_address]):   #If no key and value was there at that location creating a list to put key value pair list
            self.data[hash_address] = []    #Creating an array shelve to store the key value pair array
        self.data[hash_address].append([key, value])    #If other key and value is there the next key value pair list will be put next to it

    def get(self, key):
        hash_address = self._hash(key)
        currentBucket = self.data[hash_address]     #finding the address of the key which value we need to return
        if currentBucket:   #if some value present in that location then 
            for i in range(len(currentBucket)):     #loop over the list of key value pair at that location 
                if (currentBucket[i][0])==key:      #if the key matches any of the key of the key value pair
                    return currentBucket[i][1]      #return the value from the key value pair list  
        return None     #if no value was there return none 
    
    def keys(self):     #Making a function to show only the values in the hash table
        keysArray = []      #Initializing an empty array to store the keys
        for i in range(len(self.data)):     #this will loop through the whole memory array
            if (self.data[i]):      #If the value of the i index is holding something then the loop will continue
                if len(self.data[i])>1:     #If there is hash collision present then we need to print the collision keys too
                    for j in range(len(self.data[i])):      #It will loop through the address length 
                        keysArray.append(self.data[i][j][0])        #The keys of the hash collision will be appended to the new array by looping through the key-value pairs of the same address
                else:       #If there are no hash collisions
                    keysArray.append(self.data[i][0][0])    #The first keys of the first array would be simply appended to the new array
        return keysArray

myHashTable = hashtable(10)
myHashTable.set('grapes',10000)
myHashTable.set('grapess',567)
myHashTable.set('apples',67)
myHashTable.set('oranges',7)
print(myHashTable.get('apples'))
print(myHashTable)
print(myHashTable.keys())