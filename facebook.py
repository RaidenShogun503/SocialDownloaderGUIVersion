import re
import requests
import json
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def get_download_high_quality_url(json_data):
    links = json_data.get('links', {})
    downloads_high_quality_url = links.get("hd", "")
    return downloads_high_quality_url

def download_video():
    nhapurl = entry.get()
    url = "https://facebook-video-downloader7.p.rapidapi.com/"
    querystring = {"url":nhapurl}

    headers = {
        "X-RapidAPI-Key": "ea26619e18mshcc8a1b5bee643dbp1ca309jsna56e31c8df7f",
        "X-RapidAPI-Host": "facebook-video-downloader7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)
    hd_link = response.json()["hd"]
    print(hd_link)
    messagebox.showinfo("Thông báo!", f"Đã tải video thành công!")
    r = requests.get(hd_link)
    names = random.randrange(1, 1000)
    name = 'video'+str(names)+'.mp4'
    r = requests.get(hd_link)
    with open (name, 'wb') as f:
        f.write(r.content)
root = Tk()
root.title("Facebook Downloader (Made by Raidenshogun508)")
root.minsize(300, 150)
root.maxsize(300, 150)

frm = ttk.Frame(root, padding=10)
frm.grid()

entry = ttk.Entry(frm, width=30)
entry.grid(column=0, row=2)
ttk.Label(frm, text="Nhập link cần tải vào đây").grid(column=0, row=0)
ttk.Button(frm, text="Nhấn để tải video", command=download_video).grid(column=1, row=2)

root.mainloop()
