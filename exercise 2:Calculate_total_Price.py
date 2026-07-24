#We include 3 parameters: item, price and quantity
item = input("enter the name of the item: ")
price = float(input("enter the price of the item: "))
quantity = int(input("enter the quantity of the item: "))  
total = price * quantity
print(f"the total of {item} : {total}")
