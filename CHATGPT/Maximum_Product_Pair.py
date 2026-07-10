
# nums = [5, 20, 2, 6]


# def maximumproduct(nums):
#   maxiprod =  0
#   for i in range(len(nums)):
#       for j in range(i+1,len(nums)):
#         oneval = nums[i]
#         secondval = nums[j]

#         product  = oneval * secondval

#         if product >= maxiprod:
#           maxiprod = product
#           best_pair = ([nums[i],nums[j]])
#   return best_pair
            
# print(maximumproduct(nums))



nums = [5, 20, 2, 6]


def maximumproduct(nums):

  maxiprod = nums[0]*nums[1]
  best_pair = [nums[0], nums[1]]

  first_idx  = nums[0]
  last_idx = len(nums)-1

  while first_idx < last_idx:
      product = nums[first_idx] * nums[last_idx]

      if product > maxiprod:
         best_pair[nums[first_idx],nums[last_idx]]
         first_idx+=1
         last_idx-=1
  return best_pair
        
print(maximumproduct(nums))