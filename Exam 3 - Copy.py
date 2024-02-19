"""Exam 3
This is a code completion exam. Add code as needed
to fulfill the specifications.  You may not change
any of the code given here except for pass
statements which you may delete"""

#Put your name here: Markus Jesse

"""Question 1"""

def laugh(string, character, num):
    """Replaces every occurrence of character in string by the word
        'ha' repeated num times.  The altered string is returned.
     For example, laugh('Old MacDonald had a lamb','l',2) would
     return 'Ohahad MacDonahahad had a hahaamb'"""
    newString = ''
    
    for letter in string:
        if letter == character:
            newString = newString + str('ha'*num)
        else:
            newString = newString + letter
    
    return newString


"""Question 2"""
def distinctWords():
    """Returns the number of distinct words in the file
       sometext.txt """
    
    distinct = []
    
    infile = open('sometext.txt','r')
    
    
    for line in infile:
        sentence = line.split()
        for word in sentence:
            newWord = ''
            for letter in word:
                test = ord(letter)
                if 65<= test <=90:
                    newWord = newWord + chr(test + 32)
                else:
                    newWord = newWord + letter
                   
            if newWord not in distinct:
                distinct = distinct + [newWord]
        
    
    
    infile.close()
    
    
    return len(distinct),distinct

"""Question 3"""

def writename(numitems,numlines):
    """Creates a file called 'myname.txt' (where myname is your last name) that contains numlines
    lines each with numitems words. Each word is your last name. The words are separated
    by blank spaces.  For example, you can see what Harry Potter's makenames(6,10) produced in the file
    'potter.txt' """
    
    
    outfile = open('Jesse.txt','w')
    for j in range(numlines):
        for i in range(numitems):
            print('Jesse', end = ' ', file = outfile)
        print(file = outfile)
        
    
    outfile.close()
    
    
    return print('done')


"""Question 4"""

from random import *

def die():
    face = randint(1,6)
    return face

def FiveDiceSim():
    """Simulates rolling five six-sided dice repeatedly until all dice show the same number.
    Returns the number of rolls that were made to acheive that result."""
    
    counter = 0
    finished = False
    
    
    while not finished:
        
        
        d1,d2,d3,d4,d5 = die(),die(),die(),die(),die()
        
        d1,d2,d3,d4,d5 = randint(1,6),randint(1,6),randint(1,6),randint(1,6),randint(1,6)
        
        
        
        if d1 == d2 == d3 == d4 == d5:
            counter += 1
            finished = True
        else:
            counter += 1
        
    
    return counter






    
    




