#A dictionary is and unordered key-value pair,and it is denoted by the {},and it is different from a list,because it contains a key and a value

dict ={
     'a': [1,2,3,4,5],
     'b': 'Hello',
     'c': False,
     (1,2,3) : 20
 }
# the key and a value in a dictionary is differentiated by a : symbol
print(dict['b'][2 ])
print(dict[(1,2,3)])

#A dictionrary's key has to be immutable,wghich means it can't take another form
#A dictionary's key can only take a sting,int and a boolean key but not a list key
#A key has to be unique
dict ={
    123: [1,2,3,4,5],
    True: 'Hello',
    '[100]': False
}
print(dict)

