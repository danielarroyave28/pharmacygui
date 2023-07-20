import tkinter as tk
from tkinter import ttk
from frames.signature import SignatureCanvas
from tkinter import filedialog
import PIL.ImageGrab as ImageGrab
import datetime as dt
class SignatureFrame2(ttk.Frame):
    def __init__(self, parent):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        signature_container2 = ttk.LabelFrame(self, padding=(10, 10), text="Patient Declaration")
        signature_container2.grid(pady=5, row=0, column=0)

        declaration_label = ttk.Label(
            signature_container2,
            text="Where appropriate, I have received information about head lice infection, detection combing and "
                 "\nhow to access the Community Pharmacy Head Lice Service. \n\nExemption declaration. I declare that "
                 "the information I have given on this form is correct and complete \nand I understand that if it is "
                 "not, appropriate action may be taken. I confirm proper entitlement to exemption.")
        declaration_label.grid(row=0, column=0, sticky="EW")

        self.patient_signature = SignatureCanvas(self, width='500', height='100', bg='white', thickness=1)
        self.patient_signature.grid(row=1, column=0, pady=20)

        self.reset_button = ttk.Button(
            signature_container2,
            text="Reset Signature",
            command=self.reset_signature,
            cursor="hand2"
        )
        self.reset_button.grid(row=3, column=0, sticky="E")

        self.save_button = ttk.Button(
            signature_container2,
            text="Save Signature",
            command=self.save_signature,
            cursor="hand2"
        )
        self.save_button.grid(row=3, column=1, sticky="E")

    def reset_signature(self):
        self.patient_signature.delete("all")
        pass

    def save_signature(self):
        # Bring name and date for filename
        filename = filedialog.asksaveasfile(mode='w', defaultextension=".jpg",
                                            initialfile=str(dt.date.today()))
        x = self.winfo_rootx()
        y = self.winfo_rooty()
        img = ImageGrab.grab(bbox=(x, y, x + 850, y + 350))
        img.show()
        img.save(filename)
