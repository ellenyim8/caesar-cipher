import string 

alphabetTable = string.ascii_uppercase

def encrypt_example():
    file = open("example.txt", "r")

    content = file.read()
    #print(content)

    val = shiftValue(int(input()))
    
    # line = file.readline()
    encrypt = encryption(content, val)
    file.close()

    return encrypt 



def encryption(txt, val):
    # text is to be encrypted
    # val is shift value (1-25)
    encrypt = ""
    shift = shiftValue(val) 
    # print(shift) 
    shiftAlphabet = alphabetTable[shift:] + alphabetTable[:shift] 
    d = dict(zip(alphabetTable, shiftAlphabet))
    #for i, j in d.items():
    #    print(f" {i} : {j} ")

    #print(type(txt)) 
    for word in txt.split(" "):
        for letter in word:
            encrypt += d[letter]
    print(encrypt) 
    return encrypt 



def shiftValue(value):
    return (value % 26)



if __name__ == "__main__":
    encrypt_example()
