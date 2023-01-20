#Merging two sorted arrays.
def mergeSorted(arr1, arr2):
    #Check input
    if (len(arr1) == 0):
        return arr2
    elif (len(arr2) == 0):
        return arr1

    mergedArr = []  #Creating an empty array
    firstArrIndex = secondArrIndex = 0   #Initializing the indexes with value 0.
    flag = 0
    #The loop will run until either of the array are empty.
    while( not (firstArrIndex >= len(arr1) or secondArrIndex >= len(arr2))):
        #Comparing two array elements and pushing them to new array.
        if arr1[firstArrIndex] <= arr2[secondArrIndex]:
            mergedArr.append(arr1[firstArrIndex])
            firstArrIndex += 1
        else:
            mergedArr.append(arr2[secondArrIndex])
            secondArrIndex += 1
    #Checking which array's end was reached.
    if firstArrIndex >= len(arr1):
        flag = 1    #if its first array then 1 will be assigned to the flag and if its second array then flag value will remain 0.

    if flag == 1:     #when flag value is 1 remaining items of second array will be pushed to new array.
        for item in arr2[secondArrIndex:]:
            mergedArr.append(item)
    else :      #when flag value is not 1 means 0 ,  remaining values of first array will be pushed to new array.
        for item in arr1[firstArrIndex:]:
            mergedArr.append(item)

    return mergedArr

print(mergeSorted([30,45,89],[9,34,53]))