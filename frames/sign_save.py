import tkinter as tk
from tkinter import ttk
from frames.signature import SignatureCanvas
from tkinter import filedialog
import PIL.ImageGrab as ImageGrab
import datetime as dt


class SignatureFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.controller = controller

        pharmacist_signature = controller.pharmacist_signature

        signature_container = ttk.LabelFrame(self, padding=(10, 10), text="Pharmacist Declaration")
        signature_container.grid(pady=5, row=0, column=0)

        declaration_label = ttk.Label(
            signature_container,
            text="I certify that the patient(s) does(do) not have to pay for this treatment. \nI certify that I am "
                 "named in the Local Enhanced Service (LES) authorisation \nagreement and that I have carried out the "
                 "duties as stated in the LES")
        declaration_label.grid(row=0, column=0, sticky="EW")

        self.patient_signature = SignatureCanvas(self, width='500', height='100', bg='white', thickness=1)
        self.patient_signature.grid(row=1, column=0)

        gphc_label = ttk.Label(
            signature_container,
            text="GpHC Number:"
        )
        gphc_label.grid(row=2, column=0, pady=10)

        gphc_entry = ttk.Entry(
            signature_container,
            textvariable=pharmacist_signature,
            justify="center"
        )
        gphc_entry.grid(row=2, column=1, pady=10)

        self.reset_button = ttk.Button(
            signature_container,
            text="Reset Signature",
            command=self.reset_signature,
            cursor="hand2"
        )
        self.reset_button.grid(row=3, column=1, sticky="E")

        self.save_button = ttk.Button(
            signature_container,
            text="Save Signature",
            command=self.save_signature,
            cursor="hand2"
        )
        self.save_button.grid(row=3, column=2, sticky="E")

    def reset_signature(self):
        # reset canvas to make a new signature
        self.patient_signature.delete("all")

    def save_signature(self):
        # Bring name and date for filename
        pharmacist_name = str(self.controller.pharmacist_signature.get())
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg",
                                            initialfile=str(dt.date.today()) + '-' + pharmacist_name)
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        img = ImageGrab.grab(bbox=(x, y, x + 800, y + 350))
        img.show()
        img.save(filename)
