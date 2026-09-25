def fizzzbuz(n):

    blank= []

    for i in range(1,(n+1)):
        if (i % 3 == 0) and (i % 5 == 0):
            blank.append("FizzBuzz")
        elif i % 3 == 0:
            blank.append("Fizz")
        elif i % 5 == 0:
            blank.append("Buzz")
        else:
            blank.append(str(i))
    print(blank)


fizzzbuz(15)
