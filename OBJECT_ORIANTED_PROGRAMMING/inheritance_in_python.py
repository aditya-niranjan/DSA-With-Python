

class Dogesh:
    def Barking(self):
      print("HEllo I am   Degesh from fucntion - Barking")
      print("")
      print("")
   
print("hello I am from the Dogesh class!!")

class Cat:
   def Mav(self):
      print("HEELo i am from function Mav")
      print("")
      print("")

print("HELLO I am from class Cat!!")

class MAN(Dogesh,Cat):
   print("this is the MAN from class  man")



b = MAN()

b.Barking()
b.Mav()