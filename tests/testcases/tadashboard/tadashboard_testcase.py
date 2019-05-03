'''
Created on May 2, 2019

@author: huy.quoc.vo
'''
from tests.testcases.test_base import TestBase
from tests.pages.TADashBoard.dash_board_login_page import DashBoardLoginPage
from tests.pages.TADashBoard.dash_board_home_page import DashBoardHomePage
from selenpy.support import browser
import time

class DashBoardLoginTest(TestBase):
    
    login_page = DashBoardLoginPage()
    home_page = DashBoardHomePage()
    
    
    def test_DA_LOGIN_TC001(self):
        self.login_page.open_ta_dashboard()
        self.login_page.login("administrator", "")
        assert self.home_page._main_page.is_displayed()
        assert self.home_page._label_user_name.is_displayed()
        self.home_page._dashboard_logout()
        #time.sleep(10)
    def test_DA_LOGIN_TC002(self):
        self.login_page.open_ta_dashboard()
        self.login_page.login("abc", "abc")
        self.login_page._check_invalid_message()
        #self.login_page.check_error_message_displayed()
       
     
