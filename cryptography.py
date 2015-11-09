"""
cryptography.py
Author: Sam Supattapone
Credit: none

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while input1 != 'q':
    for x in ['a','b','c','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']:
        if x == str(input1):
            print("Did not understand command, try again.")
            input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")
        elif input1 == 'e':
            message1 = input("Message: ")
            key1 = input("Key: ")
            key1 = list(key1)*(len(message1) / len(key1))
            
            
            msgnums = []
            for c in message1:
                msgnums.append(associations.find(c))
            
            keynums = []
            for c in key1:
                keynums.append(associations.find(c))
            
            for x,y in zip(msgnums,keynums):
                print(associations[x + y], end=" ")
            
            
            input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")
        elif input1 == 'd':
            message2 = input("Message: ")
            key2 = input("Key: ")
            input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if input1 == 'q':
    print("Goodbye!")