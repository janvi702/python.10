#Types of data types included

#strings
name= "Janvi"
print(f"my name is {name}")
print(type(name))


#integer
age= 20
print(f"I am {age} years old")
print(type(age))


#Float
cgpa= 8.3
print(f"I have a cgpa of {cgpa}")
print(type(cgpa))


#Boolean
is_student= True

if is_student:
    print("you are a student")
else:
    print("you are not a student")

print(type(is_student))


#List- ordered and changeable
b = ["apple", "banana", "orange", 4, 5]
print(b[3])
print(b[-3])
print(type(b)) 

List[]
fruits= ["apple", "banana", "orange", "pineapple"]
print(dir(fruits)) #for the things, the list is able to do
print(help(fruits)) #for different terms that could help
print(len(fruits)) # gives the length
print("apple" in fruits) #a question if apple is in the fruits list(gives boolen output)

fruits[0] = "Plum"
for fruit in fruits:
	print(fruit) #the fruit in the list with index 0 --> apple, will change to plum

#to add an element in the list, we use append
fruits.append("watermelon")
print(fruits)

#to remove an element, use remove
fruits.remove("banana")
print(fruits)

#to insert an element in a given index
fruits.insert(0, "melon")
print(fruits)

#to sort list in alphabetical order
fruits.sort()
print(fruits)

#to reverse a list, use reverse
fruits.reverse()
print(fruits)

#to clear the list, we use clear
fruits.clear()
print(fruits)

#to print the index of an element
print(fruits.index("orange"))

#to count how many duplicates are available
print(fruits.count("orange"))


set{}
fruits= {"apple", "banana", "orange", "pineapple"}
print(dir(fruits)) #for the things, the list is able to do
print(help(fruits)) #for different terms that could help
print(len(fruits)) # gives the length
print("apple" in fruits) #a question if apple is in the fruits list(gives boolen output)

fruits.add("melon") #to add an element in the set
fruits.remove("banana") #to remove an element from set
fruits.pop() # randomly pops an element
fruits.clear() #clears the element



#Tupple- ordered and unchangeable
Fruits = ("apple", "banana", "cherry")
print(Fruits)
print(type(Fruits)) 


#dictionaries- ordered and changeable
Car = {
  "brand": "Ford",
  "model": "Mustang",
  "year": 1964
}
print(Car["brand"])
print(type(Car)) 

#writing things differently
Fruits = ["apple", "banana", "orange"]

