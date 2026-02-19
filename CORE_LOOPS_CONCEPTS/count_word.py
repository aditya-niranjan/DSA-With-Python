# count word withoutuseing split() function

sentence = input("Enter your sentence: ")

word_count = 0
in_word = False

for char in sentence:
    if char != " ":
        if not in_word:
            word_count += 1
            in_word = True
    else:
        in_word = False

print(f"The total number of words in your sentence is: {word_count}")
