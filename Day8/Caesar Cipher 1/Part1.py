# Encode Message

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']

wish = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

encode = ""

def encrypt(message, shift):
   encode = ""

   for letters in message:
        shifted_position = alphabets.index(letters) + shift
        shifted_position %= len(alphabets) # to take only values from 0 -> 25 and then restart
        encode += alphabets[shifted_position]

   print(f"Encoded message {encode}")


encrypt(message, shift)