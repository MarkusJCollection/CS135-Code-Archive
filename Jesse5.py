# CS135 Program 5
# Smetale Simulation
# by: Markus Jesse
# 11/1/23

    #Imports the choice function from random to provide a base for calculating what side is tossed.
from random import choice



def toss():
        #Function that randomly returns whether an object is considered face-up, or face-down.
        #1 and 2 is representative to the two faces of crosses and circles, while 3 represents face-down.
    tossOne = choice([1,3])
    tossTwo = choice([1,3])
    tossThree = choice([2,3])
    tossFour = choice([2,3])
    
    
    return tossOne,tossTwo,tossThree,tossFour





def player():
        #Uses previous toss function, and determines whether or not a player receives points based
        #on the orientation of their rolls.
    a,b,c,d = toss()
    
        #Represents whether all objects are face down, or face-up.
    if a == b == c == d or a == b == 1 and c == d == 2:
        points = 2
        
        #Represents the other case of one set being face-up while the other set is face-down.
    elif a == b and c == d:
        points = 1
        
        #d is arbitrarily chosen as the string object, and represents if it
        #shows a face the other 3 are not.
    elif d == 2 and a==3 and b==3 and c ==3 or d == 3 and a !=3 and b !=3 and c !=3:
        points = 4
        
        #Points for all other outcomes are 0.
    else:
        points = 0
        
    
    return points





def poolSubtractor(pool,subtractor):
        #Pool subtractor used to make sure that there aren't
        #more points earned that is what in the pool
    number = pool - subtractor
    
        #If the subtraction would result in a negative, the output of points is
        #equal to the pool, and the pool is set to 0.
    if number < 0:
        points = pool
        pool = 0
        
        #Otherwise the points is whatever will be subtracted and the pool loses that number of items.
    else:
        points = subtractor
        pool -= subtractor
    
    
    return points,pool





def playSmetale(pool=41):
        #Plays the game Smetale between two players, and gives a winner and number of throws to win.
        #Pool amount editable to see how it effects the win overall results.
    
        #Predefining of variables for later use.
    p1Total = 0
    p2Total = 0
    priority = 'p1'
    throws = 0
    
    
        #While there's points in the pool, the game will continue to be played.
    while pool > 0:
            #Each time it is played, a throw is added. Each player is assigned
            #a point total from the previous function.
        throws += 1
        player1 = player()
        player2 = player()
        
        
            #If player 1 has priority, their roll is judged. If they roll positive they
            #earn that number of points, while if they roll a 0 and p2 rolls positive
            #they earn their points and gain priority. If both roll 0 it rerolls for both.
        if priority == 'p1':
            
            if player1 > 0:
                p1p,pool = poolSubtractor(pool,player1)
                p1Total += p1p
                
            elif player2 > 0:
                p2p,pool = poolSubtractor(pool,player2)
                p2Total += p2p
                priority = 'p2'
                
                
            #Same statements as before, except it assumes p2 has priority in rolls
            #and rolls are reversed.
        else:
            if player2 > 0:
                p2p,pool = poolSubtractor(pool,player2)
                p2Total += p2p
                
            elif player1 > 0:
                p1p,pool = poolSubtractor(pool,player1)
                p1Total += p1p
                priority = 'p1'
                
                
        #Determines the winner by seeing who has more points.  
    if p1Total > p2Total:
        winner = 'p1'
        
    else:
        winner = 'p2'
                
            
    return winner,throws





def simulateMany(games=5000,pool=41):
        #Simulates 5000 games of Smetale automatically,
        #with the ability to simulate a custom amount.
    
        #Predefines variables for use later.
    p1wins = 0
    p2wins = 0
    totalThrows = 0
    
    
        #Loop used to play the game the designated number of times.
    for i in range(games):
            #Gets the winner and number of throws from a played game.
        winner,throws = playSmetale(pool)
        
            #Depending on who wins, that player gains a point to their total.
        if winner == 'p1':
            p1wins += 1
            
        else:
            p2wins += 1
            
            
            #Adds the number of throws to an ongoing total.
        totalThrows += throws
        
        #Takes number of throws and games played, and calculates
        #the throw average, and the win percent of player 1 and 2.
    avgThrow = round(totalThrows/games,2)
    p1Percent = round(p1wins/games*100,2)
    p2Percent = round(p2wins/games*100,2)
    
    return print('Player 1 seems to have an advantage with an average win percent of '+str(p1Percent)+'%'+' and '+str(avgThrow)+' average throws in a game.')
        
"""
Extra functionality unnecessary but interesting to see how
increasing the pool amount allows player 2 to have more rolls,
and overall balances out player 1s advantage.
"""






