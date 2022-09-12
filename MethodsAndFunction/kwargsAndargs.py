def myfunc(*args, **kwargs):
    print(args)
    print(kwargs)
    print('I will like {} {}'.format(args[0], kwargs['food']))
myfunc(10,20,30, food='eggs', fruit='apple', animal='cat')
