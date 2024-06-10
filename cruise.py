class Cat:
    species = 'mammal'
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def oldest_cat(*args):
        return max(args)
        print(f'the oldest cat is {oldest_cat(cat1.age, cat2.age, cat3.age)} years old')

cat1 = Cat("big", 25)
cat2 = Cat("medium", 25)
cat3 = Cat("Huge",30)

print()
