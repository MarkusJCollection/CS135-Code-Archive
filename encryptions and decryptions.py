plainText = input('enter encryption input: ')
print()
shift = int(input('Number of shifts: '))
print()


#encryption
cipherText = ''

for letter in plainText:
    
    if ord(letter) == 32:
        newLetter = ' '
  
    else:
        shiftNum = (ord(letter)+shift)
        while shiftNum > 122:
            shiftNum = shiftNum-26
            
        newLetter = chr( shiftNum )
        
      
    cipherText = cipherText + newLetter
    
    
print(cipherText)
print()


#decryption-

decipher = ''
for letter in cipherText:
    if ord(letter) == 32:
        newLetter = letter
    else:
        shiftNum = ord(letter)-shift
        while shiftNum < 97:
            shiftNum = shiftNum + 26
        newLetter = chr(shiftNum)
        
    decipher = decipher + newLetter
print(decipher)