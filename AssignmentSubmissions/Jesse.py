# CS135 Program 1
# Exchange Rates
# by: Markus Jesse
# 8/28/23

# This program produces a table of currency equivalences between U.S.,
# Canadian, and Mexican currencies.

def main():
    print("U.S. Dollar      Canadian Dollar      Mexican Peso")        #Prints out table headings.
    
    for USD in range(10,71,10):                                        #Evals USD in $10 intervals.
        
        CAD = round(USD*1.317,2)                #Using given rates, exchanges
        MXN = round(USD*16.751,2)               #each USD interval to CAD and MP
        
        print("   $"+str(USD),"              $"+str(CAD),"             $"+str(MXN))  #Prints each value.
    
main()
