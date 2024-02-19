#External text processing

infile = open('captains.txt','r')

text = infile.read()
textlist = text.split()

captainsList = []



for capt in textlist:
    if capt not in captainsList:
        captainsList =  captainsList + [capt]




infile.close()