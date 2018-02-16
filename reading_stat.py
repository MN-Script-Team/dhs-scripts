"""Testing Script for these classes"""

import bzio
import wx
import wx.xrc
import FuncLib
import MAXIS_panels
# Importing these modules is critical
# the bzio, FuncLib, and MAXIS_panels are modules based off of scripts in the same directory.
# MAXIS_panels is the module with all the code to read and create panels in MAXIS.

""" The intention here is that we can save on lines of code and have cleaner code if our functionality is in classes with properties and methods.
This way we do not have to code reading pannels into seperate scripts - it can happen just by calling a class and its method.
This also makes any MAXIS changes easier to resolve as we only have to change coordinates in one place."""

bzio.Connect("")
bzio.Focus()

# QUESTION Can we make this global to modules so we don't have to pass it through as a parameter?
global MAXIS_case_number

# defining case number and footer month and year
# I ran this on a training case as it DOES UPDATE Panels
# the training case has ADDR, ABPS, and 1 ACCT panel for MEMB 01
MAXIS_case_number = FuncLib.MAXIS_case_number_finder()
MAXIS_case_number = str(MAXIS_case_number)
footer_mo_yr = FuncLib.MAXIS_footer_finder()
MAXIS_footer_month = footer_mo_yr[0]
MAXIS_footer_year = footer_mo_yr[1]

# creates an object and sets that to an ADDR Panel class
ADDR = MAXIS_panels.STAT_ADDR_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year)
ADDR.gather_data()      # using the method of the ADDR Panel class to get all information from the panel

# creates an object and sets it to an ABPS Panel class
# this class needs an instance parameter
# ABPS_01 = MAXIS_panels.STAT_ABPS_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01")
# ABPS_01.gather_data()   # using the method from ABPS to get all information - this LOOKs like the same method as above but it is specific to this panel

# creates an oject and sets it to the ACCT Panel class
# this class requires member and instance parameter
# ACCT_01_01 = MAXIS_panels.STAT_ACCT_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01", "01")
# ACCT_01_01.gather_data()  # getting all information from ACCT 01 01 panel

# creating an object and setting it to ACCT Panel class - this is the same class as above BUT a different object with different property assignments
# note that this panel does not exist yet - but the object is defined in the script
# ACCT_01_02 = MAXIS_panels.STAT_ACCT_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01", "02")
# ACCT_01_02.create_new("SV", "434", "6", "12/30/2017", "", "Wells Fargo")    # using method defined in the class to create a brand new panel

# ACUT_01 = MAXIS_panels.STAT_ACUT_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01")
# ACUT_01.create_new(False, ["Y", 300, "Y", 300], [], [], [], ["Y", 15, "Y", 15], ["Y", 30, "Y", 30], [], [], True)

# ALIA_01 = MAXIS_panels.STAT_ALIA_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01")
# ALIA_01.gather_data()

# ALIA_02 = MAXIS_panels.STAT_ALIA_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "02")
# ALIA_02.add_alias_name("Larson", "Benjamin", "H")

# ALTP = MAXIS_panels.STAT_ALTP_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year)
# ALTP.change_payee("1", "02/01/2018", "D Ross", "123 Main St", "Minneapolis", "MN", "55440")
# ALTP.gather_data()
# ALTP.end_payee("09/30/2018")

# AREP = MAXIS_panels.STAT_AREP_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year)
# AREP.update_fs_alt_rep("", "", "", "", "")
# AREP.update_auth_rep("Rachel", "980 St Clair Ave", "Saint Paul", "MN", "55111")

# BILS = MAXIS_panels.STAT_BILS_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year)
# BILS.add_bill("01", "6/1/16", "09", 500, 350, "01", "M")
# BILS.add_bill("01", "5/1/16", "09", 900, 0, "01", "M")
# BILS.add_bill("01", "4/1/16", "09", 400, 50, "01", "M")
# BILS.add_bill("01", "3/1/16", "09", 500, 350, "01", "M")
# BILS.add_bill("01", "2/1/16", "09", 400, 50, "01", "M")
# BILS.add_bill("01", "1/1/16", "09", 500, 350, "01", "M")
# BILS.gather_data()

