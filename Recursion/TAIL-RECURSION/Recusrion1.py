# Tail Recursion:
# In tail recursion, the recursive call happens **after** all other statements, usually as the **last step**.

count = 0

def fc():
  global count
  if count == 10:
      return
  count+=1
  fc()
  print("Aditya")
fc()