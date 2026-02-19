# testing where two files are identicleor not then see what happens with they match identicaly


from ctypes.wintypes import PINT


with open("this.txt") as f:
  content1 = f.read()


with open("log.txt") as f:
  content2 = f.read()


  if(content1 == content2):
    print("the both are identical")
  else:
    print("both are NOt identical")

# out put of this prints the not identical beacuse they don't have any 
# such same content in it




with open("this.txt") as f:
  content3 = f.read()


with open("copy_this.txt") as f:
  content4 = f.read()


  if(content3 == content4):
    print("the both are identical")
  else:
    print("both are NOt identical")


# out put of this prints the both identical beacuse they  have the same to 
# same  content in it


