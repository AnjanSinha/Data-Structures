a1 = ['anjan','sinha','kanchan','rohit','das','barna']

a2 = ['sinha','kanchan','rohit','das','barna','anjan']

def findAnjan(array):

    for i in array:
        print("Running")
        if i == 'anjan':
            print("Found anjan")
            break

findAnjan(a1)   #best case as the result found in first place
findAnjan(a2)   #worst case as result found in last place

#we always consider worst case hence the big o of this code will be O(n)
