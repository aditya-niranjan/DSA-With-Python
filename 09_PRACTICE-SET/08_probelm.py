
# this is open the file which u wanted and reading mode

with open("this.txt","r") as f:
  data = f.read()

# this is writing the data or the content of the this.txt in the new file which we
# naming ans the copy_this.txt, it will create new file with this name and also it will 
# replacate this all same data or conatent in it

with open("copy_this.txt","w") as f:
  f.write(data)


