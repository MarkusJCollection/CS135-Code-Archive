#An interactive program that says hello

def hello():
    name = input("Hello, what is your name? ")
    print("I am happy to meet you",name)
    print()
    team = input("What is your favorite sports team "+ name + "? ")
    print()
    for i in range(3):
        print("Go",team+"!")
hello()   
    