
monthDictionary = {'jan':'01','feb':'02','mar':'03','apr':'04','may':'05','jun':'06','jul':'07','aug':'08','sept':'09','oct':'10','nov':'11','dec':'12'}

class Date:
    day = int(0)
    month = ''
    year = int(0)

    def __init__(self, day, month, year):

        self.day = day
        self.month = month
        self.year = year

    def setday(self, day):
        self.day = day

    def getday(self):
        return self.day

    def setmonth(self, month):
        self.month = month

    def getmonth(self):
        return self.month

    def setyear(self, year):
        self.year = year

    def getyear(self):
        return self.year

    def isleapyear(self):
        return self.year%4 == 0

    def getDate(self):
        return str(self.day)+'/'+str(monthDictionary.get(self.month))+'/'+str(self.year)

nitish = Date(19,'feb',1998)
Rohan = Date(23,'sept',1998)

difference = (nitish.getday() - Rohan.getday())

print(nitish.getDate())
print(Rohan.getDate())

