from random import randint


#2 12 side die, roll, how long to get doubles


def twelveDie():
    face = randint(1,12)
    return face

def rollTwo():
    die1 = twelveDie()
    die2 = twelveDie()
    return die1,die2

def untilDouble():
    count = 1
    finished = False
    while not finished:
        d1,d2 = rollTwo()
        if d1 == d2:
           finished = True
        else:
            count += 1
    return count

def simN(n):
    total = 0
    for i in range(n):
        total = total + untilDouble()
    avg = total/n
    return avg
