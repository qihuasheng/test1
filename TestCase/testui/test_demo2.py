import os
import time
from lib2to3.pgen2 import driver

from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from Common.baseui import baseUI


class Test_login:
    def test_damai(self,driver):
        #打开浏览器
        ui_driver = baseUI(driver)
        driver.get("https://detail.damai.cn/item.htm?spm=a2oeg.home.card_0.ditem_1.591b23e1IAfgml&id=592685102712")
        time.sleep(2)
        driver.find_element_by_xpath("//div[contains(text(),'立即预定')]").click()
        time.sleep(2)
        # driver.switch_to.frame("frame_reference")
        #登录
        # driver.find_element_by_xpath("//a[@attr-type='weixin']")







