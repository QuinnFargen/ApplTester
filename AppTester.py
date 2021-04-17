#############################################
# Testing & Submitting Apps

# Import funcs
from Drivers import get_driver
from TotalVisa import TotalApp
# from FirstPremier import FirstPremApp

########################################
# TotalVisa:
weburl = 'https://totalcardvisa.com/'
headless = True
driver = get_driver(weburl,headless)

# Total Visa Test App:
TotalApp(driver)

# Close Tab: #  driver.close()
# Close Quit
driver.quit()


########################################
# First Premier:
weburl = 'https://www.premiercardoffer.net/'
headless = False
driver = get_driver(weburl,headless)

# First Premier Test App:
FirstPremApp(driver)

# Close Tab: #  driver.close()
# Close Quit
driver.quit()