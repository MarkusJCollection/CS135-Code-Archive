# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = float(input("Enter the initial principal: "))
    apr1 = float(input("Enter the annual interest rate: "))
    apr2 = float(input("Enter second annual interest rate: "))
    
    
    
    for i in range(10):
        principal = principal * (1 + apr1)
        principal = principal * (1 +apr2)
    print("The value in 10 years is:", round(principal,2))

main()
