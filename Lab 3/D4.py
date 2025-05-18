#Decryption File designed to match a specific Encryption File
from Crypto.Cipher import AES   
from Crypto.Util.Padding import unpad
from Crypto.Random import get_random_bytes

path = '/home/cse/Lab3/Q4files'

#Generate your random plaintext
variable = b"o\x014\xdc\xef(\x08n\x9bG\xc01\xed'\x0e\xa0"
var = str(variable)

encrypted_file = 'Encrypted4'


#Decrypt the file
with open(f'{path}/{encrypted_file}', 'rb') as f:
    #Read the encrypted file
    ciphertext = f.read()
    #Decrypt the file
    cipher = AES.new(variable, AES.MODE_CBC)
    plaintext = unpad(cipher.decrypt(ciphertext), AES.block_size)
    #Write the decrypted file
    with open(f'/home/cse/Lab3/Solutions/Decrypted4', 'wb') as f:
        f.write(plaintext)
