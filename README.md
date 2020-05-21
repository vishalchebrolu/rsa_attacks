# rsa_attacks
Demonstrating factorization, low public key exponent, chosen ciphertext attacks on a toy RSA in which the user has choice for p,q and n.
Python 3 has been used.

rsa.py : The toy RSA file which asks for p,q and computes n. The user has a choice of setting a specified public exponent or let the program chose a random one.
         The program then waits in a busy loop, waiting for Encrypt(E)/Decrypt(D)/Stop(S) options.
   
   
fact.py : A factorization attack on RSA. Alogrithm used was knj-factorization algorithm in which prime factor p which is less sqrt(n) is checked starting from sqrt(n) and ending at 2.
          The program also takes cipher text, public exponent e along with n and decrypts the cipher text.
          
low_exp.py : This attack takes a public exponent e. It then takes n values corresponding to each of the recipients also their corresponding cipher texts.
             It then uses Chinese-Remainder Theorem(CRT) to solve for m^e and computes m by finding the eth root of m^e.
             
ch_cipher.py : This attack needs the public key values e,n and also the cipher text to be decrypted. It computes a masked cipher text as (m*2)^e mod n and asks to send to the receiver for decryption.
               The rsa.py program also gives the plain text in numbers. This decrypted text in numbers need to be supplied to the ch_cipher.py program which then computes the original plain text.
