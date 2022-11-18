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

class employee:

    name = ''
    weeklyhours = int(0)
    rate = int(0)
    overtimeRate = int(0)
    weeklytaxcredit = int(0)

    def __init__(self, name, weeklyhours, rate, overtimeRate, weeklytaxcredit):

        if overtimeRate < 0 or rate < 0:
            raise Exception('Overtimerate or rate cannot be 0')

        self.name = name
        self.weeklyhours = weeklyhours
        self.rate = rate
        self.overtimeRate = overtimeRate
        self.weeklytaxcredit = weeklytaxcredit

    def computeWeeklyPay(self,hours):
        if hours > self.weeklyhours:
            grosspay = (self.weeklyhours * self.rate) + (hours - self.weeklyhours) * self.overtimeRate
        else:
            grosspay = hours * self.rate
        return grosspay

    def computeTax(self,grosspay):
        tax = (grosspay * 0.4) - self.weeklytaxcredit
        if tax < 0:
            raise Exception('Weekly Tax Credit cannot be negative')
        else:
            return tax

emp1 = employee('Nitish',40,15,20,5)
gpa = emp1.computeWeeklyPay(40)
print(gpa)
print(emp1.computeTax(gpa))











