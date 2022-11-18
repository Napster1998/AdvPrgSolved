class Human:
    name = ''
    age = int(0)
    country = ''

    def __init__(self, name, age, country):
        self.name = name
        self.age = age
        self.country = country

    def getName(self):
        return self.name

    def setName(self,name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self,age):
        self.age = age

    def addAge(self,bywhat):
        self.age = self.age + int(bywhat)
        return

h1 = Human('Nitish',24,'India')

h1.addAge(400)
print(h1.getAge())

