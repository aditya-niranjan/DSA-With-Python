# to find the binary number in python and with raw code 


#  to find a binary number in python is easy we can use in built function 


# print(bin("add the number which u want the binary of it's that simple"))

# exaple

print(bin(9))


#  without using the python built in function to calculates we divide the number with 2 and after getting the all remainder we just revrse all the bottom to u , this below program is the the example for that 
num = 35
bit = []

while num:
    remainder = num % 2
    bit.append(remainder)
    num = num // 2

print(bit)              # reversed binary
print(bit[::-1])       # correct binary order

