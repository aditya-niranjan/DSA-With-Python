from sqlalchemy import false


s1 = "Was it a car or a cat I saw"
s2 = "tab a cat"


def fun(s):
  s = "".join(ch for ch in s if ch.isalnum()).lower()
  last = len(s)-1
  i = 0
  while i < last:
    if s[i] == s[last]:
        i+=1
        last-=1
    else:
        return False
  return True

print(fun(s1))
print(fun(s2))