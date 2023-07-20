import tkinter as tk
from tkinter import ttk


class DeclarationFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(1, weight=1)
        self.columnconfigure(1, weight=1)

        # StringVar for user input
        #self.declaration_exemption = tk.StringVar()

        declaration_exemption = controller.declaration_exemption

        declaration_container = ttk.LabelFrame(self,text="Declaration of Exemption")
        declaration_container.grid(pady=5,row=0, column=0)

        # declaration_label = ttk.Label(
        #     declaration_container,
        #     text="Declaration of Exemption",
        #     justify="center"
        # )
        # declaration_label.grid(row=0, column=1, sticky="EW", padx=100, pady=20)

        option_one_label = ttk.Label(
            declaration_container,
            text='A'
        )
        option_one_label.grid(row=1, column=0, sticky="EW")

        option_two_label = ttk.Label(
            declaration_container,
            text='B'
        )
        option_two_label.grid(row=2, column=0, sticky="EW")

        option_three_label = ttk.Label(
            declaration_container,
            text='C'
        )
        option_three_label.grid(row=3, column=0, sticky="EW")

        option_four_label = ttk.Label(
            declaration_container,
            text='D'
        )
        option_four_label.grid(row=4, column=0, sticky="EW")

        option_five_label = ttk.Label(
            declaration_container,
            text='F'
        )
        option_five_label.grid(row=5, column=0, sticky="EW")

        option_six_label = ttk.Label(
            declaration_container,
            text='G'
        )
        option_six_label.grid(row=6, column=0, sticky="EW")

        option_seven_label = ttk.Label(
            declaration_container,
            text='H'
        )
        option_seven_label.grid(row=7, column=0, sticky="EW")

        option_eight_label = ttk.Label(
            declaration_container,
            text='K'
        )
        option_eight_label.grid(row=8, column=0, sticky="EW")

        option_nine_label = ttk.Label(
            declaration_container,
            text='L'
        )
        option_nine_label.grid(row=9, column=0, sticky="EW")

        option_ten_label = ttk.Label(
            declaration_container,
            text='M'
        )
        option_ten_label.grid(row=10, column=0, sticky="EW")

        option_eleven_label = ttk.Label(
            declaration_container,
            text='N'
        )
        option_eleven_label.grid(row=11, column=0, sticky="EW")

        option_twelve_label = ttk.Label(
            declaration_container,
            text='S'
        )
        option_twelve_label.grid(row=12, column=0, sticky="EW")

        option_thirteen_label = ttk.Label(
            declaration_container,
            text='T'
        )
        option_thirteen_label.grid(row=13, column=0, sticky="EW")


        ############################ values button #############################
        option_one = ttk.Radiobutton(
            declaration_container,
            text='Is under 16 years of age',
            variable=declaration_exemption,
            value="s under 16 years of age"

        )
        option_one.grid(row=1, column=1, sticky="EW")

        option_two = ttk.Radiobutton(
            declaration_container,
            text='Is 16, 17 or 18 and in full time education',
            variable=declaration_exemption,
            value="Is 16, 17 or 18 and in full time education"

        )
        option_two.grid(row=2, column=1, sticky="EW")

        option_three = ttk.Radiobutton(
            declaration_container,
            text='Is 60 years of age or over',
            variable=declaration_exemption,
            value="Is 60 years of age or over"

        )
        option_three.grid(row=3, column=1, sticky="EW")

        option_four = ttk.Radiobutton(
            declaration_container,
            text='Has a valid maternity exemption certificate',
            variable=declaration_exemption,
            value="Has a valid maternity exemption certificate"

        )
        option_four.grid(row=4, column=1, sticky="EW")

        option_five = ttk.Radiobutton(
            declaration_container,
            text='Has a valid medical exemption certificate',
            variable=declaration_exemption,
            value="Has a valid medical exemption certificate"

        )
        option_five.grid(row=5, column=1, sticky="EW")

        option_six = ttk.Radiobutton(
            declaration_container,
            text='Has a valid prescription pre-payment plan',
            variable=declaration_exemption,
            value="Has a valid prescription pre-payment plan"

        )
        option_six.grid(row=6, column=1, sticky="EW")

        option_seven = ttk.Radiobutton(
            declaration_container,
            text='Has a valid War Pension exemption certificate',
            variable=declaration_exemption,
            value="Has a valid War Pension exemption certificate"

        )
        option_seven.grid(row=7, column=1, sticky="EW")

        option_eight = ttk.Radiobutton(
            declaration_container,
            text='Gets Income Support or income-related Employment and Support Allowance',
            variable=declaration_exemption,
            value="Gets Income Support or income-related Employment and Support Allowance"

        )
        option_eight.grid(row=8, column=1, sticky="EW")

        option_nine = ttk.Radiobutton(
            declaration_container,
            text='Gets income based Jobseeker’s Allowance',
            variable=declaration_exemption,
            value="Gets income based Jobseeker’s Allowance"

        )
        option_nine.grid(row=8, column=1, sticky="EW")

        option_ten = ttk.Radiobutton(
            declaration_container,
            text='Is named on a current HC2 charges certificate',
            variable=declaration_exemption,
            value="Is named on a current HC2 charges certificate"

        )
        option_ten.grid(row=9, column=1, sticky="EW")

        option_eleven = ttk.Radiobutton(
            declaration_container,
            text='Is entitled to, or named on, a valid NHS Tax Credit Exemption Certificate',
            variable=declaration_exemption,
            value="Is entitled to, or named on, a valid NHS Tax Credit Exemption Certificate"

        )
        option_eleven.grid(row=10, column=1, sticky="EW")

        option_twelve = ttk.Radiobutton(
            declaration_container,
            text='Has paid the current FP10 charge',
            variable=declaration_exemption,
            value="Has paid the current FP10 charge"

        )
        option_twelve.grid(row=11, column=1, sticky="EW")

        option_thirteen = ttk.Radiobutton(
            declaration_container,
            text='Has a partner who gets Pension Credit Guarantee Credit (PCGC)',
            variable=declaration_exemption,
            value="Has a partner who gets Pension Credit Guarantee Credit (PCGC)"

        )
        option_thirteen.grid(row=12, column=1, sticky="EW")

        option_thirteen = ttk.Radiobutton(
            declaration_container,
            text='Has a partner who gets Pension Credit Guarantee Credit (PCGC)',
            variable=declaration_exemption,
            value="Has a partner who gets Pension Credit Guarantee Credit (PCGC)"

        )
        option_thirteen.grid(row=12, column=1, sticky="EW")

        option_fourteen = ttk.Radiobutton(
            declaration_container,
            text='Has to pay, no valid exemption applies',
            variable=declaration_exemption,
            value="Has to pay, no valid exemption applies",

        )
        option_fourteen.grid(row=13, column=1, sticky="EW")

