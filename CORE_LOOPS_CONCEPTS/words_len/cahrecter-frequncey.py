

word = input("Enter the word: ")


alist  = {}


for char in word:
    if char in alist:
        alist[char] +=1
    else:
        alist[char] = 1


for char in alist:
    print(f"{char}: {alist[char]}. times")

