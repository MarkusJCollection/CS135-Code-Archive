#War Simulation
from random import shuffle
def makeAdeck():
    #Each card is a pair (suit, rank) expressed numerically ace = 14
    deck = []
    for i in range(4):
        for j in range(2,15):
            deck= deck + [(i,j)]
    shuffle(deck)
    return deck

#deck[0] will be considered the top of the deck
def splitDeck(deck):
    alice = []
    bob = []
    for i in range(0,51,2):  #Deals cards alternatively to alice and bob
        alice = alice +[deck[i]]
        bob = bob + [deck[i+1]]
    return alice, bob

def deal1(deck):  #returns top card of deck and removes it from deck
    card = deck[0]
    deck = deck[1:]
    return deck, card

def play1(a,b):  #a is alice's deck, b is bob's deck, ca is alice's deck, cb is bob's deck
   a,ca = deal1(a)
   b,cb = deal1(b)
   if ca[1] > cb[1]:  #if alice's card has higher rank than bob's
       a = a + [ca]+[cb] #alice gets the cards
   elif ca[1]<cb[1]:  #if bob's card has higher rank than alice's
       b = b + [cb]+[ca] #bob gets the cards 
   else:   #if the cards have the same rank each player gets their card back
       a = a+[ca]
       b = b + [cb]
   return a,b    #returns each player's deck

def simulate():
    x= makeAdeck()
    a,b = splitDeck(x)
    count = 0
    while len(a) > 10 and len(b)> 10:
        a,b = play1(a,b)
        count+=1
    if len(a)>len(b):
        return 1,count
    else:
        return 2,count

def simulateN(n):
    player1 = 0
    player2 = 0
    count = 0
    for i in range(n):
        p,c = simulate()
        if p ==1:
            player1+=1
        else:
            player2+=1
        count = count + c
    print('The average number of throws per game was {0:0.2f}.'.format(count/n))
    print('Player 1 won {0:0.2f}%'.format(player1/n*100))

def main():
    simulateN(5000)
    print("My simulations don't indicate a big advantage to going first.")
    
      
    