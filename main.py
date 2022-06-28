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

##b'MkTIvoW0qJsa-Wn4UEru8f_lIOXeWflhDK8z8NN1MHA=



# create the root window
root = tk.Tk()
root.title('Steganografi')
root.resizable(True, True)
root.geometry('950x300')

root.columnconfigure(0, weight=1)
root.columnconfigure(1, weight=10)

selected = 0

def decodeTxt():
    pass

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

def embedTxt():
    txtInput = txt_entry.get()
    txtFormatted = bytes(txtInput,"utf-8")
    #key = Fernet.generate_key()zazxsazaqwedcxs
    cipher_suite = Fernet(b'MkTIvoW0qJsa-Wn4UEru8f_lIOXeWflhDK8z8NN1MHA=')

    encoded_text = cipher_suite.encrypt(txtFormatted)
    #decoded_text = cipher_suite.decrypt(encoded_text)

    #encodedTxt_label.config(text=txtFormatted)
    messagebox.showinfo("Metininiz",encoded_text)
    cv2.imshow("Output", img)
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


embedTxt_button = ttk.Button(root, text="Mesajı göm", command=embedTxt)
embedTxt_button.grid(column=1, row=4, sticky=tk.E, padx=5, pady=5)

info_label = ttk.Label(root, text="")
info_label.grid(column=0, row=5, sticky=tk.EW)



root.mainloop()




