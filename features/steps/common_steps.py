from assertpy import assert_that
from behave import step

from frontend.page import Page


@step('I navigate to "{url}"')
def navigate_to_url(context, url):
    """
    This method navigate to a determined url
    :param url: str. url to be navigated to
    :param context: behave.context. behaves variable used to share values between steps
    """
    context.page = Page(context)
    context.page.url_connect(url)


@step("I wait for page finish loading")
def wait_for_page(context):
    """
    This method waits for the readyState of the document
    :param context: behave.context. behaves variable used to share values between steps
    """
    context.page.wait_for_page_finish_loading()


@step('I verify page title is "{page_title}"')
def verify_page_title(context, page_title):
    """
    This method verifies the title tag of a webpage
    :param page_title: str. expected title
    :param context: behave.context. behaves variable used to share values between steps
    """
    actual_title = context.page.return_title()
    assert_that(actual_title).described_as(
        f"The page title doesnt match, the expected result was: '{page_title}', "
        f"but was: '{actual_title}'"
    ).is_equal_to(page_title)


@step('I can see "{heading}" main heading')
def check_page_main_title(context, heading):
    """
    This method verifies the h1 heading of a webpage
    :param heading: str. expected h1
    :param context: behave.context. behaves variable used to share values between steps
    """
    actual_heading = context.page.get_current_page_main_heading()
    assert_that(actual_heading).described_as(
        f"The page title doesnt match, the expected result was: '{heading}', "
        f"but was: '{actual_heading}'"
    ).is_equal_to(heading)


@step("I verify the presence of alternate text for all images")
def verify_alternate_text_in_all_images(context):
    """
    This method verify the presence of alternate text for all images
    :param context: behave.context. behaves variable used to share values between steps
    """
    assert_that(context.page.verify_alt_text_for_all_images()).described_as(
        "One or more images dont have the alt " "property"
    ).is_true()


@step("I check the accessibility of the page using axe tool")
def verify_accessibility_with_axe(context):
    """
    This method verify the presence of alternate text for all images
    :param context: behave.context. behaves variable used to share values between steps
    """
    result_and_report = (
        context.page.generate_accessibility_axe_result_and_report()
    )
    results = result_and_report["results"]
    report = result_and_report["report"]
    assert len(results) == 0, report
