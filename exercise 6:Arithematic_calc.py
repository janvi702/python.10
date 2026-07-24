#python calculator
calc = input("Enter the Operator(+-*/):")
num1= float(input("Enter the first number: "))
num2= float(input("Enter the second number: "))

if calc == "+":
    print(num1 + num2 )
elif calc == "-":
    print(num1 - num2 )
elif calc == "*":
    print(num1 * num2 )
else:
    print(num1 / num2 )
