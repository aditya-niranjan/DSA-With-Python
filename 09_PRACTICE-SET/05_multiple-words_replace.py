# from operator import le
# from os import replace


# word1 = input("enter the first word which u want to replace: ")
# word2 = input("enter the second word which u want to replace: ")
# word3 = input("enter the thired word which u want to replace: ")
# word4 = input("enter the fourth word which u want to replace: ")

# words = [word1,word2,word3,word4]


# with open("para.txt","r") as f:
#   content = f.read()



# i = 0

# for word in words[i]:
#   if(len(word) == len(words[i])):
#     print("this can't be happen")
#   else:
#     content = content.replace(word,"#" * len(word[i]))

# with open("para.txt","w") as f:
#   f.write(content)


word1 = input("enter the first word which u want to replace: ")
word2 = input("enter the second word which u want to replace: ")
word3 = input("enter the thired word which u want to replace: ")
word4 = input("enter the fourth word which u want to replace: ")

words = [word1, word2, word3, word4]

with open("para.txt", "r") as f:
    content = f.read()


world_list = content.split()


for word in words:
    for original_word in world_list:
        if(original_word == word):
         content = content.replace(original_word,"#" * len(word))
       
with open("para.txt", "w") as f:
    f.write(content)
