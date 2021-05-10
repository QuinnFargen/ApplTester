
from selenium.webdriver.common.by import By

class TV_Pg1_Locators(object):
    """
    A class for TV Pg1 Locators
    """
    #Names
    Total_first_name = (By.ID, 'first_name')
    Total_last_name = (By.ID, 'last_name')
    #Emails
    Total_email_address = (By.ID, 'email_address') 
    Total_verify_email_address = (By.ID, 'verify_email_address') 
    #Addr
    Total_address_line_1 = (By.ID, 'address_line_1')
    Total_address_city = (By.ID, 'address_city')
    Total_address_state = (By.ID, 'address_state')
    Total_address_zip = (By.ID, 'address_zip')
    #Phones
    Total_home_phone = (By.ID, 'home_phone')
    Total_mobile_phone = (By.ID, 'mobile_phone')
    #Selects
    Total_has_checking_account = (By.ID, 'has_checking_account')
    Total_Page1_Continue = (By.ID, 'cta_continue')


class TV_Pg2_Locators(object):
    """
    A class for TV Pg2 Locators
    """
    #DOB
    Total_dob_mm = (By.ID, 'dob_mm')
    Total_dob_dd = (By.ID, 'dob_dd')
    Total_dob_yyyy = (By.ID, 'dob_yyyy')
    #SSN
    Total_ssn = (By.ID, 'ssn')
    Total_verify_ssn = (By.ID, 'verify_ssn')
    #Work
    Total_occupation = (By.ID, 'occupation')
    Total_employer_name = (By.ID, 'employer_name')
    Total_employer_phone = (By.ID, 'employer_phone')
    #IncExp
    Total_monthly_income_amount = (By.ID, 'monthly_income_amount')
    Total_monthly_obligation_amount = (By.ID, 'monthly_obligation_amount')
    #Selects
    Total_has_debit_credit_card = (By.ID, 'has_debit_credit_card')
    Total_cash_advance = (By.ID, 'cash_advance')
    Total_additional_card = (By.ID, 'additional_card')
    Total_additional_card_first_name = (By.ID, 'additional_card_first_name')
    Total_additional_card_middle_initial = (By.ID, 'additional_card_middle_initial')
    Total_additional_card_last_name = (By.ID, 'additional_card_last_name')
    Total_Page2_Continue = (By.ID, 'app2_continue')
    

class SearchResultsPageLocators(object):
    """
    A class for search results locators. All search results locators should come here
    """

    pass



