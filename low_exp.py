
import time
import math

#returns s,t such that a*s + b*t = gcd(a,b)
def extended_euclidean(a, b):
    r0 = a
    r1 = b
    t0 = 0
    t1 = 1
    s0 = 1
    s1 = 0
    while r1 > 0:
        q = math.floor(r0/r1)
        temp = r0 - q * r1
        r0 = r1
        r1 = temp

        temp = t0 - q * t1
        t0 = t1
        t1 = temp

        temp = s0 - q * s1
        s0 = s1
        s1 = temp
        if r1 == 0:
            return (s0,t0)
            
def crt(a1,n1,a2,n2):
	s, t = extended_euclidean(n1,n2)
	#print("s:", s)
	#print("t:", t)
	return (a1*t*n2 + a2*s*n1) % (n1 * n2)

def solve(cipherText, publicN, e):
	plainText = []
	for j in range(len(cipherText[0])):
		a = cipherText[0][j]
		product = publicN[0]
		for i in range(1,e):
			a = crt(a, product, cipherText[i][j], publicN[i])
			#print(a)
			product = product * publicN[i]
		plainText.append(chr(int(round(a ** (1/e)))))
	return ''.join(plainText)


if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    print("Low Public Exponent attack on RSA")
    e = int(input('Enter the public key exponent : '))
    print("All the n's should be co-prime")
    publicN = [None] * e
    for i in range(e):
    	print("Enter n", end="")
    	print(i, ": ", end="")
    	publicN[i] = int(input())

    cipherText = [None] * e
    for i in range(e):
    	print("Enter ciphertext for sent to recipent", end="")
    	print(i, ": ", end="")
    	text_str = input()
    	cipherText[i] = list(map(int, text_str.split(" ")))

    start = time.time()
    plainText = solve(cipherText, publicN, e)
    end = time.time()
    print("STATISTIC : Time taken to solve is ",end - start, "sec")
    print("Decrypted message:")
    print(plainText)
    