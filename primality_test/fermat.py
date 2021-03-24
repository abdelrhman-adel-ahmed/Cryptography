"""
    pierre de fermat 17th frensh mathematician century:
* a^p -a --> a is all numbers from 1 to p not including p 
* if all the outcome from the quation are divisble by p then p is a prime 
* note:we dont need to include the number it self because the outcome will be always divisble by the number
"""
number = 5


def fermate(number):
    for i in range(1, number):
        m = i ** number - i
        print(m)
        if m % number == 0:
            continue
        else:
            return False

    return True


x = fermate(number)
print(x) #-->ture
