
#define a class employee with
#attributes name, weeklyhours, rate, overtimeRate, weeklytaxcredit
# and store these in the constructor
#(20)
#Create a method computeWeeklyPay (self,hours) returning the gross pay of the employee,
# which is the hours up to weeklyhours at rate, plus hours above this at overtimeRate
#(25)
##Create method computeTax(self,grossPay) which returns the tax due at
#40% on the gross pay, reduced by the tax credit.
#(25)#
#
#Ensure overtime cannot be negative
#(10)
#weekly pay cannot be negative
#(10)
#Tax cannot be negative
#(10)


class Employee:

    name = ''
    rate = int(0)
    overtimeRate = int(0)
    weeklytaxcredit = int(0)

    def _init_(self, name, rate, overtimeRate, weeklytaxcredit):
        self.name = name
        self.weeklyhours = 0
        self.rate = rate
        self.overtimeRate = overtimeRate
        self.weeklytaxcredit = weeklytaxcredit

    def computeWeeklyPay(self, weeklyhours):
        if weeklyhours > 35:
            grosspay = 35 * self.rate + self.overtimeRate * (weeklyhours - 35)
        else:
            grosspay = weeklyhours * self.rate
        return grosspay

    def computeTax(self, grossPay):
        tax = (grossPay * 0.4) - self.weeklytaxcredit
        return tax

emp1 = Employee('Nitish',)