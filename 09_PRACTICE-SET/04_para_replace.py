
from operator import le


word = input("Enter word u want to replace from the file para: ")


with open("para.txt","r") as f:
  content = f.read()


replacement = "#" * len(word)

contentNew = content.replace(word,replacement)




with open("para.txt","w") as f:
  f.write(contentNew)



