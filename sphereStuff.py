# Volume and serface area of a sphere
# by Sabine Wren
# September 15, 2023

from math import pi


print("This program computes the volume and surface area of a sphere")
print()
r = float(input("Please enter the radius of the sphere: "))

volume = 4.0/3.0 * pi * r**3
area = 4 * pi * r**2

print("The volume is", round(volume,2), "cubic units.")
print("The surface area is", round(area,2), "square units.")



