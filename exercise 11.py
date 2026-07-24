# This program takes a list of items and their corresponding prices, then calculates the total bill.
Item = input("Enter items separated by spaces: ").split()
Price = list(map(int, input("Enter numbers separated by spaces: ").split()))

print("Your list:", Item)
print("Your number list:", Price)

total = sum(Price)
print(f"Your total bill is {total}")