def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError as e:
        raise ValueError('Invald inputs')(e)



x, y = 5, 2
try:
    result = divide(x, y)
except ValueError:
    print('Invalid input')
else:
    print('Result is %.1f' % result)

