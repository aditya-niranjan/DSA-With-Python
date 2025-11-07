# Head Recursion:
# In head recursion, the recursive call happens **before** any other statement in the function.



# print my name aditya 5 times using the Recusrion
count = 0
def greet():
    global count
    if count == 5:
        return

    print("aditya")
    count+=1
    greet()



greet()

  