# BUDG = MAXIS_panels.STAT_BUDG_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year)
# BUDG.change_budget("03/18")

# BUSI_02_01 = MAXIS_panels.STAT_BUSI_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "02", "01")
# BUSI_02_01.create_new("07/15/17", "04", "cash", 800, "1", 150, "1", 120, "01", "02/06/18", 800, 150, 120)

# CARS_01_01 = MAXIS_panels.STAT_CARS_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01", "01")
# CARS_01_01.gather_data()
# CARS_01_01.update_verif("1")
# CARS_01_01.update_value(2300, "1")
#
# CARS_01_new = MAXIS_panels.STAT_CARS_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01", "02")
# CARS_01_new.create_new("2", 2015, "Ford", "Astro", 4775, "1", "4", "N")
# CARS_01_new.update_amount_owed(2025, "01/25/18", "1")

# CASH_01 = MAXIS_panels.STAT_CASH_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01")
# CASH_01.update_cash(300)
# CASH_02 = MAXIS_panels.STAT_CASH_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "02")
# CASH_02.gather_data()

COEX_01 = MAXIS_panels.STAT_COEX_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "01")
COEX_01.update_expense("Support", 2, 350, 350)

COEX_02 = MAXIS_panels.STAT_COEX_panel(MAXIS_case_number, MAXIS_footer_month, MAXIS_footer_year, "02")
COEX_02.update_expense("Alimony", 1, 450, 450)

# this outputs the code from above so we can see it worked.
print(ADDR.case)
print(ADDR.resi1)
print(ADDR.resi_city)
print(ADDR.resi_verif)
print(ADDR.phone_list)
print(ADDR.effective_date)

# print("Absent parent is %s and is the parent of %s" % (ABPS_01.full_name, ABPS_01.children))
# print("")
# print("Account is at " + ACCT_01_01.location)
# print("Account number: " + ACCT_01_01.number)
# print("Balance is " + ACCT_01_01.balance)
# print("Verification is " + ACCT_01_01.balance_verif)
# print("New account instance: " + ACCT_01_02.instance)

# print("The known aliases for Member 01 are:")
# for key in ALIA_01.alias_names:
#    print(ALIA_01.alias_names[key])

# print("The known SSNs for Member 01 are:")
# for key in ALIA_01.secondary_ssns:
#    print(ALIA_01.secondary_ssns[key])

# print("The known aliases for Member 02 are:")
# for key in ALIA_02.alias_names:
#    print(ALIA_02.alias_names[key])

# print("The alternate payee for this case is:")
# print("Reason for alt payee is: %s" % (ALTP.reason))
# print("Name of alt payee is %s" % (ALTP.name))
# print("Address is: %s \n %s, %s %s" % (ALTP.street, ALTP.city, ALTP.state, ALTP.zip))
# print("Phone is: %s" % (ALTP.phone))
# print("Alt Payee is to start %s and end %s" % (ALTP.start_date, ALTP.end_date))
# if AREP.AREP_exists:
#    print("AREP is as follows --")
#    print("Name is: %s" % (AREP.name))
#    print("AREP is disqualified - %s" % (AREP.disq))
#    print("Address is: %s \n %s. %s %s" % (AREP.street, AREP.city, AREP.state, AREP.zip))
#    print("Phone: %s" % (AREP.phone_one))
#    print("Phone: %s" % (AREP.phone_two))

