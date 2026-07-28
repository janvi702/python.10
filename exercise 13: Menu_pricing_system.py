#Defined all the menu, cart and total
menu = {"crispy veg + coke" : 79,
        "2 crispy veg" : 79,
        "crispy chicken + coke" : 99,
        "2 crispy chicken" : 99}

cart = []
total = 0 

#Menu will be printed in a format of key_value format

print("----------MENU---------")
for key, value in menu.items():
    print(f"{key:10}: {value:.2f}")
print("------------------------")

#used while loop to get input from user multiple times
while True:
    food = input("select an item (q or quit): ").lower()
    if food == "q":
        break
    elif menu.get(food) is not None:
        cart.append(food)

#Addition of prices of the items that are available on menu's list

print("------------------------")
for food in cart:
    total += menu.get(food)
    print(food, end='')
print()
print(f"The total is: {total}")
