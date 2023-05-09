from tkinter import *
from pytube import YouTube

win=Tk()
win.title("converter")
win.geometry("400x200+600+300")
win.config(background="#323232")
win.attributes("-alpha",0.75)
win.resizable(False,False)


title_text=Label(text="converter",fg="skyblue",bg="#323232")
#obj.config(font="字形 大小")
title_text.config(font="微軟正黑體 15")
title_text.pack()

link=Label(text="連結",fg="white",bg="#323232",width=20)
link.config(font="微軟正黑體 13")
link.pack()
linken=Entry()
linken.pack()

show=Label(text="",fg="white",bg="#323232")
show.pack()

def download():
    try:
        
        yt = YouTube(linken.get())
        video = yt.streams.get_by_resolution("720p")
        video.download()
        show.config(text="下載成功!",font="微軟正黑體 8")
        show.pack()
    except Exception as error:
        show.config(text=f"ERROR: {error}",fg="#da0200",bg="#323232",font="微軟正黑體 8")
        show.pack()
btn=Button(text="下載",command=download)
btn.pack()

win.mainloop()