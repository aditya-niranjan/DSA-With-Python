
# what this method does is when u update using the instance and when u try to print it will show the updated one
#insted of showing the original that is present in the class so to maintent the manipulation of the instance we set
# @classmethod it is like staticmethod 


class Employee:
    a = 1

    @classmethod
    def show(self):
        print(f"this is a class attribute a is {self.a}")


e = Employee()

e. a = 4500

e.show()

