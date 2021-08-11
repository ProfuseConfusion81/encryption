from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives import hashes
from cryptography.hazmat.primitives.asymmetric import padding
import os
import time

# clear def

def clearScreen():
   os.system('cls' if os.name == 'nt' else 'clear')

# first we want to load the key

def keyLoader():
    clearScreen()
    print('')
    print('Enter Key File Name')
    print('')
    keyfilename = input('file name >> ')
    try:
        with open(str(keyfilename), "rb") as key_file:
            public_key = serialization.load_pem_public_key(
                key_file.read(),
                backend=default_backend()
            )
        fileLoader(keyfilename, public_key)
    except:
        print('')
        print('File not found!')
        time.sleep(3)
        keyLoader()

# now we want to get the file name from the user

def fileLoader(keyfilename, public_key):

    clearScreen()
    print('')
    print('Enter File Name')
    print('')
    filename = input('Enter File Name >> ')

    encrypto(keyfilename, public_key, filename)

# then we want to write the encrypted file

def encrypto(keyfilename, public_key, filename):
    f = open(str(filename), 'rb')

    message = f.read()

    f.close()

    encrypted = public_key.encrypt(
        message,
        padding.OAEP(
            mgf=padding.MGF1(algorithm=hashes.SHA256()),
            algorithm=hashes.SHA256(),
            label=None
        )
    )

    f = open('enc.encrypted', 'wb')
    f.write(encrypted)
    f.close()

# afterwards we want to print out the results, although I didn't do it
# here in the encrypt script because im lazy. it will just close when its done



keyLoader()