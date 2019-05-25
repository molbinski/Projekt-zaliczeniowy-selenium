# -*- coding: utf-8 -*-
# import bibliotek

import unittest
import sys
from selenium import webdriver
from Project.pages.home_page import HomePage
import Project.test_data.test_data as td
from Project.pages.search_page import SearchPage
import time

class SearchProcentTest(unittest.TestCase):
    def setUp(self):
        url = 'http://90minut.pl'
        self.driver = webdriver.Chrome('C:\Users\molbinski\Desktop\Nowy folder (2)\chromedriver.exe')
        self.driver.maximize_window()
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()

    def test_search(self):
        #1. Kliknij szukaj
        driver = self.driver
        home_page = HomePage(self.driver)
        home_page.click_search_button()
        time.sleep(5)
        #2. Wpisz w searchBoxie 'Marek Cit%'
        search_page = SearchPage(self.driver)
        search_page.fill_search_field(td.valid_player)
        time.sleep(2)
        #3. Kliknij szukaj
        search_page.click_search_player_button()
        time.sleep(2)

        #1. asercja - wyszukiwarka znajdzie Marka Citko
        assert('Marek Citko' in driver.page_source)
        #assert(driver.find_element_by_partial_link_text('Marek Citko')==td.valid_player_answ)wq



if __name__ == "__main__":
    unittest.main(verbosity=2)
