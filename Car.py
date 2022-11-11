
class Car:
    color = ''
    name = ''
    noOfWheels = int(0)
    seats = int(0)

    def __init__(self, color, name, noOfWheels, seats):

        self.color = color
        self.name = name
        self.noOfWheels = noOfWheels
        self.seats = seats

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getColor(self):
        return self.color

    def setColor(self, color):
        self.color = color

    def getnoOfWheels(self):
        return self.noOfWheels

    def setnoOfWheels(self, noOfWheels):
        self.noOfWheels = noOfWheels

    def getseats(self):
        return self.seats

    def setseats(self,seats):
        self.seats = seats

myCar = Car('Red','WagonR',4 , 5)
print(myCar.getName())
myCar.setName('McLarenP1')
print(myCar.getName())
myCar.setseats(90)
print(myCar.seats)