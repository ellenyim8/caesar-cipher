import string 

alphabet = string.ascii_uppercase 
print(alphabet)

def shiftValue(val):
    return (val % 25) + 1 

shift = shiftValue(int(input())) 
print(shift) 

shiftAlphabet = alphabet[shift:] + alphabet[:shift] 
table = dict(zip(alphabet, shiftAlphabet)) 
for k, v in table.items():
    print(f" {k} : {v} ")



