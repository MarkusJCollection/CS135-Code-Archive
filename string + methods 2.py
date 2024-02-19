


"""

def main():
    sentence = input('Sentence to Piglatinfy: ')
    wordlist = sentence.split()
    for word in wordlist:
       pigWord = word[1:]+word[0]+'ay'
       print(pigWord, end = ' ')

main()
"""
"""
def main():
    sentence = input('Sentence to Piglatinfy: ')
    wordlist = sentence.split()
    newSentence = ''
    
    for word in wordlist:
       pigWord = word[1:]+word[0]+'ay'
       newSentence = newSentence + pigWord + ' '
       
    print(newSentence[:-1])

main()
"""


"""

#Replace certain letters

bob = 'bumblebee'
newbob = bob.replace('e','*')

#Change to uppercase
bobUp = bob.upper()
#bobLower = bob.lower()

#Character counting
howManyb = bob.count('b')
howMany_um = bob.count('um')
    
#Find a character
where = bob.find('e') #Finds only the first occurence of the letter.

#How long is the string?

howLong = len(bob)

"""


sentence = input('Enter an offensive sentence to geese: ')

wordList = sentence.split()
new = sentence.replace('duck','goose')

for word in wordList:
    print(word)
    

















