
monthDictionary = {'jan':'01','feb':'02','mar':'03','apr':'04','may':'05','jun':'06','jul':'07','aug':'08','sept':'09','oct':'10','nov':'11','dec':'12'}
class Date:
  __day = int(0)
  __month = str('')
  __year = int(0)
  def __init__(self,day,month,year):
        self.__day = day
        self.__month = month
        self.__year = year
  def setDay(self, i):
      self.__day = i
  def getDay(self):
      return self.__day
  def setMonth(self, i):
      self.__month = i
  def getMonth(self):
      return self.__month
  def setYear(self, i):
      self.__year = i
  def getYear(self):
      return self.__year

  def printDate(self):
    print('Date is ',self.__day,'/',monthDictionary.get(self.__month),'/',self.__year)

  def checkLeapYear(self) :
    if (self.__year%4 == 0 and self.__year%100 != 0) or (self.__year%400 == 0):
        print(self.__year, "is a leap year.")
    else :
        print(self.__year, "is not a leap year.")


obj = Date(9,'aug',2022)
obj.printDate()
obj.checkLeapYear()

print(obj.getDay())
print(obj.getMonth())
print(obj.getYear())























