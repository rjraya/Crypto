from sympy import *

# modulus of the group
N = 264356242932330620591879762011459333409
P = primefactors(N)
e = 151089236568313654499150506467499
c = 259252555055790712660181286804144327401
print(P)

# [63467, 63473, 63487, 63493, 63499, 63521, 63527, 63533]
pows = []
for p in P:
    rede = e%(p-1)
    redc = c%p
    inv = mod_inverse(rede,p-1)
    power = (redc**inv)%p
    pows.append(power)

# [49662, 3560, 35775, 31706, 13018, 12959, 41176, 7925]
print(pows)

def extended_euclidean(a, b): 
    if a == 0: 
        return (b, 0, 1) 
    else: 
        g, y, x = extended_euclidean(b % a, a) 
        return (g, x - (b // a) * y, y) 

def crt(m, x): 

    while True: 
      
        temp1 = mod_inverse(m[1],m[0]) * x[0] * m[1] + mod_inverse(m[0],m[1]) * x[1] * m[0] 
        temp2 = m[0] * m[1] 
        x.remove(x[0]) 
        x.remove(x[0]) 
        x = [temp1 % temp2] + x  

        m.remove(m[0]) 
        m.remove(m[0]) 
        m = [temp2] + m 
 
        if len(x) == 1: 
            break

    return x[0] 
  
m = P
x = pows
print(crt(m, x))

ans = 76696583848373717873707367657884667384

while ans > 1:
    r = ans % 100 
    ans = ans // 100
    print(r)
    print(str(chr(r)))

LEASTSIGNIFICANTBIT
  
