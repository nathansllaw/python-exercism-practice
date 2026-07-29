def square(number):
    if number < 1 or number > 64:
        raise ValueError("square must be between 1 and 64")

    grains = 1
    
    for i in range(1, number):
        grains *= 2

    return grains

def total():

    total_grains = 0
    for i in range(1, 65):
        total_grains += square(i)
        
    return total_grains
