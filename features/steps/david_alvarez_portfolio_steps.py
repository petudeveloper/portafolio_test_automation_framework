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
