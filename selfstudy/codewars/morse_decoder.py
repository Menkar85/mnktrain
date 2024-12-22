
MORSE_CODE = {
    '.-': 'A', '-...': 'B', '-.-.': 'C', '-..': 'D', '.': 'E', '..-.': 'F',
    '--.': 'G', '....': 'H', '..': 'I', '.---': 'J', '-.-': 'K', '.-..': 'L',
    '--': 'M', '-.': 'N', '---': 'O', '.--.': 'P', '--.-': 'Q', '.-.': 'R',
    '...': 'S', '-': 'T', '..-': 'U', '...-': 'V', '.--': 'W', '-..-': 'X',
    '-.--': 'Y', '--..': 'Z',
    '-----': '0', '.----': '1', '..---': '2', '...--': '3', '....-': '4',
    '.....': '5', '-....': '6', '--...': '7', '---..': '8', '----.': '9',
    '.-.-.-': '.', '--..--': ',', '..--..': '?', '.----.': "'", '-.-.--': '!',
    '-..-.': '/', '-.--.': '(', '-.--.-': ')', '.-...': '&', '---...': ':',
    '-.-.-.': ';', '-...-': '=', '.-.-.': '+', '-....-': '-', '..--.-': '_',
    '.-..-.': '"', '...-..-': '$', '.--.-.': '@', '...---...': 'SOS'
}


def decode_bits(bits):
    # ToDo: Accept 0's and 1's, return dots, dashes and spaces
    bits = bits.strip('0')
    list_bits = [i for i in bits]
    i = 0
    while i < len(list_bits):
        if i > 0 and list_bits[i] != list_bits[i-1]:
            list_bits.insert(i, " ")
            i += 2
        else:
            i += 1
    str_bits = ''.join(list_bits)
    list_bits = str_bits.split()
    q = len(sorted(list_bits, key=len)[0])
    for item in list_bits:
        if "1" * q > item > "111" * q:
            item = "1" * q

    return bits.replace('111' * q, '-').replace('000' * q, ' ').replace('1'*q, '.').replace('0'*q, '')


def decode_morse(morseCode):
    message = morseCode.split(' ')
    dec_message = ""
    for letter in message:
        if len(letter) and letter != " ":
            dec_letter = MORSE_CODE[letter]
        else:
            dec_letter = " "
        dec_message += dec_letter

    return dec_message


print(decode_morse(decode_bits("00111000111000111")))
