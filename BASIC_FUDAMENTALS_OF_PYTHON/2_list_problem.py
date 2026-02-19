
names = ["Alice", "Bob", "Charlie", "David", "Eve"]


username = input("Enter a username: ")

if(username in names):
    print("Username already exists.", username)
else:
    print("not in the list")