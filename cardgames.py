#Card games
from random import shuffle

def makeAdeck():
    #Each card is a pair (suit, rank) expressed numerically ace = 14
    deck = []  #Initialize empty list
    for suit in range(4):
        for rank in range(2,15):
            deck= deck + [(suit,rank)]  #add pair (suit,rank) to deck list
    shuffle(deck)  #shuffle the deck list
    return deck








def splitDeck(deck):
    """Deals the whole deck alternately to two players. Returns the two 26-card decks"""
    alice = []
    bob = []
    
    for i in range(0,52,2):
        alice = alice + [deck[i]]
        bob = bob + [deck[i+1]]
    return alice,bob











def deal(deck,n):
    """deals n cards from a deck.
    returns the n cards and the reduced deck"""
    dealt = []
    rest = []
    dealt1 = [deck[:n]]
    dealt2 = [deck[n:52]]
    for i in range (52):
        if i+1 <= n:
            dealt = dealt + [deck[i]]
        else:
            rest = rest + [deck[i]]
    return dealt,rest,dealt1,dealt2











#A dictionary is a nonsequential data structure
def makeDictionaries():
    suitDict ={0:'Spades',1:'Hearts',2:'Diamonds',3:'Clubs'}
    rankDict ={14:'Ace',13:'King',12:'Queen',11:'Jack'}
    for rank in range(10,1,-1):
        rankDict[rank]=str(rank)
    return suitDict,rankDict









def cardName(card):
    """returns a string naming the card. cardName((1,12)) returns 'Queen of Hearts'"""
    sd,rd = makeDictionaries()
    return rd[card[1]]+' of '+sd[card[0]]
        
        
        
        
        
        
        
        
        
        
        
    pass