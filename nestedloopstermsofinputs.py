#logallpairs
a1 = [1, 2, 3, 4]

def logPairs(array):
    for i in array:     
        for j in array:     #same input but nested loops
            print(i,j)

logPairs(a1)

#big o will be O(n*n) = O(n^2) , variable name is same because of same input elements, for different input elements 
#variable will be different then the big  o will be O(m*n) 