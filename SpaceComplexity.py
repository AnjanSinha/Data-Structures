def function(n):
    i = 0       #space is constant as creating a variable takes space 
    for i in range(n):
        print("Boo")

function(6)

#Hence the space complexity will be constant space O(1)

def hiTimes(n):
    hiArray = []    #Creating array that is a data structure that takes space
    for i in range(n):
        hiArray.append('Hi')    #each items taking additional memory space 

    return hiArray

res = hiTimes(5)
print(res)
 
# hence the space complexity will be O(n)