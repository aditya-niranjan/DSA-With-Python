class Facotry:
  def __init__(self,body,wheels,engine):
    self.body = body
    self.wheels = wheels
    self.engine = engine

  def show_details(self):
    print(f"Body: {self.body}")
    print(f"Wheels: {self.wheels}")
    print(f"Engine: {self.engine}")

class Car(Facotry):
  def __init__(self,body,wheels,engine,doors):
    super().__init__(body,wheels,engine)
    self.doors = doors

  def show_details(self):
    super().show_details()
    print(f"Doors: {self.doors}")


object1 = Car("Coverd",4,"v8 Engine",4)
object2 = Facotry("Coverd",4,"v8 Engine")
object2.show_details()
print()
object1.show_details()