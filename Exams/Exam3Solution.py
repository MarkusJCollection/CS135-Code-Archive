"""Exam 3
This is a code completion exam. Add code as needed
to fulfill the specifications.  You may not change
any of the code given here except for pass
statements which you may delete"""

"""Question 1"""

def laugh(string, character, num):
    """Replaces every occurrence of character in string by the word
        'ha' repeated num times.  The altered string is returned.
     For example, laugh('Old MacDonald had a lamb','l',2) would
     return 'Ohahad MacDonahahad had a hahaamb'"""
    newstring = ''
    for ch in string:
        if ch == character:
            newch = 'ha'*num
        else:
            newch = ch
        newstring = newstring + newch
    return newstring


"""Question 2"""
def distinctWords():
    """Returns the number of distinct words in the file
       sometext.txt """
    distinct = []
    infile = open('sometext.txt','r')
    for line in infile:
        line = line.lower()
        linelist = line.split()
        for word in linelist:
            if word not in distinct:
                distinct = distinct + [word]
    infile.close()
    return len(distinct)
    

"""Question 3"""

def writenames(numitems,numlines):
    """Creates a file called 'myname.txt' (where myname is your last name) that contains numlines
    lines each with numitems words. Each word is your last name. The words are separated
    by blank spaces.  For example, you can see what Harry Potter's writenames(6,10) produced in the file
    'potter.txt' """
    
    outfile = open('potter.txt', 'w')
    for i in range(numlines):
        for j in range(numitems-1):
            print('potter', end = ' ', file = outfile)
        print('potter', file = outfile)
    outfile.close()
            
    


"""Question 4"""

from random import *
def FiveDiceSim():
    """Simulates rolling five six-sided dice repeatedly until all dice show the same number.
    Returns the number of rolls that were made to acheive that result."""
    rolls = 0
    fivedice = False
    while not fivedice:
        rolls+=1
        die1 = randint(1,6)
        die2 = randint(1,6)
        die3 = randint(1,6)
        die4 = randint(1,6)
        die5 = randint(1,6)
        if die1 == die2 == die3 == die4== die5:
            fivedice = True
            
    return rolls
    






    
    




