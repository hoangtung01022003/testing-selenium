# pages/login_page.py
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_field = (By.NAME, "uid")
        self.password_field = (By.NAME, "password")
        self.login_button = (By.NAME, "btnLogin")
        self.error_message = (By.CLASS_NAME, "error")

    def open(self):
        self.driver.get("http://www.demo.guru99.com/V4/")

    def enter_username(self, username):
        self.driver.find_element(*self.username_field).send_keys(username)

    def enter_password(self, password):
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_login(self):
        self.driver.find_element(*self.login_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def is_login_successful(self):
        # Thay đổi logic kiểm tra này nếu cần
        return "Manager's Page" in self.driver.title
