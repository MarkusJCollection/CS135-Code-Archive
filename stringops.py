"""SOME VOCAB INFO
when you see list1[0]='thing'
0 is the index; 'thing' is the value"""

videoGameChars=["Miles Edgeworth", "Dante from Devil May Cry", "Faendal", "Freddy Fazbear"]
addendum=["Hatsune Miku", "Alice"]

def addingLists(videoGameChars):
    newList=videoGameChars+addendum
    print(newList)
    
def multiplyingLists():
    numList=[2]*8 #will create a list of eight 2s
    badNumList=[2*8] #will create a list of just one 16
    print(numList)
    print (badNumList)
    print(numList.count(2))
    
def indexLists(videoGameChars):
    print(videoGameChars[0]) 
    print("feat. {0}".format(videoGameChars[1]))
    
def loopLists(videoGameChars):
    for c in videoGameChars:
        print("{0} is very cool.".format(c))
        
def ifInList(videoGameChars):
    if "Gideon Olfnir" in videoGameChars:
        print("Gideon Olfnir the All-Knowing is in the list!")
    else:
        print("Gideon Olfnir the All-Knowing is not in the list.")

def otherOps(videoGameChars):
    newList=videoGameChars+addendum
    print(len(newList))
    print(newList[:-2])
    
def methodsofLists(videoGameChars):
    videoGameChars.append("sonic the hedgehog")
    videoGameChars.append("8-bit")
    videoGameChars.append("{")
    videoGameChars.sort() #sorts in ASCII order
    print("After Sort:")
    print(videoGameChars)
    
    videoGameChars.reverse()
    print("After Reverse:")
    print(videoGameChars)
    
    i=videoGameChars.index('sonic the hedgehog')
    videoGameChars.insert(i,'Yukiko Amagi')
    print("After Insert:")
    print(videoGameChars)
    
    a=videoGameChars.remove("{") #removes first instance of "{"; returns nothing
    b=videoGameChars.pop(i) #removes item at index [i], then returns the value
    print("Remove returns: {0}".format(a))
    print("Pop returns: {0}".format(b))
    print("After remove and pop:")
    print(videoGameChars)
    
def listCopyProblem(videoGameChars):
    newList2=videoGameChars #assigns same list to two different names
    newList3=videoGameChars.copy() #copies current videoGameChars list into newList3
    videoGameChars.append('Loba Andrade')
    videoGameChars.append('Alm')
    print("newList2 (using =) is {0}".format(newList2))
    print("newList3 (using .copy()) is {0}".format(newList3))
