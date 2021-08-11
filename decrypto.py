import os
import time
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding

def clearScreen():
   os.system('cls' if os.name == 'nt' else 'clear')

# load priv key

def pkeyLoader():
    clearScreen()
    print('')
    print('Enter Private Key File')
    print('')
    pkeyfilename = input('File Name >> ')
    try:
        with open(str(pkeyfilename), "rb") as key_file:
            private_key = serialization.load_pem_private_key(
                key_file.read(),
                password=None,
                backend=default_backend()
            )
        pfileLoader(pkeyfilename, private_key)
    except:
        print('')
        print('File Not Found!') 
        time.sleep(3)
        pkeyLoader()   

# get enc file name

def pfileLoader(pkeyfilename, private_key):
    clearScreen()
    print('')
    print('Enter Encrypted File Name')
    print('')
    encfilename = input('Enter File Name >> ')
    decrypto(pkeyfilename, private_key, encfilename)

# write it to a user designated file name and extension

def decrypto(pkeyfilename, private_key, encfilename):
    clearScreen()
    enddest = input("Choose File Name >> ")
    endext = input("File Extension >> ")

    f = open(str(encfilename), 'rb')
    encrypted = f.read()
    f.close()

    original_message = private_key.decrypt(
        encrypted,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )
    
    f = open(str(enddest + '.' + endext), 'wb')
    f.write(original_message)
    f.close()

    finalfilename = str(enddest + '.' + endext)
    clearScreen()
    endScreen(pkeyfilename, encfilename, finalfilename)

# display the results, did it in this script but not the encrypt script.

def endScreen(pkeyfilename, encfilename, finalfilename):
    clearScreen()
    print('')
    print(f'The encrypted file \'{encfilename}\' was decrypted to \'{finalfilename}\' using the key from \'{pkeyfilename}\'')
    input()

pkeyLoader()