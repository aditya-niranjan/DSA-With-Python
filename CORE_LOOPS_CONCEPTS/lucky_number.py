


number  = input("Enter a number: ")


luck_number = 0

for i in number:
    if i == '4' or i == '7':
        luck_number += 1

count_str = str(luck_number)

is_lucky = True
for ch in count_str:
    if ch != '4' and ch != '7':
        is_lucky = False
        break


if is_lucky and luck_number > 0:
    print("YES")
else:
    print("NO")

