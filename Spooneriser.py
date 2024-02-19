spoonerisee = input('Input a two word phrase: ')
wordList = spoonerisee.split()

wordOne = wordList[0]
wordTwo = wordList[1]

newOne = ''
newTwo = ''




for letter in wordOne[1:]:
    newOne = newOne + letter
    
for letter in wordTwo[1:]:
    newTwo = newTwo + letter

finalOne = wordTwo[0] + newOne
finalTwo = wordOne[0] + newTwo

print(finalOne,finalTwo)
