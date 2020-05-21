

import math
import sympy
import random
import time

def decrypt(cipherText, key):
    d,n = key
    plainText = [chr(pow(char, d, n)) for char in cipherText]
    return ''.join(plainText)

def multiplicative_inverse(e, phi):
    r0 = phi
    r1 = e
    t0 = 0
    t1 = 1
    while r1 > 0:
        q = math.floor(r0/r1)
        temp = r0 - q * r1
        r0 = r1
        r1 = temp

        temp = t0 - q * t1
        t0 = t1
        t1 = temp
        if r1 == 1:
            return t1 % phi


# method to return prime divisor for n  
def PollardRho(n): 
  
    # no prime divisor for 1  
    if (n == 1): 
        return n 
  
    # even number means one of the divisors is 2  
    if (n % 2 == 0): 
        return (2, int(n / 2))
  
    # we will pick from the range [2, N)  
    x = (random.randint(0, 2) % (n - 2)) 
    y = x 
  
    # the constant in f(x). 
    # Algorithm can be re-run with a different c 
    # if it throws failure for a composite.  
    c = (random.randint(0, 1) % (n - 1)) 
  
    # Initialize candidate divisor (or result)  
    d = 1
  
    # until the prime factor isn't obtained. 
    # If n is prime, return n  
    while (d == 1): 
      
        # Tortoise Move: x(i+1) = f(x(i))  
        x = (pow(x, 2, n) + c + n)%n 
  
        # Hare Move: y(i+1) = f(f(y(i)))  
        y = (pow(y, 2, n) + c + n)%n 
        y = (pow(y, 2, n) + c + n)%n 
  
        # check gcd of |x-y| and n  
        d = math.gcd(abs(x - y), n) 
  
        # retry if the algorithm fails to find prime factor 
        # with chosen x and c  
        if (d == n): 
            return PollardRho(n) 
    return (d, int(n / d)) 


def knj_factorize(n):
    curr = math.floor(n ** 0.5)
    while curr > 1:
        if n % curr == 0:
            return (curr, int(n / curr))
        curr = sympy.prevprime(curr)


if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("Factorization attack on RSA")
    e = int(input('Enter the public key exponent : '))
    n = int(input('Enter n : '))
    cipherText = input('Enter the ciphertext to decrypt : ')
    cipherText = list(map(int, cipherText.split(" ")))
    print("Factorizing....")
    start = time.time()
    p, q = knj_factorize(n)
    end = time.time()
    print(p)
    print(q)
    print("STATISTIC : Time taken to factorize by knj is ",end - start, "sec")
    

    phi = (p-1)*(q-1)
    d = multiplicative_inverse(e, phi)
    print("Private key is", d)
    print("Decrypting....")
    plainText = decrypt(cipherText, (d, n))
    print("Decrypted message:")
    print(plainText)