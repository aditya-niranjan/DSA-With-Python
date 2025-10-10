# Recusrion with the use of parameters

# print 1 TO N Using the Recursion

def func(x,n):
    if n == 0:
        return
    print(x)
    func(x+1,n-1)

func(1,10)