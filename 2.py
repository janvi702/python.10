#the conditional statement includes if, elif and else
#the "else" conditional will be executed, when "if" and "elif" statement becomes false

a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")


#conditional expression
#example1
num1 = 10
num2 = 20

max_num= num1 if num1 > num2 else num2
print(f"the maximum number is: {max_num}")

#example2
age = 44
result= "adult" if age >=18 else "child"
print(result)