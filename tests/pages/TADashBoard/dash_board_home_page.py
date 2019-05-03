'''
Created on May 2, 2019

@author: huy.quoc.vo
'''
from selenpy.element.base_element import BaseElement
from selenpy.support.conditions import be, have
from selenpy.support import browser, browsers
from selenium.webdriver.common.action_chains import ActionChains
from pydoc import browse


class DashBoardHomePage():
    
    _main_page = BaseElement("id=div_main_body")
    _label_user_name = BaseElement("//a[text() = 'administrator']")
    _label_logout = BaseElement("//a[text()='Logout']")
        

    def __init__(self):
        pass                
    
    def _dashboard_logout(self):
        self._label_user_name.click()
        self._label_logout.click()

     