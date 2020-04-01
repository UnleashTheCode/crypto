#!/usr/bin/python3

import argparse

parser = argparse.ArgumentParser(
        description="Caesar Encryptor/Decryptor.")

parser.add_argument("-dec",dest="mode",action="store_true",help="For decryption.")

args = parser.parse_args()

if args.mode == 0:
    text = input("Message to be encrypted: ")
    key = int(input("Key(Integer): ")) #luam cheia de tip integer
    encrypted = ""
    for char in text:
        if char != ' ':
            encrypted = encrypted + chr(ord(char)+key) #transformam caracterul in integer (ASCII) 
        else:                                           #si adunam cheia dupa care transformam inapoi in caracter
            encrypted = encrypted + ' '
    print ("Encrypted text is: {}".format(encrypted))
else:
    encrypted = input("Encrypted message to be decrypted: ")
    key = int(input("Key(Integer): "))
    text = ""
    for char in encrypted:
        if char != ' ':
            text = text + chr(ord(char)-key)            #transformam caracterul in integer (ASCII)
        else:                                           #si scadem cheia dupa care transformam inapoi in caracter
            encrypted = encrypted + ' '
    print ("Decrypted text is: {}".format(text))
