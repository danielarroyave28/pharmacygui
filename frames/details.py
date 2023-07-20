import tkinter as tk
from tkinter import ttk
import datetime as dt


class SettingsFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        #self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.date = dt.datetime.now()

        self.controller = controller
        family_surname = controller.family_surname
        family_postcode = controller.family_postcode
        codes = controller.codes

        # String vars for user inputs


        # self.family_surname = tk.StringVar()
        # self.family_postcode = tk.StringVar()
        # self.codes = ("FR039", "None")

        settings_container = ttk.LabelFrame(self, padding=(10,10), text="Details")
        settings_container.grid(pady=5, row=0, column=0)

        date_label = ttk.Label(
            settings_container,
            text=f"{self.date:%A, %B %d, %Y}",
            justify="left"

        )
        date_label.grid(row=0, column=0, pady=5, columnspan=2, sticky="EW")

        family_surname_label = ttk.Label(settings_container, text="Family Surname:")
        family_surname_label.grid(row=1, column=0, sticky="EW")
        family_surname_input = ttk.Entry(settings_container, width=15, textvariable=family_surname,
                                         justify='center')
        family_surname_input.grid(row=1, column=1, pady=10, sticky="EW")
        family_surname_input.focus()

        family_code_label = ttk.Label(settings_container, text="Family Postcode:")
        family_code_label.grid(row=0, column=2, pady=10, sticky="EW")
        family_code_input = ttk.Entry(settings_container, width=10, textvariable=family_postcode, justify='center')
        family_code_input.grid(row=0, column=3,pady=10,padx=10, sticky="EW")

        pharmacy_code_label = ttk.Label(settings_container, text="Pharmacy Code:")
        pharmacy_code_label.grid(row=1, column=2, pady=10, padx=10, sticky="EW")

        codes = tk.StringVar(value=codes)
        pharmacy_code_input = tk.Listbox(settings_container,width=5, listvariable=codes, height=2, justify="center")
        pharmacy_code_input.grid(row=1, column=3, pady=10, sticky="EW")
