'''
Created on May 2, 2019

@author: huy.quoc.vo
'''
from selenpy.element.text_box import TextBox
from selenpy.element.base_element import BaseElement
from selenpy.support.conditions import be, have
from selenpy.support import browser
from selenpy.support import driver
import time
from selenpy.support.browser import get_driver



class DashBoardLoginPage():
    
    _txt_user_name = TextBox("id=username")
    _txt_pass_word = TextBox("id=password")
    _btn_log_in = BaseElement("class=btn-login")
        
    def __init__(self):
        pass
    
    def open_ta_dashboard(self):
        browser.open_url("http://localhost:8088/TADashboard/login.jsp")
        #browser.wait_until(have.title("Google"))

    def login(self, user_name,pass_word):
        # self._txt_search.wait_for_visible()
        self._txt_user_name.wait_until(be.visible)
        self._txt_user_name.send_keys(user_name)
        self._txt_user_name.wait_until(have.value(user_name))
        self._txt_pass_word.wait_until(be.visible)
        self._txt_pass_word.send_keys(pass_word)
        self._txt_pass_word.wait_until(have.value(pass_word))
        self._btn_log_in.click()
        
    def _check_invalid_message(self):
                     
        alert_obj = browser.get_driver().switch_to.alert
        strAlert = alert_obj.text 
        print ("Alert shows following message: "+ strAlert )
        time.sleep(2)  
        alert_obj.accept()
        print(" Clicked on the OK Button in the Alert Window")
        browser.get_driver().close
        return strAlert
                   
   
    
   
