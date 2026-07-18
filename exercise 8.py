#temperature convertor from celcius to F and K
C = float(input("Enter the temperature (in Celsius): ")) 

F = (( C * 1.8 ) + 32 ) 
print(f"The temperature (in Fahrenheit) is {F} ") 

K = ( C + 273.15 ) 
print(f"The temperature (in kelvin) is {K} ") 