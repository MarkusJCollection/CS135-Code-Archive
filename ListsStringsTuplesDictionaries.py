#Lists, strings, tuples, and dictionaries

alist = [1,2,14,7,'p',12]   #brackets
astring = 'gobbledegook'    #quotes
atuple = (2,8)				#parentheses
adictionary = {1: 1, 5: 25, 11:121}  #braces  key:value

#lists, strings, and pairs are sequential, dictionaries are not

print('alist[5] =',alist[5])
print('astring[5] = ',astring[5])
print('atuple[1] =',atuple[1])
print('adictionary[5] = ', adictionary[5])

#strings and tuples do not support item assignment
alist[2] = 'pop'
adictionary[11]=76
print(alist, adictionary)
#you can't do this:  astring[5]='x'
#or this: atuple[0] =77

#Only dictionaries allow creation of new keys
adictionary['bob']=123
print(adictionary)

#You can't do this: alist[7]=9

#You can slice a list or string, but you can't slice a dictionary.
print(alist[1:3])
print(astring[1:3])

#adictionary[:5] is meaningless

#You can iterate through all of these
for x in alist:
    print(x, end = ' ')
print()
for x in astring:
    print(x, end=' ')
print()
for x in atuple:
    print(x, end=' ')
print()
for x in adictionary: #key, but not value!
    print(x, end=' ')

