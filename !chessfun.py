##8x8 GRID
"""

A8 B8 C8 D8 E8 F8 G8 H8
A7 B7 C7 D7 E7 F7 G7 H7
A6 B6 C6 D6 E6 F6 G6 H6
A5 B5 C5 D5 E5 F5 G5 H5
A4 B4 C4 D4 E4 F4 G4 H4
A3 B3 C3 D3 E3 F3 G3 H3
A2 B2 C2 D2 E2 F2 G2 H2
A1 B1 C1 D1 E1 F1 G1 H1









Color- 0 = black 1 = white


"""
chessboard = [['A8', 'B8', 'C8', 'D8', 'E8', 'F8', 'G8', 'H8'], ['A7', 'B7', 'C7', 'D7', 'E7', 'F7', 'G7', 'H7'], ['A6', 'B6', 'C6', 'D6', 'E6', 'F6', 'G6', 'H6'], ['A5', 'B5', 'C5', 'D5', 'E5', 'F5', 'G5', 'H5'], ['A4', 'B4', 'C4', 'D4', 'E4', 'F4', 'G4', 'H4'], ['A3', 'B3', 'C3', 'D3', 'E3', 'F3', 'G3', 'H3'], ['A2', 'B2', 'C2', 'D2', 'E2', 'F2', 'G2', 'H2'], ['A1', 'B1', 'C1', 'D1', 'E1', 'F1', 'G1', 'H1']]
for i in chessboard:
    print(i, end='\n')

class pawn():
    
    def __init__(self,color=1,position=['A',1],promote=False,firstMove=False):
        self.firstMove = firstMove
        self.promote = promote
        self.position = position
        self.color = color
        
    def move(self,amount=1):
        position = self.position[1]
        if amount == 1:
            bounds = [1,8]
        else:
            bounds = [2,7]
        if self.color == 1:
            if position >= bounds[1]:
                return 'imposs'
            else:
                newPosition = int(position+amount)
        else:
            if position <= bounds[0]:
                return 'imposs'
            else:
                newPosition = int(position+amount)
        self.position[1] = newPosition
        return self.position
    
 
        
        
        
        
test=pawn()
test.move()
print("FSM:",test.firstMove,"PRM:",test.promote,"POS:",test.position)

position = ['A',3]

