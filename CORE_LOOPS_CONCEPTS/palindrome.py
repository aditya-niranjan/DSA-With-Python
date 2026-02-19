
word = input("Enter a word: ")

is_palindrome = word[::-1]

if is_palindrome == word:
    print("YES the world is a palindrome")
else:
    print("NO the world is not a palindrome")