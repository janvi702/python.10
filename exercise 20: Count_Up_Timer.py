import time
#defining a function to count
def count(start, end):
        #using for loop to add (end=1) number one by one
    for x in range(start, end+1):
        print(x)
            #sleep time will be of 1 second
        time.sleep(1)
            #At last, the line will print "Congratulationssssss"
    print("Congratulationssssss!")
#defining the starting and ending time
count(1, 10)
