



with open("log.txt") as f:
  lines = f.readlines()


# lineno = 1

# for line in lines:
#     if("python" in line):
#        print(f"yes python is  present . line No is: {lineno}")
#        break
#     lineno+= 1
# else:
#    print("not python is")
  

user = input("Find the line number based on the Word:")


lineno = 1
index = 0

while index<len(lines):
  line = lines[index]
  if(user in line):
    print(f"the {user} is present , on the line NO: {lineno}")
    break
  index += 1
  lineno +=1
else:
  print(f"the name {user} is not present!!")
    

       

