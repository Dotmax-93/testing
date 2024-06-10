#OOP(Class)
# Rules in creating a class
#We start with class followed by the name of the object we want(every word starts with a capital letter e.g (Class BigObject,followed by a colon)

class PlayerCharacter:
    def __init__(self, name= 'ananymous', age= 0):
        if age > 18:
            self.name = name
            self.age = age

    def shout(self):
        print(f'my name is {self.name}, my age is {self.age}')


player1 = PlayerCharacter('Tayo', 19)
print(player1.shout())

player2 = PlayerCharacter('Oladotun',25)
print(player2.shout())