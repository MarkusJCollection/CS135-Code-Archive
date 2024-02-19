"""
from random import *

x = random() #Finds a random number between 0 and 1

y = choice([1,2,3,4,19,'q']) #Selects a random element from the list

z = randint(3,12) #Returns an integer from the range specified

w = random()*100

print(w)
"""



#Example: Roshambo simulation.


from random import choice

def randomplay():        #Chooses randomly between r, p, and s.
    return choice(['r','p','s'])


def alwaysRock():
    return 'r'


def mostlyRock():
    return choice(['r','r','r','p','s'])


def copyOppLast(oppLastMove):
    return oppLastMove




def playOneGame(strategy1,strategy2,oppLastMove1 = False,oppLastMove2 = False):
    if not oppLastMove1:
        player1 = strategy1()
    else:
        player1 = strategy1(oppLastMove1)
        
        
    if not oppLastMove2:
        player2 = strategy2()
    else:
        player2 = strategy2(oppLastMove2)
    return player1,player2



def scoreTheGame(player1,player2):
    #Assumes that player1 and player2 have already made their play.
    
    winningStrings = ['pr','rs','sp'] #leftmost letter wins
    
    if player1+player2 in winningStrings:
        return 1
    elif player2+player1 in winningStrings:
        return 2
    else:
        return 0
    
    




def simulateNgames(n,strategy1,strategy2,oppLastMove1,oppLastMove2):
    olm1 = oppLastMove1
    olm2 = oppLastMove2
    player1wins = 0
    player2wins = 0
    ties = 0
    for i in range(n):
        p1,p2 = playOneGame(strategy1,strategy2,olm1,olm2)
        result = scoreTheGame(p1,p2)
        if result == 0:
            ties += 1
        elif result == 1:
            player1wins += 1
        else:
            player2wins += 1
        if oppLastMove1:
            olm1 = p2
        if oppLastMove2:
            olm2 = p1
    return player1wins,player2wins,ties

            
            









