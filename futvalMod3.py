# futval.py
#    A program to compute the value of an investment
#    carried 5 years into the future with two interest rates

def main():
    print("This program calculates the future value")
    print("of a 5-year investment.")

    principal = float(input("Enter the initial principal: "))
    apr1 = float(input("Enter the first annual interest rate: "))
    apr2 = float(input("Enter the second annual interest rate: "))
    print()
    print('Principal = $'+str(principal))
    print("APR1 =",apr1)
    print("APR2 =",apr2)
    print("Year       Balance(APR1)      Balance(APR2)")
    print("-"*43)
    principal2 = principal
    for i in range(5):
        principal = principal * (1 + apr1)
        principal2 = principal2 * (1 + apr2)
                                                                    #0    #1        #2
        print(" ${0:1}        ${1:7.2f}         ${2:7.2f}".  format(i+1,principal,principal2))    
        #          ^use 2 places
        #                        ^use 10 places with 2 to right of decimal
    
main()
