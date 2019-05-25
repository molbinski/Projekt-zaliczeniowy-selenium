from Project.locators import searchPageLocators
from base_page import BasePage

class SearchPage(BasePage):
    """Home page action methods come here. I.e. Python.org"""

    def fill_search_field(self, valid_player):
        field = self.driver.find_element(*searchPageLocators.searchText)
        field.send_keys(valid_player)

    def click_search_player_button(self):
        """Triggers the search"""
        searchButton = self.driver.find_element(*searchPageLocators.searchButton)
        searchButton.click()
