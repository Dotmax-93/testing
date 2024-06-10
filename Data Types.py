print("Hello world")

print(2 +4)

print(bin(6))

print(int('110', 2))

print(bin(25))

print(int('11001' , 2))

# Variables

age_boy = 32
shoe_size = age_boy/2
a = shoe_size

print(shoe_size)
print(a)

#Augmented Assignment Operator
shoe_size += 2
print(shoe_size)

#String data types

first_name = "Oluwatimilehin"
last_name = "Omiyale"
full_name = first_name + last_name

print(full_name)
first_name = "Oluwatimilehin"
last_name = "Omiyale"
age = 55
price = 35
full_name = first_name + "   " + last_name

print(full_name)

#Escape sequence in string
#do more exercises on escape sequence


question ="How\'s work \"really\" going?"
print(question)

question ="\tHow\'s work \"really\" going?"
print(question)

question ="How\'s work \"really\" going?\nßhope you are enjoying work?"
print(question)

# formatted strings

print(last_name)

print(age)

print("Hello " + last_name + ". You are " + str(age) + " year old")

print('Hello ' + last_name + '. you bought sugar worth, ' + str(price) + ', you are ' + str(age))

print(f'Hello {last_name}. you bought sugar worth, {price} you are {age} years old')

print(len(full_name))

#Built in methods
print(full_name.upper())

birth_year = input('what year were you born?')
age = 2024 - int(birth_year)
print(f'your age is: {age}')


#Username and password
username = input('what is your username?')
password = input('what is your password?')

password_length = len(password)
hidden_password = '*' * password_length

print(f'{username},your password,{hidden_password} is {password_length} letters long')