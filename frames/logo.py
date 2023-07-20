import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk
import os

class LogoFrame(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        logo_container = ttk.Frame(self, padding=10)
        logo_container.grid()

        current_path = os.getcwd()
        final_path = os.path.join(current_path, "logo.jpg")
        self.logo_img = Image.open(final_path)

        #self.logo_img = Image.open("/Users/arro2/PycharmProjects/parkviewgui/logo.jpg")
        #self.logo_img = Image.open("/Users/fatis/Desktop/app/logo.jpg")

        self.logo_img_resized = self.logo_img.resize((135,135))
        self.logo_photo = ImageTk.PhotoImage(self.logo_img_resized)

        img_label = ttk.Label(
            logo_container,
            image=self.logo_photo
        )
        img_label.image = self.logo_photo
        img_label.grid(sticky="NESW",padx=50)
