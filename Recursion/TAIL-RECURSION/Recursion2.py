# Tail Recursion:
# In tail recursion, the recursive call happens **after** all other statements, usually as the **last step**.

count = 0

def fc():
  global count
  if count == 4:
      return
  
  fc(count+1)
  print("Aditya")
fc()