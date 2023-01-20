#Google interview question
sample1 = [2,5,1,2,3,5,1,2,4]   #should return 2
sample2 = [2,1,1,2,3,5,1,2,4]   #should return 1

def firstRecChar(arr):
    dictionary = dict()
    for item in arr:
        if item in dictionary:
            return item 
        else:
            dictionary[item] = True
    return None

print(firstRecChar(sample1))

#The time complexity will be O(n) as we are looping through the array once and the searching in dictionary is O(1), 
#its basically an implementation of hash table
#The space complexity is O(n) coz a dictionary is created