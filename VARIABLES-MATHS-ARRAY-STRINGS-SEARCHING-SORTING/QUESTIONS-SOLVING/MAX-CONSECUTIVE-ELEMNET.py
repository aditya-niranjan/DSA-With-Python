# this one is my approach and below one is codeing and debbuging sir appraoch

nums = [1,1,0,1,0,1,1,1,1,0,1,1]

count = 0
max_count = count

for i in range(1,len(nums)):
    if nums[i] == nums[i-1]:
        count+=1
    else:
        max_count = max(count,max_count)

print(max_count)

## -------------------------

nums = [1,1,0,1,0,1,1,1,1,0,1,1]

count = 0
max_count = count

for i in range(0,len(nums)):
    if nums[i] == 1:
        count+=1
    else:
        max_count = max(count,max_count)
        count=0

print(max_count)