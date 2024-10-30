# tests/test_new_account.py

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from pages.new_account_page import NewAccountPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNewAccount:
    @pytest.fixture(scope="module")
    def setup(self):
        """Thiết lập WebDriver Edge."""
        edge_driver_path = "D:\\Ungdung\\edge\\msedgedriver.exe"
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service)
        yield driver
        driver.quit()

    def open_new_account_page(self, driver):
        """Mở trang New Account."""
        self.new_account_page = NewAccountPage(driver)
        self.new_account_page.open()
        # Chờ cho trường Customer ID có sẵn
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "cusid")))

    def test_create_account_with_valid_data(self, setup):
        """Kiểm thử tạo tài khoản với dữ liệu hợp lệ."""
        self.open_new_account_page(setup)
        self.new_account_page.enter_customer_id("12345")
        self.new_account_page.select_account_type("Savings")
        self.new_account_page.enter_initial_deposit("1000")
        self.new_account_page.click_submit()
        assert self.new_account_page.get_success_message() == "Account created successfully", "Thông báo không đúng."

    def test_create_account_with_invalid_customer_id(self, setup):
        """Kiểm thử tạo tài khoản với Customer ID không hợp lệ."""
        self.open_new_account_page(setup)
        self.new_account_page.enter_customer_id("")  # Customer ID trống
        self.new_account_page.select_account_type("Savings")
        self.new_account_page.enter_initial_deposit("1000")
        self.new_account_page.click_submit()
        assert self.new_account_page.get_error_message() == "Customer ID must not be blank", "Thông báo không đúng."

    def test_create_account_with_invalid_account_type(self, setup):
        """Kiểm thử tạo tài khoản với loại tài khoản không hợp lệ."""
        self.open_new_account_page(setup)
        self.new_account_page.enter_customer_id("12345")
        self.new_account_page.select_account_type("InvalidType")  # Loại tài khoản không hợp lệ
        self.new_account_page.enter_initial_deposit("1000")
        self.new_account_page.click_submit()
        assert self.new_account_page.get_error_message() == "Invalid account type", "Thông báo không đúng."

    def test_create_account_with_negative_initial_deposit(self, setup):
        """Kiểm thử tạo tài khoản với Initial Deposit âm."""
        self.open_new_account_page(setup)
        self.new_account_page.enter_customer_id("12345")
        self.new_account_page.select_account_type("Savings")
        self.new_account_page.enter_initial_deposit("-1000")
        self.new_account_page.click_submit()
        assert self.new_account_page.get_error_message() == "Initial Deposit must be positive", "Thông báo không đúng."

    def test_create_account_with_empty_initial_deposit(self, setup):
        """Kiểm thử tạo tài khoản với Initial Deposit trống."""
        self.open_new_account_page(setup)
        self.new_account_page.enter_customer_id("12345")
        self.new_account_page.select_account_type("Savings")
        self.new_account_page.enter_initial_deposit("")  # Trống
        self.new_account_page.click_submit()
        assert self.new_account_page.get_error_message() == "Initial Deposit must not be blank", "Thông báo không đúng."

    def test_reset_functionality(self, setup):
        """Kiểm thử chức năng reset."""
        self.open_new_account_page(setup)
        self.new_account_page.enter_customer_id("12345")
        self.new_account_page.select_account_type("Savings")
        self.new_account_page.enter_initial_deposit("1000")
        self.new_account_page.click_reset()  # Nhấn nút reset
        assert self.new_account_page.driver.find_element(By.NAME, "cusid").get_attribute('value') == "", "Trường Customer ID không được đặt lại."
        assert self.new_account_page.driver.find_element(By.NAME, "inideposit").get_attribute('value') == "", "Trường Initial Deposit không được đặt lại."
