
import json

with open('crypt.json', 'r') as f:
    crypt = json.load(f)

def decoder(morse_string):
    return ''.join(crypt.get(code, '?') for code in morse_string.split('/'))

def encoder(text):
    text = text.upper()
    return '/'.join(crypt.get(chat, '?') for char in text)

