from os import name
from typing import Self


class Employee:
    name = "Aditya"
    language = "python-dev"
    salary = 120000


    def getinfo(self):
        print(f"\n this your name:{self.name}\n this is you language:{self.language}\n this is your salary:{self.salary}")
        print("",end=" ")

    @staticmethod
    def greet():
        print("\n Good Morning BOSS", end="")
        print("")
        print("")



emp = Employee()


# emp.langauge="js-developer"  #it has more preiprity beacuse it is instances retrival
# Employee.langauge="gsap-devloper"  #it has second prepority this you can 
# print("\n",emp.name,"\n",emp.langauge,"\n",emp.salary,"\n")
# print("")

emp.getinfo()
emp.greet()
