class User:
    def __init__(self, nameInput):
        self.name= nameInput
        self.amount = 0
    
    def make_deposit(self, numAmount):
        self.amount += numAmount
        return self

    def make_withdrawl(self, numAmount):
        if self.amount< numAmount:
            print("insufficient funds")
        else:
            self.amount -= numAmount
        return self
    
    def display_User_Balance(self):
        print(f"User name: {self.name}, Balance: ${self.amount}")

    def transfer_money(self,other_user, numAmount):
        self.amount -= numAmount
        other_user.amount += numAmount
        return (self)

user1 = User("Guido van Rossum")
# print(user1.name)
# user1.display_User_Balance()
user2 = User("Steve Goodman")
user3 = User("Billy Jones")

user1.make_deposit(50).make_deposit(100).make_deposit(25).make_withdrawl(50).display_User_Balance()
user2.make_deposit(50).make_deposit(50).make_withdrawl(25).make_withdrawl(25).display_User_Balance()
user3.make_deposit(100).make_withdrawl(25).make_withdrawl(25).make_withdrawl(25).display_User_Balance()

user1.transfer_money(user3, 50).display_User_Balance()