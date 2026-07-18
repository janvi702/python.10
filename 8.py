username= input("Enter the username: ")

if len(username) > 12:
    print("The username cannot be more than 12 characters")
elif not username.find(" ")== -1:
    print("The username cannot contain space")
elif not username.isalpha():
    print("The username cannot contain number")
else:
    print(f"Welcome {username}")