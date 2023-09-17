from behave import step

from frontend.david_alvarez import DavidAlvarez
from frontend.page import Page


@step("I navigate to david's portfolio")
def navigate_to_url(context):
    """
    This method navigate to a determined url
    :param context: behave.context. behaves variable used to share values between steps
    """
    context.page = Page(context)
    context.page.url_connect("https://www.petudeveloper.com/")


@step('I validate "{section}" in David Alvarez Portfolio')
def validate_portfolio_sections(context, section):
    """
    This method validates the content of a section of the portfolio
    :type section: str
    :param context: behave.context. behaves variable used to share values between steps
    """
    context.page = DavidAlvarez(context)
    assert context.page.validate_sections(section), (
        f"The {section} section failed to be in validated David Alvarez "
        f"Portfolio"
    )
    print(
        f"{section} section was successfully validated in David Alvarez Portfolio"
    )
