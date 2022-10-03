"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""

class Employee:
    def __init__(self,name,monthly,hourly,hoursWorked,contracts,contractsDone,bonusCommission,description):
        self.name = name
        self.monthly = int(monthly)
        self.hourly = int(hourly)
        self.hoursWorked = int(hoursWorked)
        self.contracts = int(contracts)
        self.contractsDone = int(contractsDone)
        self.bonusCommission = int(bonusCommission)
        self.description = description
        Employee.get_pay(self)
        Employee.__str__(self)

    def get_pay(self):
        hourPay = self.hourly * self.hoursWorked
        commissionPay = self.contracts * self.contractsDone
        totalPay = hourPay + commissionPay + self.monthly + self.bonusCommission
        return totalPay

    def __str__(self):
        return self.description


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie',4000,0,0,0,0,0,'Billie works on a monthly salary of 4000.  Their total pay is 4000.' )

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie',0,25,100,0,0,0,'Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.' )

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee',3000,0,0,200,4,0,'Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.' )

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan',0,25,150,220,3,0,'Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.' )

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie',2000,0,0,0,0,1500,'Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.' )

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel',0,30,120,0,0,600,'Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.' )
