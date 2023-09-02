import time

from selenium.webdriver.common.by import By


class Page:
    """
    This is the main class of the pages. Here you can find the common methods and locators of any page.
    """

    def __init__(self, context):
        """
        This method initialize the Page Class
        :param context: behaves variable used to share values between steps
        """
        self.web_driver = context.driver

    # Locators
    _h1 = (By.TAG_NAME, "h1")

    # URL Methods
    # - url_connect
    def url_connect(self, url):
        """
        These methods navigate to the specified url
        :param url: str. url to navigate
        """
        self.web_driver.get(url)

    # - get_current_page_url
    # - refresh_page
    # - navigate_back
    # - navigate_forward
    # - execute_script

    # Page Methods
    def wait_for_page_finish_loading(self, timeout=120):
        """
        This method waits a determined for the document.readyState to be equal to complete
        :param timeout: int. seconds to be waited before raise error.
        """
        seconds_to_wait = timeout
        while (
            self.web_driver.execute_script("return document.readyState")
            != "complete"
        ):
            time.sleep(1)
            seconds_to_wait -= 1
            if seconds_to_wait == 0:
                raise TimeoutError(
                    "Page did not loaded document.readyState was never equal to complete"
                )

    # - get_current_page_tittle
    def get_current_page_main_heading(self):
        """
        This method get the current h1 text
        :return: str. inner text of h1 tag
        """
        return self.web_driver.find_element(By.CSS_SELECTOR, "h1").text

    def return_title(self):
        """
        This method get title of the page
        :return: str. inner text of title tag
        """
        return self.web_driver.title

    # - get_element_by_selector
    # - is_element_present_by_selector
    # - is_element_clickable_by_selector
    # - click_element
    # - click_element_by_selector
    # - hover_element_by_selector
    # - scroll_to_element
    # - scroll_to_top_of_page
    # - scroll_to_bottom_of_page
    # - scroll_down
    # - scroll_up
    # - close_current_tab
    # - full_page_screenshot

    # Cookie Methods
    # - add_cookie
    # - get_cookie_by_name
    # - get_all_cookies
    # - delete_cookie_by_name
    # - delete_all_cookies
