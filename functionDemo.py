def doubler(x):
    """Doubles the input. Assumes that x is numeric"""
    x=2*x
    return x

def largest(lst):
    """Finds the largest value in a list. Assumes that lst is a
        list of numeric types"""
    big=lst[0]
    for n in lst:
        if n>big:
            big=n
    return big

def smallest(lst):
    """Finds the smallest value in a list. Assumes that lst is a
        list of numeric types"""
    
    small=lst[0]
    for n in lst:
        if n<small:
           small=n
    return small

def either(lst,fnc):
    """Applies a function (func) to a list (lst)"""
    return fnc(lst)


def finder(lst,item):
    """Decides if an item is in a list(lst) """
    
    for k in lst:
        if type(k) == type(item) and k==item:
            return True
    return False

def adder():
    """Adds a collection of values entered by the user"""
    total=0
    more='y'
    while more=='y':
        n=eval(input('Enter a number: '))
        total=total+n
        more=input('More? (y/n) ')
    return total

def avgfile(filename,comma=False):
    """finds the average value of a collection of numerics in a file (filename)"""
    infile = open(filename, 'r')
    total = 0
    count = 0
    for line in infile:
        if not comma:
            linelist = line.split()
        else:
            linelist = line[:-1].split(',')
        for item in linelist:
            total = total + float(item)
            count +=1
    infile.close()
    average = total/count
    print( round(average,4))
    