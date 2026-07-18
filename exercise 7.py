#Body Mass Index Calculator
weight= float(input("Enter the body weight(kg):"))
height= float(input("Enter the body height(m):"))
height= pow(height, 2)

BMI= (weight/ height)
print(f"Your Body Mass Index is:{round(BMI, 3)}")
if BMI < 18.5:
    print("you are Underweight... Go eat something!!")
elif 18.5 <= BMI <= 24.9:
    print("you have a healthy weight... yeee")
elif 25.0 <= BMI <= 29.9:
    print("you are overweight....Go hit the gym!!")
else:
    print("you are obese...Go see a doctor")