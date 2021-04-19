# This is a Budget app that helps you plan and stick with your budget

class Budget:

    def __init__(self, section, amount):
        self.currentBalance = 0
        self.section = section
        self.amount = amount

    def deposit(self):
        amount = int(input("How much do you want to Deposit? "))
        self.currentBalance = self.currentBalance + amount
        print ("Deposit successful! Your current balalnce is", self.currentBalance)
    
    def withdraw(self):
        amount = int(input("How much do you want to Withdraw? "))
        if (self.currentBalance >= amount):
            self.currentBalance = self.currentBalance - amount
            print("Withdrawal successful! Current balance is", self.currentBalance)
        else:
            print("Insufficient funds")

    def balance(self):
        print ("Current balance in account is", self.currentBalance)

    def transfer(self):
        return 'Transfer successful'

food = Budget('Food', 1000)
clothing = Budget('Clothing', 2000)
entertainment = Budget('Entertainment', 3000)
offering = Budget('Offering', 4000)

food.deposit()
food.withdraw()
food.balance()
