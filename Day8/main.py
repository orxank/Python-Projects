from library import alphabet
from art import logo

print(logo)

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()

if direction not in ['encode', 'decode']:
    print("You choosed invalid input!")
    quit()

text = input("Type your message:\n").lower()
shift_amount = int(input("Type the shift number:\n"))

def encrypt(text, shift_amount):

    cipher_message = ""
    
    for letter in text:

        if letter in alphabet:
            position = alphabet.index(letter)

        position += shift_amount
        encrypted_letter = alphabet[position]
        cipher_message += encrypted_letter

    print(f"The encoded text is {cipher_message}")


def decrypt(text, shift_amount):

    plain_message = ""

    for letter in text:

        if letter in alphabet:
            position = alphabet.index(letter)

        position -= shift_amount
        decrypt_letter = alphabet[position]
        plain_message += decrypt_letter
    
    print(f"The decoded text is {plain_message}")
            

       
if direction == "encode":
    encrypt(text, shift_amount)

if direction == "decode":
    decrypt(text, shift_amount)