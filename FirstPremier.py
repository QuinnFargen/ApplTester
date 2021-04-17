
from ScreenShotter import TakeScreenShot
from SampleData import SampleInserts
from Storage import setdirectory, maketempfolder, renametempfolder
import os

# Get Data to insert
inserts = SampleInserts()

def Premier_Page1(driver):
    # TakePic
    TakeScreenShot(driver, 'Pg1_Begin')
    # Apply for Credit Card option
    driver.find_element_by_id("IntApplyNow").click()
    # TakePic
    TakeScreenShot(driver, 'Pg1_End')


def Premier_Page2(driver):
    # TakePic
    TakeScreenShot(driver, 'Pg2_Begin')
    # Name
    driver.find_element_by_id("firstName").send_keys(inserts["FstPrem"]["first_name"])
    driver.find_element_by_id("lastName").send_keys(inserts["FstPrem"]["last_name"])
    # Address
    driver.find_element_by_id("address").send_keys(
        inserts["FstPrem"]["address_line_1"])
    driver.find_element_by_id("city").send_keys(
        inserts["FstPrem"]["address_city"])
    Addr_State = driver.find_element_by_id("state")
    for State in Addr_State.find_elements_by_tag_name('option'):
        if State.text == inserts["FstPrem"]["address_state"]:
            State.click()  # select() in earlier versions of webdriver
            break
    driver.find_element_by_id("zipCode").send_keys(
        inserts["FstPrem"]["address_zip"])
    # Phones
    driver.find_element_by_id("homePhone").send_keys(inserts["FstPrem"]["home_phone"])
    driver.find_element_by_id("cellPhone").send_keys(inserts["FstPrem"]["mobile_phone"])
    # Checks & Savin
    driver.find_element_by_id("ckChecking").click()
    # driver.find_element_by_id("ckCheckinSavings").click()
    # driver.find_element_by_id("ckNeither").click()
    # Age
    driver.find_element_by_id("dobMonth").send_keys(inserts["FstPrem"]["dob_mm"])
    driver.find_element_by_id("dobDay").send_keys(inserts["FstPrem"]["dob_dd"])
    Years = driver.find_element_by_id("dobYear")
    for Yr in Years.find_elements_by_tag_name('option'):
        if Yr.text == inserts["FstPrem"]["dob_yyyy"]:
            Yr.click()  # select() in earlier versions of webdriver
            break
    # SSN
    driver.find_element_by_id("ssn1").send_keys(inserts["FstPrem"]["ssn"][0:3])
    driver.find_element_by_id("ssn2").send_keys(inserts["FstPrem"]["ssn"][3:5])
    driver.find_element_by_id("ssn3").send_keys(inserts["FstPrem"]["ssn"][5:9])
    driver.find_element_by_id("confSsn1").send_keys(inserts["FstPrem"]["verify_ssn"][0:3])
    driver.find_element_by_id("confSsn2").send_keys(inserts["FstPrem"]["verify_ssn"][3:5])
    driver.find_element_by_id("confSsn3").send_keys(inserts["FstPrem"]["verify_ssn"][5:9])
    # Email
    driver.find_element_by_id("emailAddress").send_keys(inserts["FstPrem"]["email_address"])

    # TakePic
    TakeScreenShot(driver, 'Pg2_End')
    # Submit
    driver.find_element_by_id("SubmitButton").click()
    # driver.find_element_by_xpath("/html/body/form/").click()
    
    # If no Checking adct, have to continue app
    # driver.find_element_by_id("continueAppButton").click()


def Premier_Page3(driver):
    # TakePic
    TakeScreenShot(driver, 'Pg3_Begin')
    # Income
    driver.find_element_by_id("grossAnnualIncome").send_keys(
        inserts["FstPrem"]["annual_income_amount"])
    # TakePic
    TakeScreenShot(driver, 'Pg3_End')
    # Submit
    driver.find_element_by_id("btnSubmit").click()


def Premier_Page4(driver):
    # TakePic
    TakeScreenShot(driver, 'Pg4_Begin')
    # Submit
    driver.find_element_by_id("btnSubmit").click()
    # TakePic
    TakeScreenShot(driver, 'Pg4_Middle')
    # Elect
    driver.find_element_by_id("btnYes").click()
    # TakePic
    TakeScreenShot(driver, 'Pg4_Late')
    # Accept
    driver.find_element_by_id("btnAcceptEcorr").click()
    # TakePic
    TakeScreenShot(driver, 'Pg4_End')



def Premier_Pages(driver, Path):
    Premier_Page1(driver)
    Premier_Page2(driver)
    Premier_Page3(driver)
    AppID = Premier_Page4(driver)
    return AppID


def FirstPremApp(driver):
    # Set Directory
    Path = setdirectory()
    # Make temp folder
    tempfolder = maketempfolder(Path)
    os.chdir(tempfolder)
    # Test App, get AppID
    AppID = Premier_Pages(driver, Path)
    # Rename Folder
    newfolder = renametempfolder('Premier', Path, AppID)