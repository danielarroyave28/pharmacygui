import tkinter as tk
from tkinter import ttk


class SupplyFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)

        self.controller = controller

        #IntVars
        # self.head_lice_samples = tk.IntVar()
        # self.patients_with_head_lice = tk.IntVar()
        # self.derbac_50 = tk.IntVar()
        # self.hedrin_50 = tk.IntVar()
        # self.wet_combing = tk.IntVar()
        # self.derbac_200 = tk.IntVar()
        # self.hedrin_150 = tk.IntVar()

        head_lice_samples = controller.head_lice_samples
        patients_with_head_lice = controller.patients_with_head_lice
        derbac_50 = controller.derbac_50
        hedrin_50 = controller.hedrin_50
        wet_combing = controller.wet_combing
        derbac_200 = controller.derbac_200
        hedrin_150 = controller.hedrin_150



        supply_container = ttk.LabelFrame(self, padding=10, text="Supply of Treatment")
        supply_container.grid(pady=5, padx=20, row=0, column=0)

        #Labels and Entries
        head_lice_label = ttk.Label(supply_container, text='Total number of head lice samples reviewed:')
        head_lice_label.grid(row=0, column=0, sticky="NEW")
        head_lice_entry = ttk.Entry(supply_container,width=5, textvariable=head_lice_samples, justify='center')
        head_lice_entry.grid(row=0, column=1, sticky="NEW")

        patient_with_head_lice_label = ttk.Label(supply_container, text='Number of patients with confirmed head lice:')
        patient_with_head_lice_label.grid(row=1, column=0, sticky="NEW")
        patient_with_head_lice_entry = ttk.Entry(supply_container, width=5, textvariable=patients_with_head_lice, justify='center')
        patient_with_head_lice_entry.grid(row=1, column=1, sticky="NEW")

        derbac50_label = ttk.Label(supply_container, text='Derbac M Liquid 50ml:')
        derbac50_label.grid(row=0, column=2, sticky="NEW", padx=10)
        derbac50_entry = ttk.Entry(supply_container, width=5, textvariable=derbac_50, justify='center')
        derbac50_entry.grid(row=0, column=3, sticky="NEW")

        derbac200_label = ttk.Label(supply_container, text='Derbac M Liquid 200ml:')
        derbac200_label.grid(row=1, column=2, sticky="NEW", padx=10)
        derbac200_entry = ttk.Entry(supply_container, width=5, textvariable=derbac_200, justify='center')
        derbac200_entry.grid(row=1, column=3, sticky="NEW")

        hedrin50_label = ttk.Label(supply_container, text='Hedrin Lotion 50ml:')
        hedrin50_label.grid(row=2, column=2, sticky="NEW", padx=10)
        hedrin50_entry = ttk.Entry(supply_container, width=5, textvariable=hedrin_50, justify='center')
        hedrin50_entry.grid(row=2, column=3, sticky="NEW")

        hedrin150_label = ttk.Label(supply_container, text='Hedrin Lotion 150ml:')
        hedrin150_label.grid(row=3, column=2, sticky="NEW", padx=10)
        hedrin150_entry = ttk.Entry(supply_container, width=5, textvariable=hedrin_150, justify='center')
        hedrin150_entry.grid(row=3, column=3, sticky="NEW")

        wetcombing_label = ttk.Label(supply_container, text='Wet combing method:')
        wetcombing_label.grid(row=4, column=2, sticky="NEW", padx=10)
        wetcombing_entry = ttk.Entry(supply_container, width=5, textvariable=wet_combing, justify='center')
        wetcombing_entry.grid(row=4, column=3, sticky="NEW")


