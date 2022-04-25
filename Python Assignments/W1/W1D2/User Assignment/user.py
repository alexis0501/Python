class User:

    def __init__(self, name):
        self.name = name
        self.amount = 0

    def make_a_deposit(self, amount):
        self.amount += amount

    def make_a_withdrawl(self, amount):
        self.amount -= amount

    def display_user_balance(self):
        print(f"User: {self.name}, Balance: {self.amount}")

    def transfer_money(self, amount, user):
        self.amount -= amount
        user.amount += amount
        self.display_user_balance()
        user.display_user_balance()


#names
Tim = User("Tim")
Bob = User("Bob")
Joe = User("Joe")
#Tim
Tim.make_a_deposit(250)
Tim.make_a_deposit(100)
Tim.make_a_deposit(30)
Tim.make_a_withdrawl(60)
Tim.display_user_balance()
#Bob
Bob.make_a_deposit(700)
Bob.make_a_deposit(450)
Bob.make_a_withdrawl(200)
Bob.make_a_withdrawl(300)
Bob.display_user_balance()
#Joe
Joe.make_a_deposit(1000)
Joe.make_a_withdrawl(2000)
Joe.make_a_withdrawl(3000)
Joe.make_a_withdrawl(4500)
Joe.display_user_balance()
#transfer
Bob.transfer_money(400, Tim)