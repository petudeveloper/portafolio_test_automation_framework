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
    assert_that(context.page.return_title()).is_equal_to(page_title)


@step('I can see "{heading}" main heading')
def check_page_main_title(context, heading):
    """
    This method verifies the h1 heading of a webpage
    :param heading: str. expected h1
    :param context: behave.context. behaves variable used to share values between steps
    """
    assert_that(context.page.get_current_page_main_heading()).is_equal_to(
        heading
    )
