"""
This is the test that will navigate to the table
and capture the data on the table and save it to a file
"""
import unittest
from automation_elements import AutomationElements
import desktop_automation_methods


class TestingQuasarDesktopTable(unittest.TestCase):
    """_summary_

    Args:
        unittest (_type_): _description_
    """
    @classmethod
    def setUpClass(cls):
        cls.automation_methods = desktop_automation_methods.WebElementHandler()
        cls.automation_elements = AutomationElements()
        cls.driver = cls.automation_methods.driver
        cls.file_path = "table_data.xlsx"
        cls.driver.get('https://quasar.dev/')

    def test_6_home_page(self):
        """_summary_
        """
        # Locates and clicks Accept on the Cookies Pop-Up
        web_cookies = self.automation_methods.find_element(
            self.automation_elements.web_cookies_accept_locator
        )
        web_cookies.click()

        # Locates and clicks the DOCS button at the top of the page
        web_docs = self.automation_methods.find_element(
            self.automation_elements.web_docs_locator
        )
        web_docs.click()

    def test_7_docs_page(self):
        """_summary_
        """
        # Locates and clicks the Vue Components item
        web_vc = self.automation_methods.find_element(
            self.automation_elements.web_vue_components_locator
        )
        web_vc.click()

        # Locates and clicks the Table option in the Vue Components dropdown
        web_table = self.automation_methods.find_element(
            self.automation_elements.web_vc_table_locator
        )
        web_table.click()

        # Locates and clicks the Basic usage option in the Table page list
        web_table_r7 = self.automation_methods.find_element(
            self.automation_elements.web_table_right7_locator
        )
        web_table_r7.click()
        web_table_r7.click()

        # Open the Basic usage Table dropdown
        web_table_dropdown = self.automation_methods.find_element(
            self.automation_elements.web_table_basic_usage_dropdown_button_locator
        )
        self.automation_methods.driver.execute_script("arguments[0].click();", web_table_dropdown)

        # Click the option with value "10"
        web_table_dropdown_10 = self.automation_methods.find_element(
            self.automation_elements.web_table_basic_usage_dropdown_option_10_locator
        )
        web_table_dropdown_10.click()

    def test_8_table_save(self):
        """_summary_
        """
        # Save the table data from the Basicusage Table to an XLSX file
        self.automation_methods.record_table_data(
            self.automation_elements.web_table_basic_usage_child_tables_locator,
            self.file_path
        )

    @classmethod
    def tearDownClass(cls):
        """_summary_
        """
        # Display a large popup alert with "All Done" message
        cls.automation_methods.driver.execute_script(
            "alert('All Done'); "
            "document.querySelector('style').textContent"
            "= 'body { zoom: 5; }';"
        )
        cls.automation_methods.driver.switch_to.alert.accept()
        cls.automation_methods.driver.quit()


if __name__ == '__main__':
    unittest.main()
