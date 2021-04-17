

# Pythons
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options  
import os

def get_driver(weburl, headless):
    if os.name == 'posix':  #Mac
        driverpath = '/Users/quinnfargen/Documents/GitHub/ApplTester/drivers/chromedriver_mac.exe'
    elif os.name == 'nt':   #Win
        driverpath = 'C:\\Users\\Quinn\\Desktop\\AppTester\\drivers\\chromedriver.exe'
    chrome_options = Options()  
    if headless == True:
        chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(driverpath, chrome_options=chrome_options)
    driver.get(weburl)
    return driver