import datetime

from behave import step

from frontend.page import Page


@step("I navigate to david's portfolio")
def navigate_to_url(context):
    """
    This method navigate to a determined url
    :param context: behave.context. behaves variable used to share values between steps
    """
    context.page = Page(context)
    context.page.url_connect("https://www.petudeveloper.com/")


@step("I verify the color contrast of the portfolio image")
def verify_color_contrast(context):
    """
    This method verify the color contrast of the portfolio image
    :param context: behave.context. behaves variable used to share values between steps
    """
    image_name = "page-screenshot-" + datetime.datetime.now().strftime(
        "%Y%m%d-%H%M%S"
    )
    context.page.page_screenshot(image_name)
    contrast = context.page.get_rms_contrast(
        r"C:\Users\jesus\Documents\almadev\portafolio_test_automation_framework\images\screenshots\page_screenshot.png"
    )
    print(contrast)
