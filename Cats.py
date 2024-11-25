from http.client import responses
from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO


def load_image():
    try:
        response = requests.get(url)
        response.raise_for_status()

window = Tk()
window.title("Cats")
window.geometry("400x600")

label =Label()
label.pack()

url = ("https://catsaas.com/cat")
img = load_image(url)

if img:
    label.config(image=img)
    label.image = img

window.mainloop()
