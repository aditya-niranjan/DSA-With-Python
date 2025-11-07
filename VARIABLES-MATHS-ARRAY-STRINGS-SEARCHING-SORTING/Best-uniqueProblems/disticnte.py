
def array_distinct_manual(nums1, nums2):
  def get_distinct(arr):
    distinct = []
    for num in arr:
      if num not in distinct:
        distinct.append(num)
    return distinct
  

  def get_only_first(first,second):
      answer = []
      for num in first:
          if num not in second:
             answer.append(num)
      return answer
  
  distinct1 = get_distinct(nums1)
  distinct2 = get_distinct(nums2)

  only_first1 = get_only_first(distinct1,distinct2)
  only_first2 = get_only_first(distinct2,distinct1)

  return [only_first1,only_first2]

# Example usage
n1 = [1,2,3,3]
n2 = [2,4,6,4]
result = array_distinct_manual(n1, n2)
print(result)  # Output: [[1, 3], [4, 6]]
