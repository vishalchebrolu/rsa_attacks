
import random

if __name__ == '__main__':
	'''
	Detect if the script is being run directly by the user
	'''
	print("Chosen Ciphertext attack on RSA")
	e = int(input("Enter the public key exponent : "))
	n = int(input("Enter n : "))
	cipherText = input("Enter a cipher text to decrypt: ")
	cipherText = list(map(int, cipherText.split(" ")))

	#r = random.randrange(1,10)
	r = 2
	masked_CipherText = [(char * pow(r,e,n)) % n for char in cipherText]
	print("Send the following text to the receiver for decryption")
	print(' '.join(map(lambda x: str(x), masked_CipherText)))

	masked_PlainText = input("Enter the plaintext in numbers after decryption :")
	masked_PlainText = masked_PlainText.split(" ")
	plainText = [chr(int(int(char)/r)) for char in masked_PlainText]

	print("Decrypted message:")
	print(''.join(plainText))