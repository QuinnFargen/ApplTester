#############################################
# Testing & Submitting Apps

# Import funcs
from Drivers import get_driver
from TotalVisa import TotalApp
# from FirstPremier import FirstPremApp

########################################
# TotalVisa:
weburl = 'https://totalcardvisa.com/'
headless = False
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



elements=driver.find_elements_by_xpath("/html/body/form/div")
id_list=[]
for ele in elements:
    id_list.append(ele.get_attribute("id"))