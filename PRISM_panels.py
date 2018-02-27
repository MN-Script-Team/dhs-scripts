import bzio
import FuncLib

"""Classes of MAXIS Panels"""
"""This script defines classes for all of the panels in MAXIS
Each of the panels will have a gather_data method used to get all of the information listed on the panel.
Calling class_name.gather_data() will create class properties for each of the data elements.
Many of the STAT panels will also have a create_new method to create a new panel."""


def read_pf1_menu(self, code_length, code_row, code_col, menu_code_col, menu_desc_col):
    panel_code = bzio.ReadScreen(code_length, code_row, code_col)

    if panel_code.rplace("_", "") == "":
        panel_description = ""
        bzio.SetCursor(code_row, code_col)
        bzio.PF1()
        panel_description = ""
        panel_row = 14
        while panel_description == "":
            the_code = bzio.ReadScreen(code_length, panel_row, code_col)
            if the_code == panel_code:
                panel_description = bzio.ReadScreen(30, panel_row, desc_col)
                panel_description = panel_description.strip()
            else:
                panel_row += 1
                if panel_row == 19:
                    bzio.PF8()
                    panel_row = 14
            if the_code == "  ":
                break
        bzio.PF3()
    else:
        panel_description = "Blank"

    return panel_description

class CAFS_panel:
    def __init__(self):
        pass

    def navigate_to(self):
        current_page = bzio.ReadScreen(22, 2, 28)
        if current_page != "Case Financial Summary":
            FuncLib.navigate_to_PRISM_screen("CAFS")

    def gather_data(self):

        self.navigate_to()

        self.monthly_accrual = FuncLib.read_float_from_BZ(9, 9, 30)
        self.monthly_non_accrual = FuncLib.read_float_from_BZ(9, 10, 30)
        self.unpaid_monthly_accrual = FuncLib.read_float_from_BZ(9, 11, 30)
        self.unpaid_mo_non_accrual = FuncLib.read_float_from_BZ(9, 12,30)
        self.past_due = FuncLib.read_float_from_BZ(9,13,30)
        self.total_due = FuncLib.read_float_from_BZ(9, 14, 30)
        self.suspense = FuncLib.read_float_from_BZ(9, 9, 69)
        self.NPA_arrears = FuncLib.read_float_from_BZ(9, 10, 69)
        self.PA_arrears = FuncLib.read_float_from_BZ(9, 11, 69)
        self.total_arrears = FuncLib.read_float_from_BZ(9, 12, 69)
        if bzio.ReadScreen(1, 13, 35) == "Y":
            self.holds = True
        else:
            self.holds = False
        if bzio.ReadScreen(1, 14, 35) == "Y":
            self.offset = True
        else:
            self.offset = False

        self.obligation_info = []
        numb_of_debts = bzio.ReadScreen(2, 15, 71)
        numb_of_debts = numb_of_debts.strip()
        numb_of_debts = int(numb_of_debts)

        debt_type_codes = {"ADF": "Administrative Fund Fee",
                           "AFC": "AFDC/MFIP/MA Obligation",
                           "APF": "Application Fees",
                           "ATF": "Attorney Fees",
                           "CAF": "Case Fee (Non-IV-D)",
                           "CCC": "Child Care",
                           "CHF": "Clearinghouse Fees",
                           "CPI": "CP Tax Intercept Fee",
                           "CRF": "Cost Recovery Fee",
                           "CTF": "Court Ordered Costs",
                           "DPR": "Direct Payment Recovery",
                           "FAF": "Federal Annual Fee",
                           "FCC": "IV-E Foster Care Obligation",
                           "FIF": "Full IRS Fee",
                           "FPL": "Federal Parent Locate Fee",
                           "GTF": "Genetic Testing Fees",
                           "IRA": "IRS Adjustment",
                           "MDN": "Medical Due NCP",
                           "NIF": "Non IV-D Service Fee",
                           "NPA": "Non Public Assistance Obligation",
                           "NSF": "Non Sufficient Fund Fee",
                           "NSR": "NSF/Posting Error Recoupment",
                           "N4D": "Non IV-D Obligation",
                           "OVP": "CP Overpayment",
                           "RED": "Retro Debt",
                           "SEF": "Service Fee (Not Court Order)",
                           "SOP": "Service of Process Fee"}

        obligation_codes = {}

        for debts in range[1:numb_of_debts]:
            bzio.WriteScreen(debts, 15, 57)
            bzio.Transmit()

            nbr = bzio.ReadScreen(2, 17, 2)
            status = bzio.ReadScreen(1, 17, 6)
            if status == "A":
                status = "Active"
            elif status == "I":
                status = "Inactive"
            suppress = bzio.ReadScreen(1, 17, 9)
            if suppress == "Y":
                suppress = "Yes"
            else:
                suppress = "No"
            debt_type = debt_type_codes[bzio.ReadScreen(3, 17, 13)]
            obligation = obligation_codes[bzio.ReadScreen(3, 17, 18)]
            method = bzio.ReadScreen(1, 17, 22)
            accrual = FuncLib.read_float_from_BZ(7, 17, 26)
            mo_oblig = FuncLib.read_float_from_BZ(7, 17, 36)
            begin_date = "%s/%s/%s" % (bzio.ReadScreen(2, 17, 44), bzio.ReadScreen(2, 17, 47), bzio.ReadScreen(2, 17, 50))
            balance = FuncLib.read_float_from_BZ(9, 17, 54)
            court_file = bzio.ReadScreen(16, 17, 64).strip()

            self.obligation_info.append([nbr, status, suppress, debt_type, obligation, ])


