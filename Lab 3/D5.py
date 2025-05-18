#Decryption File designed to match a specific Encryption File
from Crypto.Cipher import AES   
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes
from Crypto.Hash import MD5

path = '/home/cse/Lab3/Q5files'

#Removing the Obsfucation leaving only the relevant lines of code
h = MD5.new()
BLOCKSIZE = 2048
with open(f'{path}/R5.py', 'rb') as afile:
    buf = afile.read(BLOCKSIZE)
    while len(buf) > 0:
        h.update(buf)
        buf = afile.read(BLOCKSIZE)

#This is our Variable
hf = h.hexdigest()
var = hf

encrypted_file = 'Encrypted5'

#Decrypt the file
with open(f'{path}/{encrypted_file}', 'rb') as f:
    #Read the encrypted file
    ciphertext = f.read()
    #Decrypt the file
    cipher = AES.new(var, AES.MODE_CBC)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    #Write the decrypted file
    with open(f'/home/cse/Lab3/Solutions/Decrypted5', 'wb') as f:
        f.write(plaintext)
