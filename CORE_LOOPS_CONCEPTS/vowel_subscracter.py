


word = input("Enter the your word to find the vowel in it: ").lower()

vowels = 'aeiouAEIOU'

total_vowels = 0

for char in word:
    if char in vowels:
        total_vowels += 1


print(f"In the word {word} there are {total_vowels} vowels are there!!")