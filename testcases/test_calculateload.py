import time

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


class Testload:
    baseurl = 'https://practice.expandtesting.com/webpark'

    def test_calculateload(self):
        self.driver = webdriver.Chrome()
        self.driver.get(self.baseurl)
        self.driver.maximize_window()
        self.driver.find_element(By.XPATH, '//*[@id="entryTime"]').clear()
        self.driver.find_element(By.XPATH, '//*[@id="entryTime"]').send_keys('18:00')
        self.driver.find_element(By.XPATH, '//*[@id="exitTime"]').clear()
        self. driver.find_element(By.XPATH, '//*[@id="exitTime"]').send_keys('18:00')
        self.driver.find_element(By.XPATH, '//*[@id="calculateCost"]').click()
        time.sleep(10)



