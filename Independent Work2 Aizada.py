a = 1, 2, 3
b = 0, 2, 4
def compare(number):
    if (number > b):
        print('{} Alice receives a point'.format(number))
    elif (number <= b):
        print('{} They are equal'.format(number))
    else:
        print('{} Bob receives a point'.format(number))
compare(a)
compare(b)



