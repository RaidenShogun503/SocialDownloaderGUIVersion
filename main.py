import subprocess
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
root = Tk()
root.title("SocialDownloader(Made by RaidenShogun508)")
root.minsize(250, 300)
root.maxsize(250, 300)

def youtube():
    subprocess.call(["python", "youtube.py"])
    root.destroy()
def tiktok():
    subprocess.call(["python", "tiktok.py"])
    root.destroy()
def facebook():
    subprocess.call(["python", "facebook.py"])
    root.destroy()
def thuvien():
    subprocess.call(["pip", "install", "-r", "requirements.txt"])

    messagebox.showinfo("Thông Báo", f"Đã cài đặt Thư viện Xong!")

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Vui Lòng Chọn nền tảng cần tải!").grid(column=0, row=0)
ttk.Button(frm, text="Youtube", command=youtube).grid(column=0, row=1)
ttk.Button(frm, text="Facebook", command=facebook).grid(column=0, row=2)
ttk.Button(frm, text="Tiktok", command=tiktok).grid(column=0, row=3)
ttk.Label(frm, text="Nhấn vào nút này để cài thư viện cần thiết").grid(column=0, row=4)
ttk.Button(frm, text="Nhấn Để cài", command=thuvien).grid(column=0, row=5)

root.mainloop()