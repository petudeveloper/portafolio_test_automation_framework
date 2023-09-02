from selenium import webdriver





def before_all(context):
    driver = webdriver.Chrome()
    driver.get("https://www.petudeveloper.com/")