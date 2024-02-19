from math import sqrt

def tryExceptSample():
 while True:
    try:
        a,b,c = eval(input('Enter three numbers a,b,c separated by commas: '))
        try:
            x= sqrt(a/(b-c))
            print( f'sqrt({a}/({b}-{c}) = {x:0.2f}')
            return
        
        except ValueError:
            if b< c:
                print('b must be greater than c. Try again.')
            else:
                print('a cannot be negative. Try again.')
                
        except ZeroDivisionError:
            print('b cannot equal c. Try again.')
    except ValueError:
        print('You need three arguments. Try again.')
    except NameError:
        print('No variables, please. Try again.')
    except TypeError:
        print('Only numbers. No strings. Try again.')
    except SyntaxError:
        print('This input is incorrect. Try again.')
    except:
        print('Something is wrong. Try again.')
    
    print()
    
tryExceptSample()        
    