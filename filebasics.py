"""
                  if applicable
open(fileName,fileLocation)
       str type

infile = open(fileName,'r') exists and it's reading it
                        or
outfile = open(fileName,'w') it makes the file

"""



#External Files

infile = open('afewlinesofnumbers.txt','r')

#data = infile.read()   #read captures entire file as one string

#data1 = infile.readlines()   #produces a list whose entries are strings
                              #one string for each line of data


#data2 = infile.readline()     #produces a single line as a string
#data3 = infile.readline()


for line in infile:     #iterates by line through the file
    print(line)





infile.close()