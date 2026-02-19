import random
import re
from tkinter import N


'''
     1 = sanke
    -1 = water
     0 = gun
'''


print("Welcome to the Snake, Water, Gun game!")
computer = random.choice([1,-1,0])

user_input = input("Enter your choice (snake, water, gun): ")

userdict ={
    "snake": 1,
    "water": -1,
    "gun": 0
}

reverseddict = {
    1: "snake",   
    -1: "water",
    0: "gun"
}


you  = userdict[user_input]

print(f"you chose {reverseddict[you]}\ncomputer chose {reverseddict[computer]}")

''''
if you == computer:
    print("It's a tie!")

else:
  if(computer == -1 and you == -1):                 if(computer - you) -2: 
      print("You win! Snake beats Water.")

  elif(computer == -1 and you == 0):                if(computer - you) -1: 
      print("You lose! Gun beats Snake.")

  elif(computer == 1 and you == 1):               if(computer - you) 2:
      print("You lose! Snake beats Water.")

  elif(computer == 1 and you == 0):               if(computer - you) 1:
      print("You win! Water beats Gun.")

  elif(computer == 0 and you == -1):                if(computer - you) 1:
      print("You win! Gun beats Snake.")

  elif(computer == 0 and you == 1):               if(computer - you) -1:
      print("You lose! Water beats Gun.")
  else:
      print("Invalid input. Please enter snake, water, or gun.")
'''



# Simplified logic using numerical values

if(computer == you):
    print("It's a tie!")
else:
      if(computer - you == -1 or computer - you == 2):
         print("You lose!") 
      else:
          print("You win!")

