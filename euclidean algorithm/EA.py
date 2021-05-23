  

  """
  ======================= goal is to find the gcd of two numbers gcd(r0,r1)===========================
  a=bq1+r1
  b=r1q2+r2
  ...
  973 = 3 * 307 + 70
  307 = 4 * 70 + 21
  70 = 3 * 21 + 7
  21 = 3 * 7 + 0
  so when remender ==1 we stop and the r1 is the gcd(r0,r1)
  
  """
  
r0 = 973
r1 = 321

def gcd1(a, b):
    if b == 0:
        return a

    return gcd1(b, a % b)
