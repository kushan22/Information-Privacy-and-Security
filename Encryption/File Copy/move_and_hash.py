'''
Help Text:
Before Running the script please read the help text below
To run the script use the command:
python move_and_hash.py --scramble

Please make sure the directory structure is the same as it is.
Do not change the directory structure or move files from one place to another.

The Scripts starts below...
'''




#All the libraries needed in the program
import os
import shutil
import hashlib
import argparse


#Checking the hash before the file has been copied
def sha256HashCheck(path):
    with open(path,'rb') as f:
        bytes = f.read()
        result = hashlib.sha256(bytes).hexdigest()
    return result



#function used to scramble the byte and check the hashes again
def scrambleByte(path):

    with open(path,'rb') as f:
        file = f.read()
        # Scrambling a byte by swapping two characters
        byteArray = [elem.encode("hex") for elem in file]
        byteArray[0],byteArray[1] = byteArray[1],byteArray[0]
        asciiArray = [int(elem,16) for elem in byteArray]
        file = ''.join(chr(elem) for elem in asciiArray)


        f.close()

    with open(path,'w') as f1:
        f1.write(file)
        f1.close()

    #Checking the hashes after scrambling the byte
    hashBefore = sha256HashCheck(srcPath)
    hashAfter = sha256HashCheck(destPath)

    if (hashBefore == hashAfter):
        print("Hashes Match")
    else:
        print("Hashes doesn't match")



#Intialising the argument parser
parser = argparse.ArgumentParser(
    description="Argument for scrambling a byte in the file"
)

#Adding argument to the parser
parser.add_argument(
    "--scramble",
    action="store_true",
    help = "Scramble Argument"
)



args = parser.parse_args()


src = './a'
dest = './b'

#Using Shitil Library to copy the file
srcPath = os.path.join(src,'file.txt')
destPath = os.path.join(dest,'file.txt')
shutil.copyfile(srcPath,destPath)

#Checking hashes after Copying the file
shaHashBefore = sha256HashCheck(srcPath)
shaHashAfter = sha256HashCheck(destPath)

if (shaHashBefore == shaHashAfter):
    print("Hashes Match")
else:
    print("Hashes Doesn't Match")



if (args.scramble):
    print("Srambling the byte and checking hashes again")
    scrambleByte(destPath) #Calling Scramble Byte Function
