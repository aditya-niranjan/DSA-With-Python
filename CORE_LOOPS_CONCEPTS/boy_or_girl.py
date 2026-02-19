


name = input("Enter your name: ")


distict_characters = set(name)  
count = len(distict_characters)

if count % 2 == 0:
    # If even, chat with her
    print(f"{name} has {count} distinct characters.")
    print("CHAT WITH HER!")
else:
    print(f"{name} has {count} distinct characters.")
    print("IGNORE HIM!")  
    # If odd, ignore him

   
    