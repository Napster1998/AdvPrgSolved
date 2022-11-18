class Car():
  def mycar_init_(name, color, numofwheels):
    mycar.name = name
    mycar.color = color
    mycar.numofwheels = numofwheels
  def _repr_(mycar):
        return Car({mycar.name},{mycar.color},{mycar.numofwheels})

c1 = Car('venza','purple','4')

print(c1)