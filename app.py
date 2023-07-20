import tkinter as tk
from tkinter import ttk
from frames import SettingsFrame, CounsellingFrame, LogoFrame, SupplyFrame, DeclarationFrame, SignatureFrame, \
    SignatureFrame2, SubmitFrame
from windows import set_dpi_awareness

set_dpi_awareness()

COLOUR_PRIMARY = "#2e3f4f"
COLOUR_SECONDARY = "#293846"
COLOUR_LIGHT_BACKGROUND = "#fff"
COLOUR_LIGHT_TEXT = "#eee"
COLOUR_DARK_TEXT = "#8095a8"


class EntryForm(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        style = ttk.Style()
        style.theme_use("clam")

        style.configure("Background.TFrame", background=COLOUR_PRIMARY)

        self.geometry("1920x1080")
        self.title("HEAD LICE SERVICE CONSULTATION FORM")
        # self.columnconfigure(0, weight=1)
        # self.rowconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        # controller variables to use within different containers

        self.family_surname = tk.StringVar()
        self.family_postcode = tk.StringVar()
        self.codes = ("FR039", "None")

        self.pharmacist_signature = tk.StringVar()

        self.declaration_exemption = tk.StringVar()

        self.head_lice_samples = tk.IntVar()
        self.patients_with_head_lice = tk.IntVar()
        self.derbac_50 = tk.IntVar()
        self.hedrin_50 = tk.IntVar()
        self.wet_combing = tk.IntVar()
        self.derbac_200 = tk.IntVar()
        self.hedrin_150 = tk.IntVar()

        self.initial_counselling = tk.StringVar()
        self.comb_supplied = tk.StringVar()

        container = ttk.Frame(self)
        container.grid()
        container.columnconfigure(0, weight=1)

        details_frame = SettingsFrame(container, self)
        details_frame.grid(row=0, column=0)

        counselling_frame = CounsellingFrame(container, self)
        counselling_frame.grid(row=0, column=1)

        logo_frame = LogoFrame(container)
        logo_frame.grid(row=0, column=2)

        supply_frame = SupplyFrame(container, self)
        supply_frame.grid(row=1, column=0)

        declaration_frame = DeclarationFrame(container, self)
        declaration_frame.grid(row=1, column=1)

        signature_frame = SignatureFrame(container, self)
        signature_frame.grid(row=2, column=0)

        signature_frame2 = SignatureFrame2(container)
        signature_frame2.grid(row=2, column=1)

        submit_frame = SubmitFrame(container, self)
        submit_frame.grid(row=2, column=2)


try:

    app = EntryForm()
    app.mainloop()

except:
    import traceback

    traceback.print_exc()
    input("press enter to end...")
