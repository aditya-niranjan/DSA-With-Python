

class Dogesh:
    def __init__(self):
        print("this constructer from Dogesh bhai!!")
    a = 1

class Cat(Dogesh):
    def __init__(self):
        super().__init__()
        print("this constructer from Cat bhai!!")
    b = 2

class MAN(Cat):
    def __init__(self):
        super().__init__()
        print("this constructer from MAN bhai!!")
    c = 3


# o = Dogesh()

o = MAN()
print(o.a,o.b,o.c)


