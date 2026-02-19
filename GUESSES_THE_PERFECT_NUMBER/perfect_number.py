import random


n = random.randint(1,100)

a = -1
guesses = 1
while (a != n):
      a = int(input("Enter The Perfect No: "))
      if(a > n):
            print("Lower Number Please")
      elif(a<n):
            print("Higher Number Please")
      guesses+=1
                
print(f"you have guessed correct number:{n} in {guesses} attempts")