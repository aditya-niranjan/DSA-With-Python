



def checkOnesSegment(s):
    seen_zero = False
    
    for ch in s:
        if ch == '0':
            seen_zero = True
        elif seen_zero and ch == '1':
            return False
    
    return True

s = "1100"
result = checkOnesSegment(s)
print(result)