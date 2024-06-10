class User:
    def  sign_in(self):
        print('logged in')


class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'attacking with the power of {self.power}')


class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'attacking with arrows: arrows left- {self.num_arrows}')


wizard1 = Wizard('Timilehin', 50)
archer1 = Archer('Dotun', 100)
print(wizard1.attack())
print(archer1.attack())
wizard1.sign_in()
archer1.sign_in()

print(issubclass(Wizard, User))
