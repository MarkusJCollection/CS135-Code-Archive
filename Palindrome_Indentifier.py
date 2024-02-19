word = input('Input a potential palindrome: ')
x=-1
no = 0
for letter in word:
    reverse = word[x]
    x = x - 1
    if letter != reverse:
        no = 1
if no > 0:
    print('Not a palindrome')
else:
    print('A palindrome')
    
    
    
    