import os
from Crypto.Hash import SHA256

#Shared Path
path = '/home/cse/Lab3'

#Hash file we will use
with open(path + '/Q2hash.txt', 'r') as f:
    #Read the hash from the file
    hash = f.read().strip()

#List of files to check
files = [f for f in os.listdir(f'{path}/Q2files)') if os.path.isfile(os.path.join(f'{path}/Q2files', f))]

def get_sha256(file):
    '''returns the SHA-256 hash of the given file.'''
    h = SHA256.new()
    with open(file, 'rb') as f:
        data = f.read()
        #Read the file in binary mode
        #Update the hash with the data
        h.update(data)
    
    #return the hash    
    return h.hexdigest()



def find_matching_hash(hash, files):
    '''finds the file that has the same SHA-256 hash as the given hash.'''

    #Iterate through the files
    for file in files:
        #Get the hash of the file
        file_hash = get_sha256(file)
        #Check if the hash matches
        if file_hash == hash:
            #If it matches, return the file name
            return file

    #If no file matches, return None
    return None


if __name__ == '__main__':
    #Get the file that matches the hash
    file = find_matching_hash(hash, files)
    #Check if a file was found
    if file:
        print(f'File found: {file}')
    else:
        print('No file found')
