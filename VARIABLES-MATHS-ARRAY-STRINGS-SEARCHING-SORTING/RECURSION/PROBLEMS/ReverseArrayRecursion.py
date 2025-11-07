

# Starting a ARRay [5,7,3,2,6,1,5,9]
# Revered ARRay [9, 5, 1, 6, 2, 3, 7, 5]



def func(num,left,right):
    if num[left] >= num[right]:
        return

    num[left],num[right] = num[right],num[left]
    func(num,left+1,right-1)

num = [5,7,3,2,6,1,5,9]
func(num,0,len(num)-1)
print(num)