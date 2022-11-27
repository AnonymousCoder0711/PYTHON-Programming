from cmath import *
a = int(input("a = "))
b = int(input("b = "))
c = int(input("c = "))

neg_val = (-b - sqrt(b**2 - 4*a*c)) / (2*a)
pos_val = (-b + sqrt(b**2 - 4*a*c)) / (2*a)

print(f"The factors of quadratic equation is {pos_val} and {neg_val}")