# -*- coding: utf-8 -*-

class BasePage(object):
    """
    Klasa bazowa, z której będą korzystały wszystkie podstrony (pages)
    """

    def __init__(self, driver):
        self.driver = driver
