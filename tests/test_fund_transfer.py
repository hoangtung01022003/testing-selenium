# tests/test_fund_transfer.py

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pages.fund_transfer_page import FundTransferPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestFundTransfer:
    @pytest.fixture(scope="module")
    def setup(self):
        """Thiết lập WebDriver Edge."""
        edge_driver_path = "D:\\Ungdung\\edge\\msedgedriver.exe"  # Đường dẫn tới msedgedriver trên Windows
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service)
        yield driver
        driver.quit()

    def open_fund_transfer_page(self, driver):
        """Mở trang Fund Transfer."""
        self.fund_transfer_page = FundTransferPage(driver)
        self.fund_transfer_page.open()
        # Chờ cho trường Payers Account No có sẵn
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "payersaccount")))

    def test_fund_transfer_success(self, setup):
        """Kiểm thử chuyển khoản thành công với dữ liệu hợp lệ."""
        self.open_fund_transfer_page(setup)
        self.fund_transfer_page.enter_payers_account("123456")
        self.fund_transfer_page.enter_payees_account("654321")
        self.fund_transfer_page.enter_amount("5000")
        self.fund_transfer_page.enter_description("Transfer for testing")
        self.fund_transfer_page.click_submit()
        assert self.fund_transfer_page.get_success_message() == "Fund transfer Successful", "Thông báo không đúng."

    def test_fund_transfer_empty_payers_account(self, setup):
        """Kiểm thử chuyển khoản khi Payers Account No để trống."""
        self.open_fund_transfer_page(setup)
        self.fund_transfer_page.enter_payers_account("")
        self.fund_transfer_page.enter_payees_account("654321")
        self.fund_transfer_page.enter_amount("5000")
        self.fund_transfer_page.enter_description("Transfer for testing")
        self.fund_transfer_page.click_submit()
        assert self.fund_transfer_page.get_error_message() == "Payers Account No must not be blank", "Thông báo không đúng."

    def test_fund_transfer_empty_payees_account(self, setup):
        """Kiểm thử chuyển khoản khi Payees Account No để trống."""
        self.open_fund_transfer_page(setup)
        self.fund_transfer_page.enter_payers_account("123456")
        self.fund_transfer_page.enter_payees_account("")
        self.fund_transfer_page.enter_amount("5000")
        self.fund_transfer_page.enter_description("Transfer for testing")
        self.fund_transfer_page.click_submit()
        assert self.fund_transfer_page.get_error_message() == "Payees Account No must not be blank", "Thông báo không đúng."

    def test_fund_transfer_empty_amount(self, setup):
        """Kiểm thử chuyển khoản khi Amount để trống."""
        self.open_fund_transfer_page(setup)
        self.fund_transfer_page.enter_payers_account("123456")
        self.fund_transfer_page.enter_payees_account("654321")
        self.fund_transfer_page.enter_amount("")
        self.fund_transfer_page.enter_description("Transfer for testing")
        self.fund_transfer_page.click_submit()
        assert self.fund_transfer_page.get_error_message() == "Amount must not be blank", "Thông báo không đúng."

    def test_fund_transfer_empty_description(self, setup):
        """Kiểm thử chuyển khoản khi Description để trống."""
        self.open_fund_transfer_page(setup)
        self.fund_transfer_page.enter_payers_account("123456")
        self.fund_transfer_page.enter_payees_account("654321")
        self.fund_transfer_page.enter_amount("5000")
        self.fund_transfer_page.enter_description("")
        self.fund_transfer_page.click_submit()
        assert self.fund_transfer_page.get_success_message() == "Fund transfer Successful", "Thông báo không đúng."  # Giả sử không yêu cầu nhập mô tả

    def test_fund_transfer_invalid_amount(self, setup):
        """Kiểm thử chuyển khoản với Amount không hợp lệ."""
        self.open_fund_transfer_page(setup)
        self.fund_transfer_page.enter_payers_account("123456")
        self.fund_transfer_page.enter_payees_account("654321")
        self.fund_transfer_page.enter_amount("invalid_amount")
        self.fund_transfer_page.enter_description("Transfer for testing")
        self.fund_transfer_page.click_submit()
        assert self.fund_transfer_page.get_error_message() == "Amount must be numeric", "Thông báo không đúng."
