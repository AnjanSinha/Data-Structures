#rule3- Different terms for inputs
a1 = ['anjan' for i in range(10)]
a2 = ['sinha' for i in range(10)]

def printArray(array1, array2):
    for i in array1:    #depends on array1 inputs and we can say its Big o is O(array1) / O(m)
        print(i)

    for i in array2:    #depends on array2 inputs and we can say its Big o is O(array2) / O(n)
        print(i)

printArray(a1,a2)

#As the inputs for the two operations depends on different types of inputs then 
# The big O of this code will be then O(array1+array2) or we can say O(m+n) 