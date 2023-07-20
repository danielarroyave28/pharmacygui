import tkinter as tk
import tkinter.messagebox
from tkinter import ttk
import openpyxl
import os
import pandas as pd
from tkinter import messagebox
from datetime import date, datetime
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError
from dotenv import load_dotenv

load_dotenv()

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]

SPREADSHEET_ID = os.getenv("SPREADSHEET_ID")


class SubmitFrame(ttk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        self.columnconfigure(0, weight=1)
        self.rowconfigure(0, weight=1)

        self.family = controller.family_surname
        self.fam_postcode = controller.family_postcode
        self.phar_sig = controller.pharmacist_signature
        self.declaration_exemption = controller.declaration_exemption
        self.head_lice_samples = controller.head_lice_samples
        self.patients_with_head_lice = controller.patients_with_head_lice
        self.derbac_50 = controller.derbac_50
        self.hedrin_50 = controller.hedrin_50
        self.wet_combing = controller.wet_combing
        self.derbac_200 = controller.derbac_200
        self.hedrin_150 = controller.hedrin_150
        self.initial_counselling = controller.initial_counselling
        self.comb_supplied = controller.comb_supplied

        submit_container = ttk.Frame(self)
        submit_container.grid()
        self.submit = ttk.Button(
            submit_container,
            text="Submit",
            command=self.insert_row,
            cursor="hand2",
            width=20
        )
        self.submit.grid(sticky="WE")

    def insert_row(self):
        full_date = date.today().strftime("%d-%m-%Y")
        year = int(date.today().strftime("%Y"))
        month = date.today().strftime("%B")
        last_name = self.family.get()
        code = self.fam_postcode.get()
        pharmacist = self.phar_sig.get()
        declaration = self.declaration_exemption.get()
        head_samples = self.head_lice_samples.get()
        patients_head_confirmed = self.patients_with_head_lice.get()
        derbac_50 = self.derbac_50.get()
        hedrin_50 = self.hedrin_50.get()
        wet_combing = self.wet_combing.get()
        derbac_200 = self.derbac_200.get()
        hedrin_150 = self.hedrin_150.get()
        initial_counseling = self.initial_counselling.get()
        comb_supplied = self.comb_supplied.get()

        current_path = os.getcwd()
        final_path = os.path.join(current_path, "data.xlsx")

        # current_path = "C:/Users/arro2/Documents/data.xlsx"

        if last_name and code and pharmacist and initial_counseling and comb_supplied and declaration:

            if not os.path.exists(final_path):
                workbook = openpyxl.Workbook()
                sheet = workbook.active
                heading = ["date", "year", "month", "family_Surname", "family_code", "pharmacist_gphc",
                           "exemption_reason",
                           "head_lice_samples",
                           "patients_with_head_lice", "derbac_50_ml", "hedrin_50_ml", "wet_combing",
                           "derbac_200_ml", "hedrin_150_ml", "initial_counselling", "comb_supplied"]
                sheet.append(heading)
                workbook.save(final_path)

            else:
                try:
                    workbook = openpyxl.load_workbook(final_path)
                    sheet = workbook.active
                    sheet.append(
                        [full_date, year, month, last_name, code, pharmacist, declaration, head_samples,
                         patients_head_confirmed, derbac_50,
                         hedrin_50, wet_combing, derbac_200, hedrin_150, initial_counseling, comb_supplied])
                    workbook.save(final_path)
                    self.create_dfs(final_path)
                    self.update_google_sheet()
                    tkinter.messagebox.showinfo(title="Submitted!", message="Data entry succesful!")

                except Exception as e:
                    tkinter.messagebox.showwarning(title="Error", message=str(e))

                finally:
                    pass
        else:
            tkinter.messagebox.showwarning(title="error", message="Data required, check if something is missing!")

    def create_dfs(self, path):
        df = pd.read_excel(io=path)
        for year in df['year'].unique():
            for month in df['month'].unique():
                data = df[(df['month'] == month) & (df['year'] == year)]
                data.to_excel(str(year) + '-' + str(month) + '.xlsx', index=False)

    def update_google_sheet(self):
        # check current month

        current_month = datetime.now().strftime("%B")
        current_month_year = datetime.now().strftime("%Y-%B")
        current_year = int(datetime.now().strftime("%Y"))
        print(type(current_month))



        # load data
        df = pd.read_excel('data.xlsx')
        data = df[(df['year'] == current_year) & (df['month'] == current_month)]
        print(data)

        # Total number of initial consultarions
        # filter_list = ('Yes, no medicine given', 'No, no medicine given', 'Yes, medicine given',
        #                                      'No, but medicine given')

        filter_list = ['Yes, no medicine given', 'Yes, medicine given']

        total_consultations = len(data[data['initial_counselling'].isin(filter_list)])

        # Number of heads treating in month that medicine supplied to

        filter_list2 = ['No, but medicine given', 'Yes, medicine given']
        total_medicine_given = len(data[data['initial_counselling'].isin(filter_list2)])

        # Numer of people for whom just web combing is recommended

        filter_list3 = ['Yes, comb supplied']
        total_web_combing = len(data[data['comb_supplied'].isin(filter_list3)])

        derbac_50 = float(data['derbac_50_ml'].sum())
        hedrin_50 = float(data['hedrin_50_ml'].sum())
        hedrin_150 = float(data['hedrin_150_ml'].sum())
        derbac_200 = float(data['derbac_200_ml'].sum())

        credentials = None
        if os.path.exists("token.json"):
            credentials = Credentials.from_authorized_user_file("token.json", SCOPES)
        if not credentials or not credentials.valid:
            if credentials and credentials.expired and credentials.refresh_token:
                credentials.refresh(Request())
            else:
                flow = InstalledAppFlow.from_client_secrets_file("credentials.json", SCOPES)
                credentials = flow.run_local_server(port=0)
            with open("token.json", "w") as token:
                token.write(credentials.to_json())

        try:
            service = build("sheets", "v4", credentials=credentials)
            sheets = service.spreadsheets()
            # sheet_metadata = sheets.get(spreadsheetID=SPREADSHEET_ID).execute()
            # list_sheets = sheet_metadata.get('sheets', '')
            #
            # list = []
            # for sheet in list_sheets:
            #     title = sheets[0].get("properties", {}).get("title", f'{sheet}')
            #     if title == current_month:
            #         #update sheet values

            batch_update_values_request_body = {
                "valueInputOption": "RAW",
                "data": [
                    {
                        'range': f'{current_month_year}!B5',
                        'values': [[total_consultations]]
                    },
                    {
                        'range': f'{current_month_year}!B6',
                        'values': [[total_medicine_given]]
                    },
                    {
                        'range': f'{current_month_year}!B7',
                        'values': [[total_web_combing]]
                    },

                    {
                        'range': f'{current_month_year}!B10',
                        'values': [[hedrin_50]]
                    },

                    {
                        'range': f'{current_month_year}!B11',
                        'values': [[hedrin_150]]
                    },

                    {
                        'range': f'{current_month_year}!B12',
                        'values': [[derbac_50]]
                    },

                    {
                        'range': f'{current_month_year}!B13',
                        'values': [[derbac_200]]
                    },

                ]
            }

            sheets.values().batchUpdate(
                spreadsheetId=SPREADSHEET_ID,
                body=batch_update_values_request_body
            ).execute()

        except HttpError as e:
            DISCOVERY_SERVICE_URL = 'https://sheets.googleapis.com/$discovery/rest?version=v4'
            service = build('sheets', 'v4', credentials=credentials, discoveryServiceUrl=DISCOVERY_SERVICE_URL)
            print(e)
