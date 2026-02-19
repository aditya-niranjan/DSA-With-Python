str = "hello guys this is writing this stringin the file in hello.txt" 




writer = open("hello.txt", "w")
writer.write(str)



f = open("file.txt", "w")
f.write(str)  
writer.close()