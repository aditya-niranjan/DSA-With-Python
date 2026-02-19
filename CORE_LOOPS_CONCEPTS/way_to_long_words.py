

word = input("Enter a word: ")


if len(word) >= 10:
    print(word[0] + str(len(word) - 2) + word[-1])
else: 
    print("please try to add more or equal to 10 characters!!")