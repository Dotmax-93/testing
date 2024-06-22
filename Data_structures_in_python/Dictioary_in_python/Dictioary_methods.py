care_calls ={
     'wash': [1,2,3,4,5],
     'nutrition': 'Hello',
     'greetings': False
}
# get method
print(care_calls.get('wash'))
print(care_calls.get('age',))
print(care_calls.get('nutrition'))

print('wash' in care_calls)
print('age' in care_calls)

# we can also get either keys or values from a dictionary using

print('nutrition' in care_calls.keys())
print('Hello' in care_calls.values())

# items method grabs the entire content in the dictionary
print(care_calls.items())

# clear method
# print(care_calls.clear())

# pop method

print(care_calls.pop('wash'))
print(care_calls)

# update method
print(care_calls.update({'greetings' : True}))
print(care_calls)
