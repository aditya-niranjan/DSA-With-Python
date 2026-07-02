
str = "aditya"


vowels = "aeiouAEIOU"


def find(str):
  count = 0 
  for char in str:
      if char in vowels:
         count+=1
      else:
         count-=1
  return count
  

print(find(str))