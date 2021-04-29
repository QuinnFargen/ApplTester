
from element import BasePageElement
from locators import MainPageLocators
from SampleData import SampleInserts

class SearchTextElement(BasePageElement):
    """This class gets the search text from the specified locator"""

    #The locator for search box where search string is entered
    locator = 'q'


class BasePage(object):
    """Base class to initialize the base page that will be called from all
    pages"""

    # Get Data to insert
    inserts = SampleInserts()

    def __init__(self, driver):
        self.driver = driver


class TotalPg1(BasePage):
    """Total Visa Page 1"""

    def is_title_matches(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Total Visa" in self.driver.title

    def Ins_names(self):
        """Verifies that the hardcoded text "Python" appears in page title"""
        return "Total Visa" in self.driver.title
driver.find_element_by_id("first_name")

    def click_go_button(self):
        """Triggers the search"""

        element = self.driver.find_element(*MainPageLocators.GO_BUTTON)
        element.click()


class SearchResultsPage(BasePage):
    """Search results page action methods come here"""

    def is_results_found(self):
        # Probably should search for this text in the specific page
        # element, but as for now it works fine
        return "No results found." not in self.driver.page_source


