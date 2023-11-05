import requests
import re
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def taivideo():
    url = "https://tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com/vid/index"

    layurl = entry.get()
    querystring = {"url":layurl}
    headers = {
        "X-RapidAPI-Key": "4ba4421df8mshd017caa9b41abdfp15e1b2jsn79bc2f27180f",
        "X-RapidAPI-Host": "tiktok-downloader-download-tiktok-videos-without-watermark.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    video = response.text
    video = video.replace('[','')

    link = re.findall(r'{"video":"([^"]+)"',video)
    url_video = ''.join(link)
    messagebox.showinfo("Thông Báo", f"Đã Tải Video Thành Công!")
    names = random.randrange(1, 1000)
    name = 'video'+str(names)+'.mp4'

    r = requests.get(url_video)
    with open(name, 'wb') as f:
        f.write(r.content)



root = Tk()
root.title("Tiktok Downloader (Made by RaidenShogun508)")
root.minsize(300, 150)
root.maxsize(300, 150)

frm = ttk.Frame(root, padding=10)
frm.grid()

ttk.Label(frm, text="Nhập Link cần tải vào đây").grid(column=0, row=0)
entry = ttk.Entry(frm, width=30)
entry.grid(column=0, row=2)
ttk.Button(frm, text="Nhấn để tải video", command=taivideo).grid(column=1, row=2)

root.mainloop()