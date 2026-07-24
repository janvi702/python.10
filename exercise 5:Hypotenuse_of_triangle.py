#finding hypotenuse of a triangle
import math

A= float(input("Enter the side A:"))
B= float(input("Enter the side B:"))

C=  math.sqrt(pow(A, 2) + pow(B, 2)) 

print(f"The side C of the triangle is: {C}")

#Result:
#Enter the side A:3
#Enter the side B:4
#The side C of the triangle is: 5.0
