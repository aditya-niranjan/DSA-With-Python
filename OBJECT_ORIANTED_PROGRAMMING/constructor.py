
class Employee:
    name = "Aditya"
    language = "python-dev"
    salary = 120000


    def __init__(self,name,language,salary):  # this called as Dudnder method in python whichever the function in python called with double underscrore are Dunder method in python
        print("this is automatically called when new instance object is called")
        self.name = name
        self.language = language
        self.salary = salary
        

        

    def getinfo(self):
        print(f"\n this your name:{self.name}\n this is you language:{self.language}\n this is your salary:{self.salary}")
        print("",end=" ")

    @staticmethod
    def greet():
        print("\n Good Morning BOSS", end="")
        print("")
        print("")



# emp = Employee()


# emp.langauge="js-developer"  #it has more preiprity beacuse it is instances retrival
# Employee.langauge="gsap-devloper"  #it has second prepority this you can 
# print("\n",emp.name,"\n",emp.langauge,"\n",emp.salary,"\n")
# print("")

# emp.getinfo()
# emp.greet()

aditya = Employee("aditya","full-stack-dev",100000)
print(aditya.name,aditya.language,aditya.salary)

om = Employee("om","full-stack-dev",40000000)
print(om.name,om.language,om.salary)

