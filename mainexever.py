import subprocess
import ctypes
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("SocialDownloader(Made by RaidenShogun508)")
root.minsize(200, 120)
root.maxsize(200, 120)
icon_path = "icon.ico"
root.iconbitmap(icon_path)

otiktok = "tiktok.exe"
oyoutube= "youtube.exe"
ofacebook = "facebook.exe"

def youtube():
    subprocess.run(oyoutube)
    root.destroy()
def tiktok():
    subprocess.run(otiktok)
    root.destroy()
def facebook():
    subprocess.run(ofacebook)
    root.destroy()


frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Vui Lòng Chọn nền tảng cần tải!").grid(column=0, row=0)
ttk.Button(frm, text="Youtube", command=youtube).grid(column=0, row=1)
ttk.Button(frm, text="Facebook", command=facebook).grid(column=0, row=2)
ttk.Button(frm, text="Tiktok", command=tiktok).grid(column=0, row=3)


root.mainloop()