import configparser

from loguru import logger
from selenium import webdriver


def before_all(context):
    """
    These run before the whole shooting match
    :param context: behave.context. behaves variable used to share values between steps
    """
    settings = configparser.ConfigParser()

    settings.read("./settings.ini")
    context.device = settings["config"]["device"]
    context.browser = settings["config"]["browser"]

    if context.device == "pc":
        if context.browser == "chrome":
            context.driver = webdriver.Chrome()
        elif context.browser == "firefox":
            context.driver = webdriver.Firefox()
        else:
            logger.error("Only supported browser is Chrome")
    else:
        logger.error("Only supported device is PC")


def after_all(context):
    """
    These run after the whole shooting match
    :param context: behave.context. behaves variable used to share values between steps
    """
    if context.device == "pc" and context.browser == "firefox":
        context.driver.quit()
