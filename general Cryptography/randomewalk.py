import random

"""
In mathematics, a random walk is a mathematical object, known as a stochastic or random process, 
that describes a path that consists of a succession of random steps on some mathematical space such as the integers.
"""

def random_walk_(n):
    """ return coordinte after 'n' blocks random walks"""

    x, y = 0, 0
    for i in range(n):
        step = random.choice(["n", "s", "e", "w"])
        if step == "n":
            y += 1
        if step == "s":
            y -= 1
        if step == "e":
            x += 1
        else:
            x -= 1
    return (x, y)


def random_walk(n):
    x, y = 0, 0
    for i in range(n):
        dy, dx = random.choice([(0, 1), (0, -1), (1, 0), (-1, 0)])
        x += dx
        y += dy
    return (x, y)


# will walk 25 times ,each walk is 10 block in distance
for i in range(5):
    walk = random_walk(10)
    print(f"i walk 10 block from home and get to position {walk} wich is {abs(walk[0])+abs(walk[1])} block from home")
