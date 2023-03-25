# Use Pytest using Page Object Model

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from Test_Data.data import Subash_Data
from Test_Locators.locators import Subash_Locators
import pytest

class Test_Subash:

    #Booting method for running the Pytest test cases
    @pytest.fixture
    def boot(self):
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
        self.driver.implicitly_wait(10)
        yield   
    
    def test_edit(self, boot):
        self.driver.get(Subash_Data().url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.find_element(by=By.NAME, value=Subash_Locators().username_input_box).send_keys(Subash_Data().username)
        self.driver.find_element(by=By.NAME, value=Subash_Locators().password_input_box).send_keys(Subash_Data().password)
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().submit_button).click()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Admin_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Admin_holder_1)
        self.driver.refresh()

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Pim_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Pim_holder_1)

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Leave_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Leave_holder_1)

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Time_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Time_holder_1)

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Recruitment_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Recruitment_holder_1)

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Info_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Info_holder_1)

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Performance_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Performance_holder_1)

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Dashboard_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Dashboard_holder_1)

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Directory_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Directory_holder_1)

        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Maintenance_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Maintenance_holder_1)
        
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Buzz_holder)
        self.driver.refresh()
        self.driver.find_element(by=By.XPATH, value=Subash_Locators().placeholder_button).send_keys(Subash_Data().Buzz_holder_1)
        
        print("The user should able to search above mentioned admin and individual menu name should displayed under text box")
        
        while(True):
            pass
       