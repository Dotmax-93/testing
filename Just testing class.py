


class Toyota:
    def __init__(self,brand,year,color):
        self.brand= brand
        self.year = year
        self.color = color

    def call(self):
        print(f'This is a Toyota {self.brand}, the model year ia {self.year}, and it is a {self.color} colored car')


    def run(self):
        print(f'Do you want a {self.brand} of year {self.year} and a {self.color} colored car?')


car1= Toyota('Venza', 2012, 'Red')
car2= Toyota('Camry', 2016, 'Blue')

print(car1.call())
print(car2.call())
(car1.run())
car1.year = 'LLLLLL'
car1.color = '222222'
print(car1.year)






