string = "abcd"
target = "abce"

def compare_strings(string :str,target :str)->str:
    if len(string) <=0:
      return target
    
    for i, char in enumerate(string):
        if char == target[i]:
            continue
        else: 
            return target[i]

result = compare_strings(string,target)
print(result)

# time complexity: O(n) where n is the length of the string

# cook your dish here
# string = "IloveCodeChef"

# print(len(string))