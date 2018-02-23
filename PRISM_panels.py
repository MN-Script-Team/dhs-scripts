import bzio
import FuncLib

"""Classes of MAXIS Panels"""
"""This script defines classes for all of the panels in MAXIS
Each of the panels will have a gather_data method used to get all of the information listed on the panel.
Calling class_name.gather_data() will create class properties for each of the data elements.
Many of the STAT panels will also have a create_new method to create a new panel."""

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
