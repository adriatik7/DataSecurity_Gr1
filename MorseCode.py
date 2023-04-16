import winsound
import time

morse_code_dict = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.'}

def encode_morse_code(text):
    text = text.upper()
    encoded_text = []
    for char in text:
        if char == ' ':
            encoded_text.append('/')
        else:
            encoded_text.append(morse_code_dict[char])
    return ' '.join(encoded_text)

def decode_morse_code(encoded_text):
    encoded_text = encoded_text.split(' ')
    decoded_text = []
    for char in encoded_text:
        if char == '/':
            decoded_text.append(' ')
        else:
            for key, value in morse_code_dict.items():
                if char == value:
                    decoded_text.append(key)
    return ''.join(decoded_text)

def play_morse_code(encoded_text):
    dot_duration = 100  # milliseconds
    dash_duration = dot_duration * 3
    space_duration = dot_duration
    char_space_duration = dot_duration * 3
    for char in encoded_text:
        if char == '.':
            winsound.Beep(440, dot_duration)
        elif char == '-':
            winsound.Beep(440, dash_duration)
        elif char == '/':
            winsound.Beep(37, space_duration)
        else:
            continue
        time.sleep(char_space_duration / 1000)

def main():
    print('Morse Code Encoder/Decoder')
    while True:
        choice = input('Enter "1" to encode, "2" to decode, or "0" to quit: ')
        if choice == '0':
            print('Goodbye!')
            break
        elif choice == '1':
            text = input('Enter text to encode: ')
            encoded_text = encode_morse_code(text)
            print('Encoded text:', encoded_text)
            play_morse_code(encoded_text)
        elif choice == '2':
            encoded_text = input('Enter Morse code to decode: ')
            decoded_text = decode_morse_code(encoded_text)
            print('Decoded text:', decoded_text)
        else:
            print('Invalid choice, please try again.')

if __name__ == '__main__':
    main()