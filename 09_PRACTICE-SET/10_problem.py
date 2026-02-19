
with open("crash.txt") as f:
  content1 = f.read()


user = int(input("ENter random number to try to delet the file using this numebr"))


num_check = 20

if(user <= num_check):
  with open("crash.txt","w") as f:
    f.write("")
else:
  print("u can't delet the conetnt bro try to add brocode!!!")
 



