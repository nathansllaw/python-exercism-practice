def is_armstrong_number(number):

    numberstring = str(number)
    num_digits = len(numberstring)

    total = 0
    for i in numberstring:
        total += int(i)**num_digits
    
    return total == number
