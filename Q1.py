file = 'bigdata.txt'
infile = open(file,'r')
numbers = infile.read()
infile.close()
numbers = numbers.split()

found = False
special = None
tilCount = 0
afterCount = 0

for i in numbers:
    if i == '-1':
        found = True
    elif found == True:
        special = i
        afterCount +=1
        found = False
    elif special != None:
        if i == special:
            afterCount+=1
    else:
        tilCount+=1
        
befCount = 0
for i in numbers[:tilCount]:
    if i == special:
        befCount += 1
        
totalCount = befCount + afterCount
print('{0} appeared {1} times in {2}'.format(special,totalCount,file))