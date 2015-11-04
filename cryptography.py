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
let/num = [('a', 0),('b', 1),('c', 2),('d', 3),('e', 4),('f', 5),('g', 6),('h', 7),('i', 8),('j', 9),('k', 10),('l', 11),('m', 12),('n', 13),('o', 14),('p', 15),('q', 16),('r', 17),('s', 18),('t', 19),('u', 20),('v', 21),('w', 22),('x', 23),('y', 24),('z', 25),('A', 26),('B', 27),('C', 28),('D', 29),('E', 30),('F', 31),('G', 32),('H', 33),('I', 34),('J', 35),('K', 36),('L',37),('M', 38),('N', 39),('O', 40),('P', 41),('Q', 42),('R', 43),('S', 44),('T', 45),('U', 46),('V', 47),('W', 48),('X',49),('Y', 50),('Z', 51),('0', 47),('W', 48),('X',49),('Y', 50),('Z', 51),('V', 47),('W', 48),('X',49),('Y', 50),('9', 51)]

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