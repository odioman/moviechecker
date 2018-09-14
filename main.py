if True:
    enter_age = int(input('Enter your age: '))

    if enter_age >= 18:
        print('You can see an NC-17, as well as any other movie if you would like')

    elif 13 <= enter_age <= 17:
        print('You can see an R rated and PG-13 movie but not NC-17')

    else:
        print('You can watch a PG or G movie')
