
from ScreenShotter import TakeScreenShot


def T01_Page1(driver, inserts):
    # TakePic
    TakeScreenShot(driver, 'Pg1_Begin')
    # Name
    driver.find_element_by_id("first_name").send_keys(inserts[0]["first_name"])
    driver.find_element_by_id("last_name").send_keys(inserts[0]["last_name"])
    # Email
    driver.find_element_by_id("email_address").send_keys(
        inserts[0]["email_address"])
    driver.find_element_by_id("verify_email_address").send_keys(
        inserts[0]["verify_email_address"])
    # Address
    driver.find_element_by_id("address_line_1").send_keys(
        inserts[0]["address_line_1"])
    driver.find_element_by_id("address_city").send_keys(
        inserts[0]["address_city"])
    Addr_State = driver.find_element_by_id("address_state")
    for State in Addr_State.find_elements_by_tag_name('option'):
        if State.text == inserts[0]["address_state"]:
            State.click()  # select() in earlier versions of webdriver
            break
    driver.find_element_by_id("address_zip").send_keys(
        inserts[0]["address_zip"])
    # Phones
    driver.find_element_by_id("home_phone").send_keys(inserts[0]["home_phone"])
    driver.find_element_by_id("mobile_phone").send_keys(
        inserts[0]["mobile_phone"])
    # Checking
    btn_Check = "//*[@name='has_checking_account'][@value='" + \
        inserts[0]["has_checking_account"] + "']"
    driver.find_element_by_xpath(btn_Check).click()
    # Card
    # Not Currently Sure How to Select
    # TakePic
    TakeScreenShot(driver, 'Pg1_End')
    # Submit
    driver.find_element_by_id("cta_continue").click()


def T01_Page2(driver, inserts):
    # TakePic
    TakeScreenShot(driver, 'Pg2_Begin')
    # Age
    Months = driver.find_element_by_id("dob_mm")
    for Mo in Months.find_elements_by_tag_name('option'):
        if Mo.text == inserts[1]["dob_mm"]:
            Mo.click()  # select() in earlier versions of webdriver
            break
    Days = driver.find_element_by_id("dob_dd")
    for Da in Days.find_elements_by_tag_name('option'):
        if Da.text == inserts[1]["dob_dd"]:
            Da.click()  # select() in earlier versions of webdriver
            break
    Years = driver.find_element_by_id("dob_yyyy")
    for Yr in Years.find_elements_by_tag_name('option'):
        if Yr.text == inserts[1]["dob_yyyy"]:
            Yr.click()  # select() in earlier versions of webdriver
            break
    # SSN
    driver.find_element_by_id("ssn").send_keys(inserts[1]["ssn"])
    driver.find_element_by_id("verify_ssn").send_keys(inserts[1]["verify_ssn"])
    # Occupation
    Work = driver.find_element_by_id("occupation")
    for job in Work.find_elements_by_tag_name('option'):
        if job.text == inserts[1]["occupation"]:
            job.click()  # select() in earlier versions of webdriver
            break
    # Income
    driver.find_element_by_id("monthly_income_amount").send_keys(
        inserts[1]["monthly_income_amount"])
    driver.find_element_by_id(
        "monthly_obligation_amount").send_keys(inserts[1]["monthly_obligation_amount"])
    # Debit
    btn_Debit = "//*[@name='has_debit_credit_card'][@value='" + \
        inserts[1]["has_debit_credit_card"] + "']"
    driver.find_element_by_xpath(btn_Debit).click()
    # Cash Adv
    btn_CashAdv = "//*[@name='cash_advance'][@value='" + \
        inserts[1]["cash_advance"] + "']"
    driver.find_element_by_xpath(btn_CashAdv).click()
    # Addl Card
    btn_AddlCard = "//*[@name='additional_card'][@value='" + \
        inserts[1]["additional_card"] + "']"
    driver.find_element_by_xpath(btn_AddlCard).click()
    # TakePic
    TakeScreenShot(driver, 'Pg2_End')
    # Submit
    driver.find_element_by_id("app2_continue").click()


def T01_Page3(driver, inserts):
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


def T01_Page4(driver, inserts):
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


def T01_TestApp(driver, inserts, Path):
    T01_Page1(driver, inserts)
    T01_Page2(driver, inserts)
    T01_Page3(driver, inserts)
    AppID = T01_Page4(driver, inserts)
    return AppID
