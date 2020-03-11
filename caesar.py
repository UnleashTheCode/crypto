#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(
        description="Caesar Encryptor/Decryptor.")

parser.add_argument("-dec",dest="mode",action="store_true",help="For decryption.")

args = parser.parse_args()

if args.mode == 0:
    text = input("Message to be encrypted: ")
    key = int(input("Key(Integer): "))
    encrypted = ""
    for char in text:
        encrypted = encrypted + chr(ord(char)+key)
    print ("Encrypted text is: {}".format(encrypted))
else:
    encrypted = input("Encrypted message to be decrypted: ")
    key = int(input("Key(Integer): "))
    text = ""
    for char in encrypted:
        text = text + chr(ord(char)-key)
    print ("Decrypted text is: {}".format(text))
