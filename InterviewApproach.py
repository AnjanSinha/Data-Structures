# We are given two arrays. We have to find if these two arrays contain any matching elements.
# For example, array1 = ['a','b','c','x'] , array2 = ['x','y','z']
# This should return True as element 'x' appears in both arrays.

# Now, the very first solution that comes to mind is the naive, or brute force solution.
# So let's code that down.

array1 = ['a','b','c','x']
array2 = ['x','y','z']

def containsCommonItems(arr1, arr2):
    for i in arr1:
        for j in arr2:
            if i == j :
                return True     #return exits a funtction with a value if matched
    return False

#result = containsCommonItems(array1, array2)
#print(result)

#Space complexity of O(1) because in this solution we are not creating any new variables here just using the inputs.
#At first glance the time complexity looks like O(n^2) but since there are two different 
# variables in the form of array1 and array2,
# The complexity actually is O(m*n), which is equally bad.

#This is a good first solution to come up with but we can easily recognize here that as the input size gets large,
#This function becomes very inefficient.
#So we need to come up with something better.

#One solution can be creating a dictionary for one of the arrays and then looping over the other array
#To check if any of its elements are present in the dictionary's keys.
#Dictionaries are implemented as hash tables in python, and the time complexity for look-ups or searching for an item, is O(1).
#Therefore, the dictionary can be created in O(n) time and then we loop over one array of size say m,
#Where we check for every element if it is present in the dictionary's keys, which is an O(1) operation.
#Therefore, the overall complexity of the function becomes, O(n + m*1) = O(m+n)
#Which is significantly better than our previous function.

def smarterMatching(arr1, arr2):
    dictionary = dict()

    #Looping through first array and creating dictionary for the first array with true values
    for i in range(len(arr1)):
        dictionary[arr1[i]] = True

    #Now loop through second array to check if any of array2 elements are present in created dictionary
    for j in range(len(arr2)):
        if array2[j] in dictionary:
            return True
    return False

#print(smarterMatching(array1, array2))

#The space complexity of this code is O(n) as we are creating a new dictionary here and each items in dictionary takes
#additional memory space
#If the two arrays given are large, then this solution is better than the previous solution in order to time complexity.
#Dont use confusing variable names such as if the arrays has some specified meaning like array1 is for "UserName" and 
#array2 is used for "id"

#In this solution, we've made a number of asssumptions, like there will be no repitions of any element in an array,
#Or that our function will receive exactly 2 inputs which will be arrays.
#Now that we have come up with a better solution in terms of time complexity, we can look to iron out the minor flaws.
#Let's make our function such that it can receive arrays with repititve elements, and if it receives anything other than two arrays
#It gives an error message instead of just crashing out.

def smarterMatching2(arr1, arr2):
    try:
        dictionary = dict()
        for i in range(len(arr1)):
            if i not in dictionary:
                dictionary[arr1[i]] = True


        for j in range(len(arr2)):
            if arr2[j] in dictionary:
                return True
        
        return False

    except TypeError:
        return "Please enter two arrays."

print(smarterMatching2(array1, 0))      #it receives anything other than array so it could'nt executed the "try" block
                                        #and as the error happens in try block it executes the "except block"
