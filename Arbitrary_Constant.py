#Arbitary arguments for multiple arguments
#*args= allows to pass multiple non-key arguments
#**kwargs= allows you to pass multiple keyword arguments
def add(*num):
    print(type(num) ) 
add(1,2,3)

#To display a name
Def add(*args) :
 Total= 0
 For arg in args:
  Print(arg, end= " ") 
Display_name(" Ms.", "Janvi", " Singh") 

#To display address
def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}:{value}")
print_address(state= "Maharashtra"
             City= "Pune"
             Area= "Kalyani nagar")
