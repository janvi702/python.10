#to print num 100, 200, 300
int x= (100, 200, 300) 
print(x) 

#instead of printing normal variables, we use iterables
li = [100, 200, 300]
it = iter(li)

# Iterate until StopIteration is raised
while True:
    try:
        print(next(it))
    except StopIteration:
        print("End of iteration")
        break