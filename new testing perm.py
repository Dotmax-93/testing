while True:
    try:
        year = int(input('what year were you born?'))
        print(year)
    except ValueError as err:
        print('Please,kindly insert a nmerice value')
    except IndentationError:
        print('check your indentation')

    else:
        print('You are logged in!')