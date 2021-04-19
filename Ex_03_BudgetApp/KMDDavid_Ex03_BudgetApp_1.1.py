# This is a Budget app that helps you plan and stick with your budget

class Budget:

    budgetName = input("What is the name of your Budget App? \n" )

    def __init__(self, section, amount):
        self.currentBalance = 0
        self.section = section
        self.amount = amount

print ("Welcome to",Budget.budgetName, "Budget App")
