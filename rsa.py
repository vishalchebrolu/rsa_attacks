
import random
import math

'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
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

'''
Tests to see if a number is prime.
'''
def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num**0.5)+2, 2):
        if num % n == 0:
            return False
    return True

def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    #n = pq
    n = p * q
    if n <= 256:
        raise ValueError('n should be greater than 256. Give larger primes')

    #Phi is the totient of n
    phi = (p-1) * (q-1)

    #Choose an integer e such that e and phi(n) are coprime
    rand_option = input("Do you want to have a specific public exponent? Y/N ")
    if rand_option.startswith("Y"):
        while True:
            e = int(input("Enter the public exponent : "))
            if gcd(e,phi) == 1:
                break
            print("gcd(" + str(e) + ", " + str(phi) + ") is not 1")
    else:
        e = random.randrange(2, phi)
    #Use Euclid's Algorithm to verify that e and phi(n) are comprime
        g = gcd(e, phi)
        while g != 1:
            e = random.randrange(2, phi)
            g = gcd(e, phi)

    #Use Extended Euclid's Algorithm to generate the private key
    d = multiplicative_inverse(e, phi)
    
    #Return public and private keypair
    #Public key is (e, n) and private key is (d, n)
    return ((e, n), (d, n))

def encrypt(pk, plaintext):
    #Unpack the key into it's components
    key, n = pk
    #Convert each letter in the plaintext to numbers based on the character using a^b mod m
    cipher = [pow(ord(char), key, n) for char in plaintext]
    #Return the array of bytes
    return cipher

def decrypt(pk, ciphertext):
    #Unpack the key into its components
    key, n = pk
    #Generate the plaintext based on the ciphertext and key using a^b mod m
    plain = [pow(char, key, n) for char in ciphertext]
    #Return the array of bytes as numbers
    return plain
    

if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("RSA Encrypter/ Decrypter")
    print("The product of prime numbers(p,q) should be greater than 16")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print("Your public key is ", public ," and your private key is ", private)

    choice = input("Want me to Encrypt/Decrypt/Stop? ")
    while not choice.startswith('S'):
        if choice.startswith('E'):
            message = input("Enter a message to encrypt with your public key: ")
            encrypted_msg = encrypt(public, message)
            print("Your encrypted message is: ")
            print(' '.join(map(lambda x: str(x), encrypted_msg)))
        elif choice.startswith('D'):
            encrypted_msg = input("Enter the cipher text to decrypt with your private key: ")
            encrypted_msg = list(map(int, encrypted_msg.split(" ")))
            print("Decrypting message with private key ", private ," . . .")
            plain = decrypt(private, encrypted_msg)
            print("Your message in numbers :")
            print(' '.join(list(map(str, plain))))
            print("Your message in ASCII characters :")
            print(''.join(list(map(chr, plain))))
        choice = input("Want me to Encrypt/Decrypt/Stop? ")