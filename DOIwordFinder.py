infile = open('DOI.txt','r')

words = []
areCount = 0
nonAre = 0
for line in infile:
    words = words + line.split()
for word in words:
    if word == 'are':
        areCount += 1
    else:
        nonAre += 1


print(areCount)


infile.close()


outfile = open('DOI_are_count.txt','w')
print(areCount,file = outfile)
outfile.close()
