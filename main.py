from tkinter import*
BACKGROUND_COLOR = "#e9e9e9"
morse_dict = {'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.',
              'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.',
              'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-',
              'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--..', '1': '.----', '2': '..---',
              '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...', '8': '---..',
              '9': '----.', '0': '-----', '.': '.-.-.-', ',': '--.--', ':': '---...', '?': '..--..',
              "'": '.----.', '-': '-....-', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
              '"': '.-..-.', '=': '-...-', '+': '.-.-.', '@': '.--.-.', '!': '-.-.--',
              '&': '.-...', ';': '-.-.-.', '_': '..--.-', '$': '...-..-',  '': ' '}


def encrypt():
    code.delete('1.0', END)
    word = text.get(1.0, END).lower()
    word_encoded = ""
    for letter in word:
        try:
            word_encoded = word_encoded + morse_dict[letter] + ' '
        except KeyError:
            word_encoded += letter
    code.insert('1.0', word_encoded)


def decipher():
    text.delete('1.0', END)
    value = code.get(1.0, END).rstrip()
    value_list = value.split(' ')
    decrypted_word = ''
    for element in value_list:
        if element == "":
            decrypted_word += ' '
        elif element not in morse_dict.values():
            decrypted_word += element
        for k, v in morse_dict.items():
            if v == element:
                decrypted_word += k
    text.insert('1.0', decrypted_word)


window = Tk()
window.title("Text to Morse Code Converter")
window.config(padx=50, pady=50, background=BACKGROUND_COLOR)

canvas = Canvas(width=440, height=110, highlightthickness=1)
Morse_image = PhotoImage(file="Morse.png")
canvas.create_image(220, 60, image=Morse_image)
canvas.grid(column=0, row=0, columnspan=30)


label_1 = Label(text="Latin", background=BACKGROUND_COLOR)
label_1.grid(column=0, row=4)

text = Text(width=25, height=6, bg="white",
            fg='black', wrap=WORD)
text.grid(column=0, row=5, columnspan=2)

label_2 = Label(text="Morse code",background=BACKGROUND_COLOR )
label_2.grid(column=5, row=4)

code = Text(width=25, height=6, bg="white",
            fg='black', wrap=WORD)
code.grid(column=5, row=5, columnspan=2)

arrow = PhotoImage(file='arrow.png')
button_cipher = Button(image=arrow, width=12, height=12, command=encrypt)
button_cipher.grid(column=4, row=4)

arrow_left = PhotoImage(file='arrow_left.png')
button_decoder = Button(image=arrow_left, width=12, height=12, command=decipher)
button_decoder.grid(column=3, row=4)

window.mainloop()