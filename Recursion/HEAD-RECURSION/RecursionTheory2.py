
# Head Recursion:
# In head recursion, the recursive call happens **before** any other statement in the function.


def greet(count): 
    if count == 5:
        return

    print("aditya")
    greet(count+1)

greet(0)