class NCDE_panel:
    def __init__(self, mci):
        self.mci = mci

    global race_codes
    race_codes = {"AFA": "African American",
                  "AMI": "American Indian",
                  "ASI": "Asian",
                  "HIS": "Hispanic",
                  "OTH": "Other",
                  "PAC": "Pacific Islander",
                  "WHI": "White",
                  "___": "Blank"}

    global color_codes
    color_codes = {"BRO": "Brown",
                   "DIC": "Dichromatic",
                   "GRA": "Gray",
                   "GRE": "Green",
                   "HAZ": "Hazel",
                   "MIX": "Mixed",
                   "RED": "Red",
                   "SAN": "Sandy",
                   "WHI": "White",
                   "OTH": "Other",
                   "UNK": "Unknown",
                   "___": "Blank"}

    global language_codes
    language_codes = {"01": "Spanish",
                      "02": "Hmong",
                      "03": "Vietnamese",
                      "04": "Cambodian",
                      "05": "Laotian",
                      "06": "Russian",
                      "07": "Somalian",
                      "08": "American Sign Language",
                      "09": "Amharic",
                      "10": "Arabic",
                      "11": "Bosnian",
                      "12": "Oromiffa",
                      "13": "Tigrinya",
                      "14": "Burmese",
                      "15": "Cantonese",
                      "16": "French",
                      "17": "Mandarin",
                      "18": "Swahili",
                      "19": "Yoruba",
                      "20": "Korean",
                      "21": "Karen",
                      "97": "Unknown",
                      "98": "Other",
                      "99": "English",
                      "__": "Blank"}

    global military_branch_codes
    military_branch_codes = {"AIF": "Air Force",
                             "ANG": "Air National Guard",
                             "ARM": "Army",
                             "COG": "Coast Guard",
                             "MAR": "Marines",
                             "NAV": "Navy",
                             "RES": "Reserves",
                             "RNG": "Regular Army National Guard",
                             "___": "None"}

    def find_language(self, row, col):
        panel_code = bzio.ReadScreen(2, row, col)

        if panel_code != "__":
            bzio.SetCursor(row, col)
            bzio.PF1()
            panel_language = ""
            panel_row = 14
            while panel_language == "":
                the_code = bzio.ReadScreen(2, row, 8)
                if the_code == panel_code:
                    panel_language = bzio.ReadScreen(30, row, 13)
                    panel_language = panel_language.strip()
                else:
                    panel_row += 1
                    if panel_row == 19:
                        bzio.PF8()
                        panel_row = 14
                if the_code == "  ":
                    break
            bzio.PF3()
        else:
            panel_language = "Blank"

        return panel_language

    def find_country(self, row, col):
        panel_code = bzio.ReadScreen(2, row, col).replace("_", "")

        if panel_code != "":
            bzio.SetCursor(row, col)
            bzio.PF1()
            bzio.WriteScreen(panel_code, 20, 28)
            bzio.Transmit()
            if bzio.ReadScreen(2, 14, 7) == panel_code:
                panel_country = bzio.ReadScreen(30, 14, 13)
                panel_country = panel_country.strip()
            else:
                panel_country = "Unknown"
            bzio.PF3()
        else:
            panel_country = "Blank"

        return panel_country

    def navigate_to(self):
        current_page = bzio.ReadScreen(16, 2, 31)
        if current_page != "NCP Demographics":
            FuncLib.navigate_to_PRISM_screen("NCDE")

    def gather_data(self):
        self.navigate_to()

        self.ssn = bzio.ReadScreen(11, 6, 7)
        if self.ssn == "   -  -    ":
            self.ssn = ""
        self.dob = bzio.ReadScreen(10, 9, 29).replace("_", "")
        self.gender = bzio.ReadScreen(1, 6, 41)
        if self.gender == "M":
            self.gender = "Male"
        if self.gender == "F":
            self.gender = "Female"
        if self.gender == "U":
            self.gender = "Unknown"
        self.numb_of_cases = bzio.ReadScreen(1, 6, 60)
        self.numb_of_cases = int(self.numb_of_cases)
        self.smi = bzio.ReadScreen(9, 6, 68)
        self.last_name = bzio.ReadScreen(17, 8, 8).replace("_", "")
        self.first_name = bzio.ReadScreen(12, 8, 34).replace("_", "")
        self.middle_name = bzio.ReadScreen(12, 8, 56).replace("_", "")
        self.suffix = bzio.ReadScreen(3, 8, 74).replace("_", "")

        self.race = race_codes[bzio.ReadScreen(3, 9, 19)]
        if bzio.ReadScreen(1, 9, 74) == "Y":
            self.interp_needed = True
        else:
            self.interp_needed = False

        self.language = language_codes[bzio.ReadScreen(2, 9, 55)]
        self.language = self.find_language(9, 55)

        self.home_phone = "(%s)%s-%s" % (bzio.ReadScreen(3, 13, 14), bzio.ReadScreen(3, 13, 18), bzio.ReadScreen(4, 13, 22))
        if self.home_phone == "(___)___-____":
            self.home_phone = ""
        self.cell_phone =  "(%s)%s-%s" % (bzio.ReadScreen(3, 14, 14), bzio.ReadScreen(3, 14, 18), bzio.ReadScreen(4, 14, 22))
        if self.cell_phone == "(___)___-____":
            self.cell_phone = ""
        self.alt_phone =  "(%s)-%s-%s" % (bzio.ReadScreen(3, 13, 40), bzio.ReadScreen(3, 13, 44), bzio.ReadScreen(4, 13, 48))
        if self.alt_phone == "(___)___-____":
            self.alt_phone = ""
        self.alt_phone_ext = bzio.ReadScreen(4, 13, 58).replace("_", "")

        self.city_of_birth = bzio.ReadScreen(20, 15, 12).replace("_", "")
        self.county_of_birth = bzio.ReadScreen(20, 15, 39)
        self.state_of_birth = bzio.ReadScreen(2, 15, 64)
        self.country_of_birth = self.find_country(15, 76)

        self.wgt = bzio.ReadScreen(3, 16, 7).replace("_", "")
        self.hgt = "%s ft. %s in." % (bzio.ReadScreen(1, 16, 24), bzio.ReadScreen(2, 16, 26).replace("_", ""))
        self.eyes = color_codes[bzio.ReadScreen(3, 16, 36)]
        self.hair = color_codes[bzio.ReadScreen(3, 16, 47)]
        if bzio.ReadScreen(1, 16, 69) == "Y":
            self.glasses = True
        elif bzio.ReadScreen(1, 16, 69) == "N":
            self.glasses = False
        else:
            self.glasses = "Unknown"

        if bzio.ReadScreen(1, 16, 78) == "Y":
            self.beard = True
        elif bzio.ReadScreen(1, 16, 78) == "N":
            self.beard = False
        else:
            self.beard = "Unknown"

        self.unique_phys_marks = "%s %s" % (bzio.ReadScreen(60, 17, 19).replace("_", ""), bzio.ReadScreen(60, 18, 19).replace("_", ""))
        self.spec_cond = bzio.ReadScreen(66, 19, 13).replace("_", "")

        bzio.PF11()

        self.tribe = bzio.ReadScreen(25, 8, 12).strip()

        self.mother_last_name = bzio.ReadScreen(17, 10, 24).replace("_", "")
        self.mother_first_name = bzio.ReadScreen(12, 10, 50).replace("_", "")
        self.monther_middle_initial = bzio.ReadScreen(1, 10, 68).replace("_", "")
        self.mother_maiden_name = bzio.ReadScreen(17, 11, 24).replace("_", "")
        self.father_last_name = bzio.ReadScreen(17, 12, 24).replace("_", "")
        self.father_first_name = bzio.ReadScreen(12, 12, 50).replace("_", "")
        self.father_middle_initial = bzio.ReadScreen(1, 12, 68).replace("_", "")
        self.father_suffix = bzio.ReadScreen(3, 12, 76).replace("_", "")

        self.military_branch = military_branch_codes[bzio.ReadScreen(3, 14, 19)]
        self. military_station = bzio.ReadScreen(25, 14, 42).replace("_", "")
        if bzio.ReadScreen(1, 14, 78) == "Y":
            self.veteran = True
        else:
            self.veteran = False

        self.military_begin = bzio.ReadScreen(10, 15, 19).replace("_", "")
        self.military_end = bzio.ReadScreen(10, 15, 48).replace("_", "")
