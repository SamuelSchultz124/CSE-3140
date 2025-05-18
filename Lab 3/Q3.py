from Crypto.Hash import SHA256
from Crypto.Signature import pkcs1_15
from Crypto.PublicKey import RSA
import os

#Shared Path
path = '/home/cse/Lab3'

#open the public key file
with open(f'{path}/Q3pk.pem', 'rb') as f:
    #Read the public key from the file
    public_key = f.read()


#list of files
files = []

#Iterate through the files in the directory
for file in os.listdir(f'{path}/Q3files'):
    #check if the file is a signature
    if file.endswith('.exe'):
        #add to list of signatures
        files.append(file)





def verify_signature(signature, message, public_key):
    """
    Verify the signature of a message using the public key.

    :param signature: The signature to verify.
    :param message: The original message.
    :param public_key: The public key to use for verification.
    :return: True if the signature is valid, False otherwise.
    """
    #load the signature and message
    with open(f'{path}/Q3files/{signature}', 'rb') as f: signature = f.read()
    with open(f'{path}/Q3files/{message}', 'rb') as f: message = f.read()

    #Gererate the hash of the message
    h = SHA256.new(message)
    #import the public key
    rsa = RSA.import_key(public_key) 
    #Create the signer object
    singer = pkcs1_15.new(rsa)
    #Verify the signature
    try:
        #Verify the signature
        singer.verify(h, signature)
        #If the signature is valid, return True
        return True
    except (ValueError, TypeError):
        #If the signature is invalid, return False
        return False


if __name__ == '__main__':
    #Iterate through the files and signatures
    for file in files:
        #Get the signature for the file
        signature = f'{file}.sign'
        #Verify the signature
        result = verify_signature(signature, file, public_key)
        #Check if the signature is valid
        if result:
            print(f'Success {file} is correctly signed')
        else:
            print(f'Failed {file} is not correctly signed')