
import hashlib
import sys

word_list = []
hashedValues = []
saltValues = []
passwords = []
formSpringHashes = []

input = open("word_list.txt",'r',encoding="utf-8")
salts = [str(x).zfill(2) for x in range(100)]

for line in input.read().splitlines():
    for i in salts:
        pSalted = i + line
        hashValue = hashlib.sha256(pSalted.encode("utf8")).hexdigest()
        print(hashValue)
        hashedValues.append(hashValue)
        passwords.append(line)
        saltValues.append(i)





def formSpringHashes():
    output = open("formspring.txt","r",encoding="utf-8")
    z = []
    for out in output.read().splitlines():
        z.append(out)

    return z



formSpringHashes = formSpringHashes()

for i in range(len(hashedValues)):
    for j in range(len(formSpringHashes)):
        if (hashedValues[i] == formSpringHashes[j]):
            sys.stdout = open('cracked.txt','a',encoding='utf-8')
            print(formSpringHashes[j], ':', passwords[i],':',  'salt =', saltValues[i],)
            sys.stdout.close()
            break
