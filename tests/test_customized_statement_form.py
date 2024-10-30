# tests/test_customized_statement.py

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pages.customized_statement_page import CustomizedStatementPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestCustomizedStatement:
    @pytest.fixture(scope="module")
    def setup(self):
        """Thiết lập WebDriver Edge."""
        edge_driver_path = "D:\\Ungdung\\edge\\msedgedriver.exe"  # Đường dẫn tới msedgedriver trên Windows
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service)
        yield driver
        driver.quit()

    def open_customized_statement_page(self, driver):
        """Mở trang Customized Statement Form."""
        self.statement_page = CustomizedStatementPage(driver)
        self.statement_page.open()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.TAG_NAME, "table")))

    def test_submit_customized_statement(self, setup):
        """Kiểm thử gửi Customized Statement Form thành công."""
        self.open_customized_statement_page(setup)

        # Nhập thông tin hợp lệ vào biểu mẫu
        self.statement_page.fill_form(
            account_no="123456",
            from_date="2024-01-01",
            to_date="2024-01-31",
            min_transaction="1000",
            num_transaction="5"
        )

        # Gửi biểu mẫu
        self.statement_page.submit_form()

        # Kiểm tra thông báo xác nhận
        assert self.statement_page.get_confirmation_message() == "Thông báo xác nhận ở đây", "Thông báo không đúng."

    def test_submit_without_account_no(self, setup):
        """Kiểm thử gửi Customized Statement Form mà không có số tài khoản."""
        self.open_customized_statement_page(setup)

        # Không nhập số tài khoản
        self.statement_page.fill_form(
            account_no="",
            from_date="2024-01-01",
            to_date="2024-01-31",
            min_transaction="1000",
            num_transaction="5"
        )

        # Gửi biểu mẫu
        self.statement_page.submit_form()

        # Kiểm tra thông báo lỗi cho số tài khoản
        assert self.statement_page.get_confirmation_message() == "Số tài khoản không được để trống", "Thông báo lỗi không đúng."

    def test_submit_with_invalid_account_no(self, setup):
        """Kiểm thử gửi Customized Statement Form với số tài khoản không hợp lệ."""
        self.open_customized_statement_page(setup)

        # Nhập số tài khoản không hợp lệ
        self.statement_page.fill_form(
            account_no="abc123",
            from_date="2024-01-01",
            to_date="2024-01-31",
            min_transaction="1000",
            num_transaction="5"
        )

        # Gửi biểu mẫu
        self.statement_page.submit_form()

        # Kiểm tra thông báo lỗi cho số tài khoản không hợp lệ
        assert self.statement_page.get_confirmation_message() == "Số tài khoản không hợp lệ", "Thông báo lỗi không đúng."

    def test_submit_without_dates(self, setup):
        """Kiểm thử gửi Customized Statement Form mà không có ngày."""
        self.open_customized_statement_page(setup)

        # Không nhập ngày
        self.statement_page.fill_form(
            account_no="123456",
            from_date="",
            to_date="",
            min_transaction="1000",
            num_transaction="5"
        )

        # Gửi biểu mẫu
        self.statement_page.submit_form()

        # Kiểm tra thông báo lỗi cho ngày
        assert self.statement_page.get_confirmation_message() == "Ngày không được để trống", "Thông báo lỗi không đúng."

    def test_submit_with_invalid_transaction_value(self, setup):
        """Kiểm thử gửi Customized Statement Form với giá trị giao dịch không hợp lệ."""
        self.open_customized_statement_page(setup)

        # Nhập giá trị giao dịch không hợp lệ
        self.statement_page.fill_form(
            account_no="123456",
            from_date="2024-01-01",
            to_date="2024-01-31",
            min_transaction="-500",  # Giá trị âm không hợp lệ
            num_transaction="5"
        )

        # Gửi biểu mẫu
        self.statement_page.submit_form()

        # Kiểm tra thông báo lỗi cho giá trị giao dịch không hợp lệ
        assert self.statement_page.get_confirmation_message() == "Giá trị giao dịch không hợp lệ", "Thông báo lỗi không đúng."
