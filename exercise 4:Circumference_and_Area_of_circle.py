#Circumference of a circle
import math
Radius= float(input("Enter the number:"))
Coc= 2 * math.pi * Radius
print(f"The circumference of a circle is: {round(Coc, 3)}")

#Result:
#Enter the number:5
#The circumference of a circle is: 31.416

#Area of a circle
import math
R= float(input("Enter the number:"))
Areaofcircle=  math.pi * pow(R, 2) #pow(R, 2) maens square of R
print(f"The area of a circle is: {round(Areaofcircle, 2)}") #round(Areaofcircle, 3) means the output will be upto 2 digits after decimal EX:.54

#Result:
#Enter the number:5
#The area of a circle is: 78.54
