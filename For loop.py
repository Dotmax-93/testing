#for item in (1.,2.,3.,4.,5.):
    #for x in ["a", "b", "c"]:
     #print(item, x)

#Using loop for dictionaries

user = {
    'name': 'Dotmax',
    'age': '2006',
    'can_swim': True
}
for item in user.values():
    print(item)

for item in user.items():
    print(item)

for item in user.keys():
    print(item)

for key, values in user.items():
    print(key,values)

my_shopping_list = [1,2,3,4,5,6,7,8,9,10,11,13]

counter = 0
for item in my_shopping_list:
    counter = counter + item

print(counter)

i = 0
while i < 50:
    print(i)
    i = i+ 1