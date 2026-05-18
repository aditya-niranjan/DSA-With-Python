

from unittest import result


num = [3,4,6,7,8,9,12,15,18,21,24,27,30]

target = 15

finallist = []

def ThreeSum(num,target):

    for i in range(len(num)):
        for j in range(i+1,len(num)):
            for k in range(j+1,len(num)):
                  result = num[i] + num[j] + num[k]

                  if result == target:
                       finallist.append([i,j,k])
                  else:
                       continue
                  
    return finallist  


ThreeSum(num,target)
print(finallist)