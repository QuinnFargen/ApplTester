
from ScreenShotter import TakeScreenShot
from SampleData import SampleInserts
from Storage import setdirectory, maketempfolder, renametempfolder
import os

# Get Data to insert
inserts = SampleInserts()

def Total_Page1(driver):
    # TakePic
    TakeScreenShot(driver, 'Pg1_Begin')
    # Name
    driver.find_element_by_id("first_name").send_keys(inserts["TotalVisa"]["first_name"])
    driver.find_element_by_id("last_name").send_keys(inserts["TotalVisa"]["last_name"])
    # Email
    driver.find_element_by_id("email_address").send_keys(
        inserts["TotalVisa"]["email_address"])
    driver.find_element_by_id("verify_email_address").send_keys(
        inserts["TotalVisa"]["verify_email_address"])
    # Address
    driver.find_element_by_id("address_line_1").send_keys(
        inserts["TotalVisa"]["address_line_1"])
    driver.find_element_by_id("address_city").send_keys(
        inserts["TotalVisa"]["address_city"])
    Addr_State = driver.find_element_by_id("address_state")
    for State in Addr_State.find_elements_by_tag_name('option'):
        if State.text == inserts["TotalVisa"]["address_state"]:
            State.click()  # select() in earlier versions of webdriver
            break
    driver.find_element_by_id("address_zip").send_keys(
        inserts["TotalVisa"]["address_zip"])
    # Phones
    driver.find_element_by_id("home_phone").send_keys(inserts["TotalVisa"]["home_phone"])
    driver.find_element_by_id("mobile_phone").send_keys(
        inserts["TotalVisa"]["mobile_phone"])
    # Checking
    btn_Check = "//*[@name='has_checking_account'][@value='" + \
        inserts["TotalVisa"]["has_checking_account"] + "']"
    driver.find_element_by_xpath(btn_Check).click()
    # Card
    # Not Currently Sure How to Select
    # TakePic
    TakeScreenShot(driver, 'Pg1_End')
    # Submit
    driver.find_element_by_id("cta_continue").click()


def Total_Page2(driver):
    # TakePic
    TakeScreenShot(driver, 'Pg2_Begin')
    # Age
    Months = driver.find_element_by_id("dob_mm")
    for Mo in Months.find_elements_by_tag_name('option'):
        if Mo.text == inserts["TotalVisa"]["dob_mm"]:
            Mo.click()  # select() in earlier versions of webdriver
            break
    Days = driver.find_element_by_id("dob_dd")
    for Da in Days.find_elements_by_tag_name('option'):
        if Da.text == inserts["TotalVisa"]["dob_dd"]:
            Da.click()  # select() in earlier versions of webdriver
            break
    Years = driver.find_element_by_id("dob_yyyy")
    for Yr in Years.find_elements_by_tag_name('option'):
        if Yr.text == inserts["TotalVisa"]["dob_yyyy"]:
            Yr.click()  # select() in earlier versions of webdriver
            break
    # SSN
    driver.find_element_by_id("ssn").send_keys(inserts["TotalVisa"]["ssn"])
    driver.find_element_by_id("verify_ssn").send_keys(inserts["TotalVisa"]["verify_ssn"])
    # Occupation
    Work = driver.find_element_by_id("occupation")
    for job in Work.find_elements_by_tag_name('option'):
        if job.text == inserts["TotalVisa"]["occupation"]:
            job.click()  # select() in earlier versions of webdriver
            break
    # Income
    driver.find_element_by_id("monthly_income_amount").send_keys(
        inserts["TotalVisa"]["monthly_income_amount"])
    driver.find_element_by_id(
        "monthly_obligation_amount").send_keys(inserts["TotalVisa"]["monthly_obligation_amount"])
    # Debit
    btn_Debit = "//*[@name='has_debit_credit_card'][@value='" + \
        inserts["TotalVisa"]["has_debit_credit_card"] + "']"
    driver.find_element_by_xpath(btn_Debit).click()
    # Cash Adv
    btn_CashAdv = "//*[@name='cash_advance'][@value='" + \
        inserts["TotalVisa"]["cash_advance"] + "']"
    driver.find_element_by_xpath(btn_CashAdv).click()
    # Addl Card
    btn_AddlCard = "//*[@name='additional_card'][@value='" + \
        inserts["TotalVisa"]["additional_card"] + "']"
    driver.find_element_by_xpath(btn_AddlCard).click()
    # TakePic
    TakeScreenShot(driver, 'Pg2_End')
    # Submit
    driver.find_element_by_id("app2_continue").click()


def Total_Page3(driver):
    # TakePic
    TakeScreenShot(driver, 'Pg3_Begin')
    # Electronic Comms
    driver.find_element_by_id("electronic_consent_yes").click()
    # Electronic stmt
    driver.find_element_by_id("statement_electronic").click()
    # Acknowledge
    driver.find_element_by_id("disclosure_consent").click()
    # TakePic
    TakeScreenShot(driver, 'Pg3_End')
    # Submit
    driver.find_element_by_id("disclosures_continue").click()


def Total_Page4(driver):
    # TakePic
    TakeScreenShot(driver, 'Pg4_Begin')
    # Get AppID
    fullmessage = driver.find_element_by_xpath("/html/body/div[2]").text
    rightmessage = fullmessage.split("Your Application ID:", 1)[1]
    AppID = [int(i) for i in rightmessage.split() if i.isdigit()][0]
    # Download PDF
    # TakePic
    TakeScreenShot(driver, 'Pg4_End')
    return AppID


def Total_TestApp(driver, Path):
    Total_Page1(driver)
    Total_Page2(driver)
    Total_Page3(driver)
    AppID = Total_Page4(driver)
    return AppID


def TotalApp(driver):
    # Set Directory
    Path = setdirectory()
    # Make temp folder
    tempfolder = maketempfolder(Path)
    os.chdir(tempfolder)
    # Test App, get AppID
    AppID = Total_TestApp(driver, Path)
    # Rename Folder
    newfolder = renametempfolder('Total', Path, AppID)