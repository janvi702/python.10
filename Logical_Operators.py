#logical statements

#OR logical operator
Temp = 20
is_raining = False

if Temp > 30 or Temp < 12 or is_raining:
    print("the weather is not stable... be careful!")
else:
    print("the weather is stable... enjoy your day!")
    
#AND logical operator
adhar_card = True
pan_card = False

if adhar_card and pan_card:
    print("Access Granted")
else:
    print("Access denied")

#NOT logical operator
exam_passed = False

if not exam_passed:
    print("Sorry! Try again next time...")
else:
    print("Congratulations! you passed..")
