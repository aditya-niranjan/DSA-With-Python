num = [2,7,11,15]

target = 9

left=0
right = 1


for i in num:
  if left >= right:
      break
  else:
     temp = num[left] + num[right]
     if temp == target:
        print(f"Pair found: {left}, {right}")
        break
     elif temp < target:  
        left += 1
     else:
        right += 1

