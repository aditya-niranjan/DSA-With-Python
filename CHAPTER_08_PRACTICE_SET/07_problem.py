# We want to:

# Remove all items in the list equal to "an".

# From the remaining items, try to remove "an" from their beginning or end using strip("an").







list = ["an", "an", "an", "banana", "an", "orange", "an", "an", "an" ,"aditya"]

word = input("Enter a word to remove: ")

def remove(list,word):
    n = []
    for item in list:
        if not(item == word)  :
            n.append(item.strip(word))    
    return n
print(remove(list,word))

