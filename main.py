from base64 import decode
from doctest import master
from fileinput import filename
from logging import exception
from tkinter import messagebox
from types import NoneType
from cryptography.fernet import Fernet
import tkinter as tk
from tkinter import  Grid, Radiobutton, ttk
from tkinter import filedialog as fd
from tkinter.messagebox import showinfo
import cv2
from PIL import Image
import steganografi
##b'MkTIvoW0qJsa-Wn4UEru8f_lIOXeWflhDK8z8NN1MHA=



# create the root window
root = tk.Tk()
root.title('Steganografi')
root.resizable(True, True)
root.geometry('950x300')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)

selected = 0
steg = steganografi.Main()

def select_file():
    filetypes = (
        ('Image ', '*.jpg , *.png , *.jpeg'),
        ('All files', '*.*')
    )

    filename = fd.askopenfilename(
        title='Bir resim secin',
        initialdir='/',
        filetypes=filetypes)

    showinfo(
        title='Secilen dosya',
        message=filename
    )
    global img
    img = cv2.imread(filename)
    if (type(img) != NoneType):
        info_label.config(text="Resim yüklendi")
    else:
        info_label.config(text="Resim yükleme başarısız")

def decodedData(bits):
    all_bytes = [ bits[i: i+8] for i in range(0, len(bits), 8) ]
    decoded_data = ""
    for byte in all_bytes:
        decoded_data += chr(int(byte, 2))
        if decoded_data[-5:] == "#####": #check if we have reached the delimeter which is "#####"
          break
  #print(decoded_data)
    return decoded_data[:-5]

def decodeTxt():
    key = key_entry.get()
    keyB = bytes(key,"utf-8")
    
    cipher_suite = Fernet(keyB)

    encoded_text = steg.decode(img)
    encoded_textB = bytes(encoded_text,"utf-8")
    #print(encoded_textB)
    encoded_text = decodedData(encoded_textB)
    encoded_textB = bytes(encoded_text, "utf-8")
    decoded_text = cipher_suite.decrypt(decodedData(encoded_textB))

    print(decoded_text)
    # try:
    #      key = key_entry.get()
    #      #keyFormatted = bytes(key,"ascii")
    # except:
    #      info_label.config(text="Key kısmı hatalı")


    # cipher_suite = Fernet(key)
    # # print(cipher_suite)
    # # print(type(cipher_suite))
    # encoded_text = steg.decode(img)

    # print(encoded_text)
    # print(type(encoded_text))
    # encoded_text = bytes(encoded_text,"ascii")
    # decoded_text = cipher_suite.decrypt(encoded_text)
    # # print(decoded_text)
    # # print(type(decoded_text))
    # messagebox.showinfo("Decoded text",decoded_text)
    # # # decoded_text = cipher_suite.decrypt(encoded_textb)
    
    # # # print(decoded_text)
    # # # messagebox.showinfo("Decoded", decoded_text)
    # return 0



def encodeTxt():
    txtInput = txt_entry.get()
    if(len(txtInput) == 0 ):
        info_label.config(text="Mesaj kısmı boş bırakılamaz")
        return 0
    txtInput = txtInput + "#####"
    txtFormatted = bytes(txtInput,"utf-8")

    keyInput = key_entry.get()
    
    if (keyInput == ""):
        #KEY GİRİLMEDİYSE

        key = Fernet.generate_key()
        cipher_suite = Fernet(key)
        encoded_text = cipher_suite.encrypt(txtFormatted)
        messagebox.showinfo("Metininiz",encoded_text)
        with open('key.txt',"w") as f:
            f.write(str(key.decode("utf-8")))

        #encoded_img = steg.encode(encoded_text,img)
        print(encoded_text)
        steg.encode(encoded_text,img)
    else:        
        #KEY GİRİLDİYSE
        #keyFormatted = bytes(keyInput,"ascii")
        cipher_suite = Fernet(keyInput)
        encoded_text = cipher_suite.encrypt(txtFormatted)
        
        #encodedTxt_label.config(text=txtFormatted)
        messagebox.showinfo("Metininiz",encoded_text)
        print(encoded_text)
        cv2.imshow("Output", img)
        steg.encode(encoded_text,img)
        
    return 0


img_label = ttk.Label(root, text="Bir resim seçin :")
img_label.grid(column=0, row=0, sticky=tk.W, padx=5, pady=5)

open_button = ttk.Button(root, text="Bir resim seçin", command=select_file)
open_button.grid(column=1, row=0, sticky=tk.EW, padx=5, pady=5,ipadx=3,ipady=3, columnspan=3)

txt_label = ttk.Label(root, text="Gömülecek metni girin :")
txt_label.grid(column=0, row=1, sticky=tk.W, padx=5, pady=5)

txt_entry = ttk.Entry(root)
txt_entry.grid(column=1, row=1, sticky=tk.EW, padx=5, pady=5)

key_label = ttk.Label(root, text="Şifrelemek için anahtarınızı girin :")
key_label.grid(column=0, row=2, sticky=tk.W, padx=5, pady=5)

key_entry = ttk.Entry(root)
key_entry.grid(column=1, row=2, sticky=tk.EW, padx=5, pady=5)

decode_button = ttk.Button(root, text="Mesajı çöz", command=decodeTxt)
decode_button.grid(column=0, row=4, sticky=tk.E, padx=5, pady=5)

embedTxt_button = ttk.Button(root, text="Mesajı göm", command=encodeTxt)
embedTxt_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

info_label = ttk.Label(root, text="")
info_label.grid(column=0, row=5, sticky=tk.EW)






root.mainloop()