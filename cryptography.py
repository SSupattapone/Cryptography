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
let/num = [('a', 0),('b', 1),('c', 2),('d', 3),('e', 4),('f', 5),('g', 6),('h', 7),('i', 8),('j', 9),('k', 10),('l', 11),('m', 12),('n', 13),('o', 14),('p', 15),('q', 16),('r', 17),('s', 18),('t', 19),('u', 20),('v', 21),('w', 22),('x', 23),('y', 24),('z', 25),]

while input1 != 'q':
    for x in ['a','b','c','f','g','h','i','j','k','l','m','n','o','p','r','s','t','u','v','w','x','y','z']:
        if x == str(input1):
            print("Did not understand command, try again.")
            input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")
        elif input1 == 'e':
            message1 = input("Message: ")
            key1 = input("Key: ")
            input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")
        elif input1 == 'd':
            message2 = input("Message: ")
            key2 = input("Key: ")
            input1 = input("Enter e to encrypt, d to decrypt, or q to quit: ")

if input1 == 'q':
    print("Goodbye!")