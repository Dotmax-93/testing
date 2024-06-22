Tesco_cart = [
    'bread',
    'sugar',
    'beer',
    'apple',
    'watermelon'
    ]
print(Tesco_cart[0])
print(Tesco_cart[0::2])

#Lists are mutable,which means the values can be changed
Tesco_cart[1] = 'sweetener'
New_cart = Tesco_cart[::]
New_cart[2] = "gin"
print(New_cart)
print(Tesco_cart)
