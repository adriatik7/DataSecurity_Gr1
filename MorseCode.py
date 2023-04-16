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
