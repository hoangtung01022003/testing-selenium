import pytest
import sys
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from pages.new_customer_page import NewCustomerPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestNewCustomer:
    @pytest.fixture(scope="module")
    def setup(self):
        """Thiết lập WebDriver Edge."""
        edge_driver_path = "D:\\Ungdung\\edge\\msedgedriver.exe"
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service)
        yield driver
        driver.quit()

    def open_new_customer_page(self, driver):
        """Mở trang New Customer."""
        self.new_customer_page = NewCustomerPage(driver)
        self.new_customer_page.open()
        # Chờ cho trường tên khách hàng có sẵn
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.NAME, "name")))

    def log_error_message(self):
        """Ghi lại thông báo lỗi từ màn hình."""
        error_message = self.new_customer_page.get_error_message()
        if error_message:
            print(f"Log lỗi: {error_message}")

    def test_customer_name_with_numbers(self, setup):
        """Kiểm thử tạo tên khách hàng với số."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("thien12")
        self.new_customer_page.enter_address("Danang")
        self.new_customer_page.enter_city("DaNang")
        self.new_customer_page.enter_pin("123456")
        self.new_customer_page.enter_phone("0337526546")
        self.new_customer_page.enter_email("thien@gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.click_submit()
        self.log_error_message()  # Ghi lại thông báo lỗi
        assert self.new_customer_page.get_error_message() == "Numbers are not allowed", "Thông báo không đúng."

    def test_customer_name_with_special_characters(self, setup):
        """Kiểm thử tạo tên khách hàng với ký tự đặc biệt."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("thien**")
        self.new_customer_page.enter_address("Danang")
        self.new_customer_page.enter_city("DaNang")
        self.new_customer_page.enter_pin("123456")
        self.new_customer_page.enter_phone("0337526546")
        self.new_customer_page.enter_email("thien@gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.click_submit()
        self.log_error_message()  # Ghi lại thông báo lỗi
        assert self.new_customer_page.get_error_message() == "Special characters are not allowed", "Thông báo không đúng."

    def test_customer_address_empty(self, setup):
        """Kiểm thử địa chỉ khách hàng để trống."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("Thien")
        self.new_customer_page.enter_address("")
        self.new_customer_page.enter_city("DaNang")
        self.new_customer_page.enter_pin("123456")
        self.new_customer_page.enter_phone("0337526546")
        self.new_customer_page.enter_email("thien@gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.click_submit()
        self.log_error_message()  # Ghi lại thông báo lỗi
        assert self.new_customer_page.get_error_message() == "Address must not be blank", "Thông báo không đúng."

    def test_customer_city_empty(self, setup):
        """Kiểm thử thành phố khách hàng để trống."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("Thien")
        self.new_customer_page.enter_address("Danang")
        self.new_customer_page.enter_city("")
        self.new_customer_page.enter_pin("123456")
        self.new_customer_page.enter_phone("0337526546")
        self.new_customer_page.enter_email("thien@gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.click_submit()
        self.log_error_message()  # Ghi lại thông báo lỗi
        assert self.new_customer_page.get_error_message() == "City Field must not be blank", "Thông báo không đúng."

    def test_customer_pin_too_short(self, setup):
        """Kiểm thử mã PIN không đủ 6 chữ số."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("Thien")
        self.new_customer_page.enter_address("Danang")
        self.new_customer_page.enter_city("DaNang")
        self.new_customer_page.enter_pin("12345")
        self.new_customer_page.enter_phone("0337526546")
        self.new_customer_page.enter_email("thien@gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.click_submit()
        self.log_error_message()  # Ghi lại thông báo lỗi
        assert self.new_customer_page.get_error_message() == "PIN Code must have 6 Digits", "Thông báo không đúng."

    def test_customer_phone_special_characters(self, setup):
        """Kiểm thử số điện thoại có ký tự đặc biệt."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("Thien")
        self.new_customer_page.enter_address("Danang")
        self.new_customer_page.enter_city("DaNang")
        self.new_customer_page.enter_pin("123456")
        self.new_customer_page.enter_phone("#0234234024")
        self.new_customer_page.enter_email("thien@gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.click_submit()
        self.log_error_message()  # Ghi lại thông báo lỗi
        assert self.new_customer_page.get_error_message() == "Special characters are not allowed", "Thông báo không đúng."

    def test_customer_email_invalid(self, setup):
        """Kiểm thử email không hợp lệ."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("Thien")
        self.new_customer_page.enter_address("Danang")
        self.new_customer_page.enter_city("DaNang")
        self.new_customer_page.enter_pin("123456")
        self.new_customer_page.enter_phone("0337526546")
        self.new_customer_page.enter_email("thien#gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.click_submit()
        self.log_error_message()  # Ghi lại thông báo lỗi
        assert self.new_customer_page.get_error_message() == "Email ID is not valid", "Thông báo không đúng."

    def test_customer_gender_selection(self, setup):
        """Kiểm thử chọn giới tính."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("Thien")
        self.new_customer_page.select_gender("male")  # Hoặc "female"
        self.new_customer_page.enter_address("Danang")
        self.new_customer_page.enter_city("DaNang")
        self.new_customer_page.enter_pin("123456")
        self.new_customer_page.enter_phone("0337526546")
        self.new_customer_page.enter_email("thien@gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.click_submit()
        assert self.new_customer_page.get_success_message() == "Account added successfully", "Thông báo không đúng."

    def test_customer_dob_format(self, setup):
        """Kiểm thử định dạng ngày sinh."""
        self.open_new_customer_page(setup)
        self.new_customer_page.enter_customer_name("Thien")
        self.new_customer_page.enter_address("Danang")
        self.new_customer_page.enter_city("DaNang")
        self.new_customer_page.enter_pin("123456")
        self.new_customer_page.enter_phone("0337526546")
        self.new_customer_page.enter_email("thien@gmail.com")
        self.new_customer_page.enter_password("mypassword")  # Thêm mật khẩu
        self.new_customer_page.enter_date_of_birth("2002-03-01")  # Định dạng đúng: YYYY-MM-DD
        self.new_customer_page.click_submit()
        assert self.new_customer_page.get_success_message() == "Account added successfully", "Thông báo không đúng."
