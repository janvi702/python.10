#python calculator
#defining variable calc, num1 and num2
calc = input("Enter the Operator(+-*/):")
num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))
#using if, elif and else statements
if calc == "+":
    print(num1 + num2 )
elif calc == "-":
    print(num1 - num2 )
elif calc == "*":
    print(num1 * num2 )
else:
    print(num1 / num2 )
