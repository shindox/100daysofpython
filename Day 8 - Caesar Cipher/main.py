from art import logo

alphabet = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
    'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd',
    'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's',
    't', 'u', 'v', 'w', 'x', 'y', 'z'
]


def caesar(start_text, shift_number, direction):
    end_text = ""
    if direction == "decode" or direction == "d":
        shift_number *= -1

    for letter in start_text:
        if letter not in alphabet:
            end_text += letter
        else:
            new_index = (alphabet.index(letter) + shift_number) % len(alphabet)
            end_text += alphabet[new_index]

    if direction == "encode" or direction == "e":
        print(f"The encoded text is: {end_text}\n")

    elif direction == "decode" or direction == "d":
        print(f"The decoded text is: {end_text}\n")


print(logo)

while True:
    direction = input(
        "Type '(e)ncode' to encrypt, '(d)ecode' to decrypt, or '(q) to quit':\n"
    )
    if direction == "q":
        print("Goodbye")
        break
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(start_text=text, shift_number=shift, direction=direction)
