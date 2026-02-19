

'''


we have to read a file if it containes are we have to read 
that file containe the word twinkle or not if containe we return the 
full and if not then will give the small massegae to it , 
like this is not there in it



'''


f  = open("poem.txt",'r')

content = f.read()

word = input("enetr the word to find in the file: ")


if(word
    in content):
  print(f"yes its there : {word}\n\n{content}")
else:
  print("u don't have such a word that u asking for sorry!!!")

f.close()