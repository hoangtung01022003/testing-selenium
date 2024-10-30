# tests/test_withdraw.py

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pages.withdraw_page import WithdrawPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestWithdraw:
    @pytest.fixture(scope="module")
    def setup(self):
        """Thiết lập WebDriver Edge."""
        edge_driver_path = "D:\\Ungdung\\edge\\msedgedriver.exe"  # Đường dẫn tới msedgedriver trên Windows
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service)
        yield driver
        driver.quit()

    def open_withdraw_page(self, driver):
        """Mở trang Withdraw."""
        self.withdraw_page = WithdrawPage(driver)
        self.withdraw_page.open()
        # Chờ cho trường Account No có sẵn
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "accountno")))

    def test_withdraw_success(self, setup):
        """Kiểm thử rút tiền thành công với dữ liệu hợp lệ."""
        self.open_withdraw_page(setup)
        self.withdraw_page.enter_account_number("123456")
        self.withdraw_page.enter_amount("10000")
        self.withdraw_page.enter_description("Withdrawal for testing")
        self.withdraw_page.click_submit()
        assert self.withdraw_page.get_success_message() == "Withdrawal Successful", "Thông báo không đúng."

    def test_withdraw_account_no_empty(self, setup):
        """Kiểm thử rút tiền khi Account No để trống."""
        self.open_withdraw_page(setup)
        self.withdraw_page.enter_account_number("")
        self.withdraw_page.enter_amount("10000")
        self.withdraw_page.enter_description("Withdrawal for testing")
        self.withdraw_page.click_submit()
        assert self.withdraw_page.get_error_message() == "Account No must not be blank", "Thông báo không đúng."

    def test_withdraw_amount_empty(self, setup):
        """Kiểm thử rút tiền khi Amount để trống."""
        self.open_withdraw_page(setup)
        self.withdraw_page.enter_account_number("123456")
        self.withdraw_page.enter_amount("")
        self.withdraw_page.enter_description("Withdrawal for testing")
        self.withdraw_page.click_submit()
        assert self.withdraw_page.get_error_message() == "Amount must not be blank", "Thông báo không đúng."

    def test_withdraw_description_empty(self, setup):
        """Kiểm thử rút tiền khi Description để trống."""
        self.open_withdraw_page(setup)
        self.withdraw_page.enter_account_number("123456")
        self.withdraw_page.enter_amount("10000")
        self.withdraw_page.enter_description("")
        self.withdraw_page.click_submit()
        assert self.withdraw_page.get_success_message() == "Withdrawal Successful", "Thông báo không đúng."  # Giả sử không yêu cầu nhập mô tả

    def test_withdraw_amount_invalid(self, setup):
        """Kiểm thử rút tiền với Amount không hợp lệ."""
        self.open_withdraw_page(setup)
        self.withdraw_page.enter_account_number("123456")
        self.withdraw_page.enter_amount("invalid_amount")
        self.withdraw_page.enter_description("Withdrawal for testing")
        self.withdraw_page.click_submit()
        assert self.withdraw_page.get_error_message() == "Amount must be numeric", "Thông báo không đúng."
