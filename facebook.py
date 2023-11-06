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
    querystring = {"url": nhapurl}

    headers = {
        "X-RapidAPI-Key": "ea26619e18mshcc8a1b5bee643dbp1ca309jsna56e31c8df7f",
        "X-RapidAPI-Host": "facebook-video-downloader7.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    if response.status_code == 200:
        try:
            hd_link = response.json()["hd"]
            r = requests.get(hd_link)
            names = random.randrange(1, 1000)
            name = 'video' + str(names) + '.mp4'
            with open(name, 'wb') as f:
                f.write(r.content)
            messagebox.showinfo("Thông báo!", f"Đã tải video thành công!")
        except (KeyError, ValueError):
            messagebox.showerror("Lỗi", "Không thể tải video hoặc lỗi khi xử lý dữ liệu!")
    else:
        messagebox.showerror("Lỗi", f"Lỗi khi tải video: {response.status_code}.Vui lòng xem lại link tải hoặc báo cáo lỗi qua github https://github.com/RaidenShogun503/SocialDownloaderGUIVersion")

root = Tk()
root.title("Facebook Downloader (Made by Raidenshogun503)")
root.minsize(300, 150)
root.maxsize(300, 150)
icon_path = "icon.ico"
root.iconbitmap(icon_path)

frm = ttk.Frame(root, padding=10)
frm.grid()

entry = ttk.Entry(frm, width=30)
entry.grid(column=0, row=2)
ttk.Label(frm, text="Nhập link cần tải vào đây").grid(column=0, row=0)
ttk.Button(frm, text="Nhấn để tải video", command=download_video).grid(column=1, row=2)

root.mainloop()
