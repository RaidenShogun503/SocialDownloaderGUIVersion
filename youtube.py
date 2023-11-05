import yt_dlp
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

def taivideo():
    video_url = entry.get()
    if video_url:
        try:
            ydl_opts = {}
            with yt_dlp.YoutubeDL(ydl_opts) as ydl:
                info_dict = ydl.extract_info(video_url, download=False)
                video_title = info_dict.get("title", "Video Title")
                messagebox.showinfo("Thông báo", f"Đang tải video: {video_title}")
                ydl.download([video_url])
                messagebox.showinfo("Thông báo", f"Tải video {video_title} thành công!")
        except Exception as e:
            messagebox.showerror("Lỗi", f"Có lỗi xảy ra: {str(e)}")
    else:
        messagebox.showerror("Lỗi", "Vui lòng nhập URL video!")

root = Tk()
root.title("Youtube Downloader (Made by RaidenShogun508)")
root.minsize(300, 150)
root.maxsize(300, 150)

frm = ttk.Frame(root, padding=10)
frm.grid()

entry = ttk.Entry(frm, width=30)
entry.grid(column=0, row=2)
ttk.Label(frm, text="Nhập link cần tải vào đây").grid(column=0, row=0)
ttk.Button(frm, text="Nhấn để tải video", command=taivideo).grid(column=1, row=2)

root.mainloop()
