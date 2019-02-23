'''
Help Text:
Before Running this program please look at the help text below for how to use
commands in order to run this script properlyself.

To use encryption use command:
python caesar.py --encrypt "Some String that you want to encrypt"

To use decryption use Command:
python caesar.py --decrypt "Some Cipher Text To Decrypt"

PS: Do not forget to put the String that you want to encrypt or decrypt in quotes.
Otherwise the script will give weird results.
'''


#Script Starts Here
import argparse
import random


key = 3  # The Key used for encryption or decryption

def encrypt(plainText):
    #Encyption code comes here
    cipherText = ""
    for c in plainText:

        if (c.isalpha()):
            if (c.isupper()):
                cipherText += chr(((ord(c) - ord('A') + key) % 26) + ord('A'))   # Shifting the characters by the key to the right for upper case
            else:
                cipherText += chr(((ord(c) - ord('a') + key) % 26) + ord('a'))  #Shifting the character by the key to the right for lower case
        else:
            cipherText += c

    print(cipherText)


def decrypt(cipherText):   # Function to decrypt the cipher Text back to PLain Text
    plainText = ""
    for c in cipherText:

        if (c.isalpha()):
            if (c.isupper()):
                plainText += chr(((ord(c) - ord('A') - key) % 26) + ord('A'))   #Shifting the characters to the left by the key for uppercase
            else:
                plainText += chr(((ord(c) - ord('a') - key) % 26) + ord('a'))   # Shifting the characters to the left by the key for lowercase
        else:
            plainText += c

    print(plainText)

    #Intialising the parser
parser = argparse.ArgumentParser(
    description="Arguments for Caesar Cypher Enrcyption and Descryption"
)

    #Adding first Argument for Encrypting the plaintext
parser.add_argument(
    "-e", "--encrypt",
    help = "String to Encrypt"
)
    #Adding second argument for decrypting the cipher text
parser.add_argument(
    "-d", "--decrypt",

    help = "String to decrypt"
)

arguments = vars(parser.parse_args())


plainText = arguments["encrypt"]
cipherText = arguments["decrypt"]

if (cipherText == None):
    encrypt(plainText)
else:
    decrypt(cipherText)
