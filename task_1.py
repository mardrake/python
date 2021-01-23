def delenie(arg_1, arg_2):
    if arg_1 != 0:
      arg_1 = arg_1
    else:
      arg_1 = int(input('Try again Enter first number:'))
    if arg_2 != 0:
      arg_2 = arg_2
    else:
      arg_2 = int(input('Try again Enter second number:'))

    return int(arg_1 / arg_2)



print(delenie(int(input('Enter first number')), int(input('Enter second number'))))