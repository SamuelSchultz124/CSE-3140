#Defender Decryption Software

#Importing necessary libraries
import sys
import os
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad


#Get the encrypted file name from the command line
if len(sys.argv) != 2:
    print("Usage: python AD6.py <decryption_key>")
    sys.exit(1)

#Get the decryption key from the command line
decryption_key = sys.argv[1]

#Open the decryption key
with open(decryption_key, 'rb') as key_file:
    key = key_file.read()

#Iterate through all files in the current directory
for filename in os.listdir():
    #Check if the file is an encrypted file
    if filename.endswith('.encrypted'):
        
        #Open the encrypted file
        with open(filename, 'rb') as encrypted_file:
            plaintext = encrypted_file.read()

            #Extract the IV and ciphertext
            iv = plaintext[:AES.block_size]
            ciphertext = plaintext[AES.block_size:]

            #Decrypt the file
            cipher = AES.new(key, AES.MODE_CBC)
            decrypted = unpad(cipher.decrypt(plaintext), AES.block_size)
        
            #Restore the Decrypted file
            with open(filename[:-10], 'wb') as decrypted_file:
                decrypted_file.write(decrypted[AES.block_size:])
