picture = [
  [0,0,0,1,0,0,0],
  [0,0,1,1,1,0,0],
  [0,1,1,1,1,1,0],
  [1,1,1,1,1,1,1],
  [0,0,0,1,0,0,0],
  [0,0,0,1,0,0,0]
]
# iterate over pictures
 #if 0,print and empty space and if it's 1,print *

def show_tree():
    for row in picture:
        for pixels in row:
            if pixels== 0:
                print(' ', end = ' ')
            else:
                print('•', end =' ')
        print(' ')

show_tree()
show_tree()
show_tree()
def checkDriverAge():
    age = input('what is your age?: ')

    if int(age) < 18:
        print('Sorry, you are too youung to drive this car. Powering off')
    elif int(age) > 18:
        print('Powering on. Enjoy the ride!')
    elif int(age) == 18:
        print('congratulations on your first year of driving. Enjoy the ride!')
checkDriverAge()



def checkDriverAge(age=0):

    if int(age) < 18:
        print('Sorry, you are too youung to drive this car. Powering off')
    elif int(age) > 18:
        print('Powering on. Enjoy the ride!')
    elif int(age) == 18:
        print('congratulations on your first year of driving. Enjoy the ride!')
checkDriverAge(92)





