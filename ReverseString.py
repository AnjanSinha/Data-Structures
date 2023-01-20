#Reverse a Input string   
#"Hi my name is Anjan" should be : "najnA si eman ym iH"
def Reverse(string):
    backwards = []
    for i in range(len(string)-1,-1,-1):        #Creating a reverse list of characters
        backwards.append(string[i])
    print("".join(backwards))       #Joining reverse list of characters

Reverse("Hi my name is Anjan")
#Another method 
def Reverse2(string):
    charlist = [*string]    #Creating list of characters
    charlist.reverse()      #Creating reverse list of charcters
    print("".join(charlist))    #Joining reverse list of characters

Reverse2("Hello have a good day")
#Another method
def Reverse3(string):
    charlist = [i for i in string]    #Creating list of characters
    charlist.reverse()      #Creating reverse list of charcters
    print("".join(charlist))       #Joining reverse list of characters

Reverse3("This is a tree")
#Another method
def Reverse4(string):
    charlist = list(string)    #Creating list of characters
    charlist.reverse()      #Creating reverse list of charcters
    print("".join(charlist))       #Joining reverse list of characters

Reverse4("He is a good boy")
#Another method
def Reverse5(string):
    charlist = [*string]    #Creating list of characters
    charlist.reverse()      #Creating reverse list of charcters
    revString= ""
    for i in charlist:       #Joining reverse list of characters
        revString +=i
    print(revString)

Reverse5("Dada is calling")