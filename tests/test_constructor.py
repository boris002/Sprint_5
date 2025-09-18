from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import TAB_BUNS, TAB_FILLINGS, TAB_SAUCES, TEXT_BUNS, TEXT_FILLINGS, TEXT_SAUCES
import pytest
class TestTabsNavigation:

    def test_go_to_buns(self, driver):
        driver.find_element(*TAB_SAUCES).click()
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located(TEXT_SAUCES))
        driver.find_element(*TAB_BUNS).click()
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located(TEXT_BUNS))
        buns_h2 = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TEXT_BUNS))
        assert buns_h2.is_displayed()

    def test_go_to_sauces(self, driver):
        driver.find_element(*TAB_SAUCES).click()
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located(TEXT_SAUCES))
        sauces_h2 = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TEXT_SAUCES))
        assert sauces_h2.is_displayed()

    def test_go_to_fillings(self, driver):
        driver.find_element(*TAB_FILLINGS).click()
        WebDriverWait(driver, 1).until(EC.visibility_of_element_located(TEXT_FILLINGS))
        fillings_h2 = WebDriverWait(driver, 3).until(EC.visibility_of_element_located(TEXT_FILLINGS))
        assert fillings_h2.is_displayed()