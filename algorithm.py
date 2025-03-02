
import string 

upper_alphabet = string.ascii_uppercase
# lower_alphabet = string.ascii_lowercase


def shift(value):
    # returns a value between 1 - 26 
    return (value % 26) + 1


def caesarEncryption(txt, dict):
    # encryption 
    encrypted_txt = ""
    for word in txt.split(" "):
        for letter in word:
            encrypted_txt += dict[letter]
    
    return encrypted_txt


def caesarDecryption(txt, dict):
    # decryption 
    decrypted_txt = ""
    for word in txt.split(" "):
        for letter in word:
            decrypted_txt += dict[letter]

    return decrypted_txt


def main():
    # main code 
    value = int(input()) 

    shift_val = shift(value) 
    print(shift_val) 

    shifted_alphabet = upper_alphabet[shift_val:] + upper_alphabet[:shift_val]
    table = dict(zip(upper_alphabet, shifted_alphabet)) 

    text = input() 

    encrypt_txt = caesarEncryption(text, table)

    print("Your encrypted text: ")
    print(encrypt_txt, "\n")

    reverse_table = dict(zip(shifted_alphabet, upper_alphabet))
    decrypt_txt = caesarDecryption(encrypt_txt, reverse_table)

    # print("your original message: ")
    # print(decrypt_txt, "\n")


main() 
