# Try and Except error handling
#steps in handling errors
#try function,which has the pythoin command,using the right indentation
#use the except function to name the error and print the response you need to generate
#use else function to generate a response after the command has been ran and add "break" to discontinue the loop
#you can wrapa all the above mentioned steps in a while loop,using the right indentation



while True:
    try:
        age = int(input('what\'s your age?'))
        print(age)
        10/age

    except ValueError:
        print('please enter your age in number')

    except:
        print('Please enter a number greater than 0')

    else:
        print('Thank you!')
        break