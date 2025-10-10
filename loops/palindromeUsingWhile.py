




s = "NITIN"
l = 0
r = len(s) - 1
is_palindrome = True  

while l < r:
    if s[l] != s[r]:
        is_palindrome = False
        break
    l += 1
    r -= 1

# Ternary operator in Python
print("Palindrome" if is_palindrome else "Not Palindrome")
