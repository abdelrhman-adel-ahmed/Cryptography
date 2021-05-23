
"""
=========================goal======================
gcd(r0,r1) = r = s * r0 + t * r1
the goal is to find: 1- gcd(r0,r1) 
2- the main goal to find s and t 
* because if r0,r1 is relatively prime (coprimes)
* then the inverse mod n of r1 is the t
inverse mod n is very usful in cryptography 
e.x RSA the step 5 in the algo which to calc the private key (d) is just doing inverse mod n 

initial values (for more clarification see the proof of EEA):
s0=1 s1=0
t0=1 t1=1
"""

def gcdExtended(a, b):

    # Base Case
    if a == 0:
        return b, 0, 1
    
    gcd, x1, y1 = gcdExtended(b % a, a)

    # Update x and y using results of recursive
    # call
    s = y1 - (b // a) * x1
    t = x1

    return gcd, s, t
