from behave import *
from frontend.page import Page


@step('we have behave installed')
def step_impl(context):
    context.page = Page()
    context.page.do_something()
    pass


@step('we implement a test')
def step_impl(context):
    context.page.do_something()
    assert True is not False


@step('behave will test it for us!')
def step_impl(context):
    assert context.failed is False
