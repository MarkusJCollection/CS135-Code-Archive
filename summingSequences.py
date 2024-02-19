
#Summing a sequence

n = int(input("How many terms to sum? "))
"""
#Example 1
# 1 + 1/2 + 1/3 + 1/4 + 1/5 + ...
total = 0
for i in range(n):
    total = total + 1/(i+1)
print("Example 1 total:",total)

input("Enter to go on")
#Example 2
# 1 + 1/2 + 1/4 + 1/8 + 1/16 + ...
total = 0
for i in range(n):
    total = total + 1/(2**i)
print("\nExample 2 total:",total)

input("Enter to go on")
#Example 3
# 5 - 5/2 + 5/4 - 5/8 + 5/16 + ...
total = 0
for i in range(n):
    total = total + ((-1)**i)*5/(2**i)
print("\nExample 3 total:",total)

input("Enter to go on")
#Example 4
# sin(pi/2)+sin(pi/4)+sin(pi/9) +...
from math import pi,sin
total = 0
for i in range(n):
    total = total + sin(pi/(i+1))
print("\nExample 4 total:",total)

"""
#Example 5
# 1 + 1/4 + 1/9 + 1/16 + ...
total = 0
for i in range(n):
    total = total + 1/(i+1)**2
print("Example 5 total:",total)

from math import pi

#Compare Example 5 sum to pi*pi/6
print("pi*pi/6 =",pi*pi/6)
print("\nDifference between Example 5 sum and pi*pi/6")
print(abs(total - pi*pi/6))

