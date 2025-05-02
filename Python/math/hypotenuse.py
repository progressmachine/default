import math

a = float(input("Enter length of side A: "))
b = float(input("Enter length of side B: "))

print(f"The length of the hypotenuse is {round(math.sqrt(pow(a, 2) + pow(b, 2)), 2)}.")