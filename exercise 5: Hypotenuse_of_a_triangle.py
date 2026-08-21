#finding hypotenuse of a triangle
import math
#Assigning 2 variables
A= float(input("Enter the side A:"))
B= float(input("Enter the side B:"))
#define a value
C=  math.sqrt(pow(A, 2) + pow(B, 2)) 
#printing the output 
print(f"The side C of the triangle is: {C}")
