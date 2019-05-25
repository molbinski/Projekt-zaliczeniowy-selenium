# -*- coding: utf-8 -*-

from selenium.webdriver.common.by import By

class HomePageLocators(object):
    """A class for main page locators. All main page locators should come here"""
    goToSearch = (By.XPATH, "//*[@alt='Wyszukiwarka klubów, zawodników i sędziów w serwisie 90 Minut']")

class searchPageLocators(object):
    """A class for search results locators. All search results locators should come here"""
    searchText = (By.XPATH, "//input[@type='text']")
    searchButton = (By.XPATH, "//input[@value='SZUKAJ']")
