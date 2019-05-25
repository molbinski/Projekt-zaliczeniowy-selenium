# -*- coding: utf-8 -*-
from Project.locators import HomePageLocators
from base_page import BasePage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class HomePage(BasePage):

    def click_search_button(self):
        goToSearch = self.driver.find_element(*HomePageLocators.goToSearch)
        goToSearch.click()
