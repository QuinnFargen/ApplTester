#############################################
# Testing & Submitting Apps
# Website           # https://totalcardvisa.com/
# Chrome Driver     # C:\Program Files (x86)

# Other Py Files
from TotalVisaPages import T01_TestApp
from SampleData import SampleInserts
from Storage import setdirectory, maketempfolder, renametempfolder
# Python
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import os

# Set Directory
Path = setdirectory()

# Start Tester
driverpath = 'C:\\Users\\Quinn\\Desktop\\AppTester\\drivers\\chromedriver.exe'
driver = webdriver.Chrome(driverpath)
weburl = 'https://totalcardvisa.com/'
driver.get(weburl)

# Get Data to insert
inserts = SampleInserts()

# Make temp folder
tempfolder = maketempfolder(Path)
os.chdir(tempfolder)

# Test App, get AppID
AppID = T01_TestApp(driver, inserts, Path)

# Rename Folder
newfolder = renametempfolder(Path, AppID)

# Close Tab: #driver.close()
# Close Quit
driver.quit()
