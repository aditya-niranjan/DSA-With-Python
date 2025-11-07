# checking a String is Palindrome or not using for loops

s = "NITIN"

left = 0
right = len(s)-1

is_palindrome = True
for ch in s:
    if s[left] != s[right]:
        is_palindrome = False
        break
    else:
        left+=1
        right-=1


if is_palindrome:
    print("String is Palindrome")
else:
    print("String is not Palindrome")