# if AREP.FS_alt_rep_exists:
#    print("ALT REP is as follows --")
#    print("Name is: %s" % (AREP.FS_alt_rep_name))
#    print("AREP is disqualified - %s" % (AREP.FS_alt_rep_disq))
#    print("Address is: %s \n %s. %s %s" % (AREP.FS_alt_rep_street, AREP.FS_alt_rep_city, AREP.FS_alt_rep_state, AREP.FS_alt_rep_zip))
#    print("Phone: %s" % (AREP.FS_alt_rep_phone_one))
#    print("Phone: %s" % (AREP.FS_alt_rep_phone_two))

# if BILS.bills_exist is True:
#    for bill in BILS.all_bills:
#        print(bill)

# print("Budget is currently: %s-%s - source: %s" % (BUDG.current_budg_start, BUDG.current_budg_end, BUDG.current_budg_src))
# print("HC Application date is %s" % (BUDG.hc_app_date))
# print(BUDG.past_budgets)

# print("Self Employment -- for MEMB %s" % (BUSI_02_01.member))
# print("Type of income - %s" % (BUSI_02_01.business_type))
# print("NET: $%s, GROSS: $%s, EXPENSE: $%s for CASH" % (BUSI_02_01.cash_prosp_net, BUSI_02_01.cash_prosp_gross, BUSI_02_01.cash_prosp_exp))
# print("Verified by: %s" % (BUSI_02_01.cash_inc_verif))
# print("Method used: %s established on %s" % (BUSI_02_01.self_emp_method, BUSI_02_01.method_date))

# print("Vehicle 1")
# print("%s - %s %s %s" % (CARS_01_01.type, CARS_01_01.year, CARS_01_01.make, CARS_01_01.model))
# print("Trade-In: %s - Loan: %s - Source: %s" % (CARS_01_01.trade_in_value, CARS_01_01.loan_value, CARS_01_01.value_source))
# print("Use: %s" % (CARS_01_01.use))
#
# print("Vehicle 2")
# print("%s - %s %s %s" % (CARS_01_new.type, CARS_01_new.year, CARS_01_new.make, CARS_01_new.model))
# print("Trade-In: %s - Loan: %s - Source: %s" % (CARS_01_new.trade_in_value, CARS_01_new.loan_value, CARS_01_new.value_source))
# print("Use: %s" % (CARS_01_new.use))

# print("Member %s has $%s in cash" % (CASH_01.member, CASH_01.amount))
# print("Member %s has $%s in cash" % (CASH_02.member, CASH_02.amount))

print("Member %s has Court Ordered Expenses of:" % (COEX_01.member))
print("Support - $%s: Verif: %s, HC Estimate: $%s" % (COEX_01.support_prosp, COEX_01.support_verif, COEX_01.support_hc_est))
print("Alimony - $%s: Verif: %s, HC Estimate: $%s" % (COEX_01.alimony_prosp, COEX_01.alimony_verif, COEX_01.alimony_hc_est))
print("Tax Dep - $%s: Verif: %s, HC Estimate: $%s" % (COEX_01.tax_dep_prosp, COEX_01.tax_dep_verif, COEX_01.tax_dep_hc_est))
print("Other - $%s: Verif: %s, HC Estimate: $%s" % (COEX_01.other_prosp, COEX_01.other_verif, COEX_01.other_hc_est))

print("Member %s has Court Ordered Expenses of:" % (COEX_02.member))
print("Support - $%s: Verif: %s, HC Estimate: $%s" % (COEX_02.support_prosp, COEX_02.support_verif, COEX_02.support_hc_est))
print("Alimony - $%s: Verif: %s, HC Estimate: $%s" % (COEX_02.alimony_prosp, COEX_02.alimony_verif, COEX_02.alimony_hc_est))
print("Tax Dep - $%s: Verif: %s, HC Estimate: $%s" % (COEX_02.tax_dep_prosp, COEX_02.tax_dep_verif, COEX_02.tax_dep_hc_est))
print("Other - $%s: Verif: %s, HC Estimate: $%s" % (COEX_02.other_prosp, COEX_02.other_verif, COEX_02.other_hc_est))
