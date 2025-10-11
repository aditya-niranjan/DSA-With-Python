s = 'nitin'

def func(s,left,right):
  if left>=right:
      return True
  if s[left] != s[right]:
     return False
  return func(s,left+1,right-1)
print("palindrome" if func(s,0,len(s)-1) else "Not palindrome")
