infile = open('lotsoflinesofnumbers.txt','r')

line = infile.readline()
newLine = ''
print(line)

for character in infile.read():
    item = ord(character)
    if item == 44:
        newLine = newLine + ' '
    else:
        newLine = newLine + character
        
        
        
        
newnew = newLine.split()


howMany=0
highest = 0
lowest = 0
total = 0

for number in newnew:
    howMany += 1
    val = float(number)
    total = total + val
    if val < lowest:
        lowest = val
    elif val > highest:
        highest = val
    else:
        yes=1
mean = total/howMany
print(howMany,highest,lowest,mean)





infile.close()