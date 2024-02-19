"""
#Strings and String Methods

b = 'bumblebee'
for letter in b:
    print(letter, end = ' ')
print()
    
#Slicing
fourthLetter = b[3] #0,1,2,3
fourthTosixth = b[3:6] #3,4,5
print(fourthLetter)
print(fourthTosixth)
print(b[:7]) #0,1,2,3,4,5,6
print(b[5:]) #5,6,7,...
print(b[-1]) #Last letter
print(b[-2]) #Second to last
"""



#Take out first letter, put to end, add ay
def main():
    pigInput = input('What word would you like to pig-latinify: ')
    pigLatin = pigInput[1:] + pigInput[0] + 'ay'
    print (pigLatin)

main()

















