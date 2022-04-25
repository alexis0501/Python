class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_a_deposit(self, amount):
        self.amount += amount
        return self
    def make_a_withdrawl(self, amount):
        self.amount -= amount
        return self
    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")
        return self
    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()
        return self
    def yield_interest(self, int_rate):
        if self.amount > 0:
            self.amount *= int_rate
        return self


#names
Tim = User("Tim")
Bob = User("Bob")
#Tim
Tim.make_a_deposit(250)
Tim.make_a_deposit(100)
Tim.make_a_deposit(30)
Tim.make_a_withdrawl(60)
Tim.display_user_balance()
Tim.yield_interest(.05)
#Bob
Bob.make_a_deposit(200)
Bob.make_a_deposit(450)
Bob.make_a_withdrawl(400)
Bob.make_a_withdrawl(700)
Bob.display_user_balance()
Bob.yield_interest(.05)
#Joe
Bob.transfer_money(400, Tim)