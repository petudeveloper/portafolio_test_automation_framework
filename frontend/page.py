import time

from axe_selenium_python import Axe
from loguru import logger
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

    # ------------------------------------------- Locators -------------------------------------------
    _h1 = (By.TAG_NAME, "h1")
    _images_list = (By.TAG_NAME, "img")

    # ------------------------------------------- URL Methods -------------------------------------------
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

    # ------------------------------------------- Page Methods -------------------------------------------
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

    def verify_alt_text_for_all_images(self):
        """
        Verify that all the images have the alt property
        :return:
        """
        images_list = self.web_driver.find_elements(By.CSS_SELECTOR, "img")
        no_alt_images = []
        for image in images_list:
            if image.get_attribute("alt") == "":
                no_alt_images.append(image.get_attribute("src"))
        return no_alt_images

    def generate_accessibility_axe_result_and_report(self):
        """
        Run axe tool to generate accessibility test results
        :return:
        """
        axe = Axe(self.web_driver)
        # Inject axe-core javascript into page.
        axe.inject()
        # Run axe accessibility checks.
        results = axe.run()
        # Write results to file
        axe.write_results(results, "./results/a11y.json")
        # Assert no violations are found
        return {
            "results": results["violations"],
            "report": axe.report(results["violations"]),
        }

    # def get_rms_contrast(self, img_url):
    #     """
    #     Calculates the RMS contrast using the standard deviation of the greyed image pixel intensities
    #     :param img_url: str. url of the image
    #     :return:
    #     """
    #     img_grey = cv2.cvtColor(img_url, cv2.COLOR_BGR2GRAY)
    #     contrast = img_grey.std()
    #     return contrast

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
    def page_screenshot(self, image_name):
        """
        This method takes a screenshot of the page
        :param image_name: str. name of the image
        :return:
        """
        self.wait_for_page_finish_loading()
        required_width = self.web_driver.execute_script(
            "return document.body.parentNode.scrollWidth"
        )
        required_height = self.web_driver.execute_script(
            "return document.body.parentNode.scrollHeight"
        )
        self.web_driver.set_window_size(required_width, required_height)
        self.web_driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);"
        )
        body_el = self.web_driver.find_element(By.TAG_NAME, "body")
        body_el.screenshot("./images/screenshots/" + image_name + ".png")
        logger.success("took full screenshot!")

    # ------------------------------------------- Cookie Methods -------------------------------------------
    # - add_cookie
    # - get_cookie_by_name
    # - get_all_cookies
    # - delete_cookie_by_name
    # - delete_all_cookies
