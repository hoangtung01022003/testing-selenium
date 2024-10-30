# tests/test_deposit.py

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pages.deposit_page import DepositPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestDeposit:
    @pytest.fixture(scope="module")
    def setup(self):
        """Thiết lập WebDriver Edge."""
        edge_driver_path = "D:\\Ungdung\\edge\\msedgedriver.exe"  # Đường dẫn tới msedgedriver trên Mac
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service)
        yield driver
        driver.quit()

    def open_deposit_page(self, driver):
        """Mở trang Deposit."""
        self.deposit_page = DepositPage(driver)
        self.deposit_page.open()
        # Chờ cho trường Account No có sẵn
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "accountno")))

    def test_deposit_success(self, setup):
        """Kiểm thử gửi tiền thành công với dữ liệu hợp lệ."""
        self.open_deposit_page(setup)
        self.deposit_page.enter_account_number("123456")
        self.deposit_page.enter_amount("10000")
        self.deposit_page.enter_description("Deposit for testing")
        self.deposit_page.click_submit()
        assert self.deposit_page.get_success_message() == "Deposit Successful", "Thông báo không đúng."

    def test_deposit_account_no_empty(self, setup):
        """Kiểm thử gửi tiền khi Account No để trống."""
        self.open_deposit_page(setup)
        self.deposit_page.enter_account_number("")
        self.deposit_page.enter_amount("10000")
        self.deposit_page.enter_description("Deposit for testing")
        self.deposit_page.click_submit()
        assert self.deposit_page.get_error_message() == "Account No must not be blank", "Thông báo không đúng."

    def test_deposit_amount_empty(self, setup):
        """Kiểm thử gửi tiền khi Amount để trống."""
        self.open_deposit_page(setup)
        self.deposit_page.enter_account_number("123456")
        self.deposit_page.enter_amount("")
        self.deposit_page.enter_description("Deposit for testing")
        self.deposit_page.click_submit()
        assert self.deposit_page.get_error_message() == "Amount must not be blank", "Thông báo không đúng."

    def test_deposit_description_empty(self, setup):
        """Kiểm thử gửi tiền khi Description để trống."""
        self.open_deposit_page(setup)
        self.deposit_page.enter_account_number("123456")
        self.deposit_page.enter_amount("10000")
        self.deposit_page.enter_description("")
        self.deposit_page.click_submit()
        assert self.deposit_page.get_success_message() == "Deposit Successful", "Thông báo không đúng."  # Giả sử không yêu cầu nhập mô tả

    def test_deposit_amount_invalid(self, setup):
        """Kiểm thử gửi tiền với Amount không hợp lệ."""
        self.open_deposit_page(setup)
        self.deposit_page.enter_account_number("123456")
        self.deposit_page.enter_amount("invalid_amount")
        self.deposit_page.enter_description("Deposit for testing")
        self.deposit_page.click_submit()
        assert self.deposit_page.get_error_message() == "Amount must be numeric", "Thông báo không đúng."
