#dedicated to beb <3
from art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z','a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

running = True
while running == True: 
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n")) % 26

    def caesar(direction, text, shift):
        message = ''
        if direction == "decode":
            shift *= -1
        
        for letter in text:
            if letter in alphabet:
                new = alphabet.index(letter) + shift
                message += alphabet[new]
            else:
                message += letter
                continue
                
        print(f"The {direction}d text is: {message}")

    caesar(direction=direction, text=text, shift=shift)

    play_again = input("Do you want to play again? yes or no\n")

    if play_again == "no":
        running = False

