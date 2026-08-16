#To print the elements of a 2D collection in a structured format, we can use nested loops
print("The example of animal 2D collection")
Animals =   [["Tiger", "Lion", "Elephant"], 
            ["Eagle", "Parrot", "Owl"],
            ["Whale", "Octopus", "Shark"]]

for x in Animals:
    for A in x:
        print(A, end=" ")
    print()
    

print("------------------------------")

#To print the elements in a number pad 2D format
print("The example of number pad 2D collection")
Num =   [["1", "2", "3"], 
        ["4", "5", "6"],
        ["7", "8", "9"],
        ["*", "0", "#"]]

for x in Num:
    for A in x:
        print(A, end=" ")
    print()