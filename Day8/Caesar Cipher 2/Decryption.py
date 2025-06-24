# Decode the message


alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']

wish = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
encoded_message = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def decrypt(encoded_message, shift):
    decode = ""

    for letters in encoded_message:
        original_position = alphabets.index(letters) - shift
        original_position %= len(alphabets)

        decode += alphabets[original_position]

    print(f"Decoded message : {decode}")

decrypt(encoded_message, shift)