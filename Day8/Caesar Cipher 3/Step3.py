# Encode Message

alphabets = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
 'u', 'v', 'w', 'x', 'y', 'z']

loop = "yes"

while loop == "yes":

    wish = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    message = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    # Encode Message
    def encrypt(message, shift):
        encode = ""

        for letters in message:
            shifted_position = alphabets.index(letters) + shift
            shifted_position %= len(alphabets) # to take only values from 0 -> 25 and then restart
            encode += alphabets[shifted_position]

        print(f"Encoded message {encode}")

    # Decode the message
    def decrypt(message, shift):
        decode = ""

        for letters in message:
            original_position = alphabets.index(letters) - shift
            original_position %= len(alphabets)

            decode += alphabets[original_position]

        print(f"Decoded message : {decode}")


    if wish == "decode":
        decrypt(message, shift)
    elif wish == "encode":
        encrypt(message, shift)
    else:
        print("Wrong input")

    loop = input("To Continue type 'yes'\nTo Stop type 'no\n").lower()