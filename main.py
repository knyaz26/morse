
import tkinter as tk
from tkinter import ttk
import json

with open('crypt.json', 'r') as f:
    morse_dict = json.load(f)
encode_dict = {v: k for k, v in morse_dict.items()}

def decoder(morse_string):
    return ''.join(morse_dict.get(code, '?') for code in morse_string.split('/'))

def encoder(text):
    text = text.upper()
    return '/'.join(encode_dict.get(char, '?') for char in text)

def translate():
    inp = input_text.get("1.0", "end").strip()
    if all(c in '.-/ ' for c in inp) and '/' in inp:
        out = decoder(inp)
    else:
        out = encoder(inp)
    output_text.config(state='normal')
    output_text.delete("1.0", "end")
    output_text.insert("1.0", out)
    output_text.config(state='disabled')

root = tk.Tk()
root.title("Morse Code Translator")
root.geometry('640x360')

frame = ttk.Frame(root, padding=20)
frame.pack(expand=True)
frame.place(relx=0.5, rely=0.5, anchor='center')

ttk.Label(frame, text="Input").pack(pady=(0, 5))

input_text = tk.Text(frame, height=5, width=40)
input_text.pack()

ttk.Button(frame, text="Translate", command=translate).pack(pady=10)

ttk.Label(frame, text="Output").pack(pady=(0, 5))

output_text = tk.Text(frame, height=10, width=40, state='disabled')
output_text.pack()

root.mainloop()
