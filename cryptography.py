"""
cryptography.py
Author: Sam Supattapone
Credit: none

Assignment: Cryptography

Write and submit a program that encrypts and decrypts user data.

See the detailed requirements at https://github.com/HHS-IntroProgramming/Cryptography/blob/master/README.md
"""
associations = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789 .,:;'\"/\\<>(){}[]-=_+?!"
input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")

while str(input1) != 'q':
    for x in ['a','b','c','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']:
        if x == str(input1):
            print("Did not understand command, try again.")
            input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")
        elif str(input1) == 'e':
            message = input("Message: ")

if str(input1) == 'q':
    print("Goodbye!")