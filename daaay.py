class dayType :

    def _init_(self):
        self.currentDay = 1
        self.weekdays = {1:"Mon",2:"Tue",3:"Wed",4:"Thu",5:"Fri",6:"Sat",7:"Sun"}

    def setDay(self,dayToSet) :

        if type(dayToSet) == int :

            self.currentDay = dayToSet
        elif type(dayToSet) == str :
            for dictionaryDays in self.weekdays.keys() :
                if self.weekdays[dictionaryDays] == dayToSet :
                    self.currentDay = dictionaryDays
        print("New set day is : " ,self.weekdays.get(self.currentDay))

    def printDay(self) :
        print("Print Day is : " , self.weekdays.get(self.currentDay))

    def returnCurrentDay(self) :

        return self.weekdays.get(self.currentDay)

    def returnNextDay(self) :

        if self.currentDay == 7 :
            return self.weekdays.get(1)
        else :
            return self.weekdays.get(int(self.currentDay) + int(1))

    def returnPreviousDay(self):

        if self.currentDay == 1:
            return self.weekdays.get(7)
        else:
            return self.weekdays.get(int(self.currentDay) - int(1))

    def returnDayModifiedInput(self, daysToAdd):

        count = 1
        currentDayModification = self.currentDay
        for it in range(daysToAdd) :

            if currentDayModification == 7:
                currentDayModification = 1
            else :
                currentDayModification = currentDayModification +1
            count = count + 1

        return self.weekdays.get(currentDayModification)
