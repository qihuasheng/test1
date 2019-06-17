from selenium import webdriver
import os
webdriver_path=os.path.join(os.path.dirname(__file__), r"C:\Users\Administrator\PycharmProjects\api-auto-test\chromedriver\chromedriver.exe")

driver=webdriver.Chrome(webdriver_path);