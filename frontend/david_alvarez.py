from selenium.webdriver.common.by import By

from frontend.page import Page


class DavidAlvarez(Page):
    """
    This is the class for the David Alvarez portfolio page
    """

    _about_section = (By.ID, "About")
    _experience_section = (By.ID, "#Experinece")
    _work_section = (By.ID, "#Work")
    _contact_section = (By.ID, "#Contact")

    def validate_sections(self, section):
        """
        This method validates the presence of the sections in the portfolio
        :param section:
        :return: boolean. Return true if the element is visible and false if it is not
        """
        if section == "About":
            return self.get_element_by_selector(self._about_section)
        elif section == "Experience":
            return self.get_element_by_selector(self._experience_section)
        elif section == "Work":
            return self.get_element_by_selector(self._work_section)
        elif section == "Contact":
            return self.get_element_by_selector(self._contact_section)
