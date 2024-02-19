infile = open('afewlinesofnumbers.txt','r')
#Add all numbers in the file

total = 0
howMany = 0
least=1
highest=0

for line in infile:
    num = line.split()
    for val in num:
        howMany += 1
        number = float(val)
        total = total+number
        print(number)
        if number < least:
            least = number
        elif number > highest:
            highest = number
        else:
            a = 'a'
            
mean = total/howMany
print(total)
print(mean)


print(howMany)

infile.close()

#Put the number of items, total, and mean into an external file
#called statistics.txt.

outfile = open('statistics.txt','w')

print(howMany,total,mean, file = outfile)

outfile.close()






