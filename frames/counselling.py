import tkinter as tk
from tkinter import ttk


class CounsellingFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self["style"] = "Background.TFrame"

        self.columnconfigure(0, weight=1)
        self.rowconfigure(2, weight=1)

        self.controller = controller

        #String vars for user inputs
        # self.initial_counselling = tk.StringVar()
        # self.comb_supplied = tk.StringVar()

        initial_counselling = controller.initial_counselling
        comb_supplied = controller.comb_supplied

        counselling_container = ttk.LabelFrame(self, padding=10, text='Initial Counselling')
        counselling_container.grid(row=0, column=0)

        # counselling_container = ttk.Frame(self, padding=10)
        # counselling_container.grid()

        initial_counselling_label = ttk.Label(counselling_container, text="Initial Counselling & Advice Given:")
        initial_counselling_label.grid()
        initial_counselling_input = ttk.Combobox(counselling_container, textvariable=initial_counselling)
        initial_counselling_input["values"] = ('Yes, no medicine given', 'No, no medicine given','Yes, medicine given',
                                               'No, but medicine given')
        initial_counselling_input.grid(pady=10, sticky="EW")

        comb_supplied_label = ttk.Label(counselling_container, text="Head lice Comb Supplied:")
        comb_supplied_label.grid()
        comb_supplied_input = ttk.Combobox(counselling_container, textvariable=comb_supplied)
        comb_supplied_input["values"] = ('Yes, comb supplied', 'No')
        comb_supplied_input.grid(pady=10, sticky="EW")



