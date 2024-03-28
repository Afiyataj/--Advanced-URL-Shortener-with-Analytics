import pyperclip
import pyshorteners
from tkinter import *

gui = Tk()
gui.geometry("400x200")
gui.title("URL Shortener")
gui.configure(bg="#49A")
url = StringVar()
url_address = StringVar()

def urlshortener():
    urladdress = url.get()
    url_short = pyshorteners.Shortener().tinyurl.short(url_address)
    url_address.set(url_short)

def copyurl():
    url_short = url_address.get()
    pyperclip.copy(url_short)

Label(gui, text="My URL Shortener", font="poppins").pack(pady=10)
Entry(gui, textvariable=url).pack(pady=5)
Button(gui, text="Generate Short URL", command=urlshortener).pack(pady=7)
Entry(gui, textvariable=url_address).pack(pady=5)
Button(gui, text="Copy URL", command=copyurl).pack(pady=5)

gui.mainloop()
