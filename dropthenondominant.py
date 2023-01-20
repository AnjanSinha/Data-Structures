a1 = [1, 2, 3, 4]

def logPairs(array):
    #printing the numbers
    print("The numbers.")
    for i in array:     #Time complexity will be O(n).
        print(i)
    #printing the sum of the log pairs
    print("The sum of the pair")
    for i in array:     #Time complexity will be O(n^2) , as its a nested loop will same term of inputs.
        for j in array:
            print(i+j)

logPairs(a1)

#So the complexity of the code will be O(n + n^2), but we drop the non-dominant term in big o ,hence the 
#complexity will be O(n^2) , here O(n) is non-dominant because big o consider the worst case and here O(n) is 
#better than O(n^2)