
def func(x,n):
   
   if x>n:
      return

   print(x)
   func(x+1,n)

func(1,5)