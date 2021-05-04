# This is a Budget app that helps you plan and stick with your budget

class Budget:

    def __init__(self, section, amount):
        self.section = section
        self.amount = amount

    def deposit(self, amount):
        self.amount = amount + amount
        return "Amount of {} has been deposited into {} section".format(amount, self.section)
    
    def balance(self):
        return "Current balance in {} section is: {}".format(self.section,self.amount)

    def withdraw(self, amount, section):
       self.amount = amount - amount
       return "Amount of {} has been withdrawn from {} section".format(amount, self.section)

    def transfer(self, amount, section):
        self.amount = amount - amount
        section.amount = amount + amount
        return "Amount of {} was successfully transferred to {} section".format(amount, section.section)

Offering = Budget('Offering', 4000)
Food = Budget('Food',2000)
Electricity = Budget('Electricity', 1000)
Accommodation = Budget('Accommodation', 5000)

print(Food.deposit(200))
print(Accommodation.transfer(500, Food))
print(Food.balance())
print(Offering.withdraw(360, Offering))