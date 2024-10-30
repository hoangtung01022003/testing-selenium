import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage  # Giả định có lớp LoginPage trong thư mục pages

class TestLogin:
    @pytest.fixture(scope="module")
    def setup(self):
        """Thiết lập WebDriver Edge."""
        edge_driver_path = "D:\\Ungdung\\edge\\msedgedriver.exe"
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service)
        yield driver  # Trả về driver để có thể sử dụng trong các test
        driver.quit()

    def test_login_success_valid_user(self, setup):
        """Kiểm thử đăng nhập thành công với thông tin hợp lệ."""
        login_page = LoginPage(setup)  # Truyền driver vào LoginPage
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("mngr596318")  # Tên người dùng
        login_page.enter_password("uzunEzY")      # Mật khẩu
        login_page.click_login()  # Nhấn nút đăng nhập
        assert login_page.is_login_successful(), "Đăng nhập thành công với thông tin đúng."

    def test_login_success(self, setup):
        """Kiểm thử đăng nhập thành công với thông tin khác."""
        login_page = LoginPage(setup)  # Truyền driver vào LoginPage
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("mngr123")  # Tên người dùng khác
        login_page.enter_password("abcd1234")  # Mật khẩu khác
        login_page.click_login()  # Nhấn nút đăng nhập
        assert login_page.is_login_successful(), "Đăng nhập thành công không đúng."

    def test_login_wrong_user_id(self, setup):
        """Kiểm thử đăng nhập với User ID không đúng."""
        login_page = LoginPage(setup)
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("wrongUser")  # User ID không đúng
        login_page.enter_password("uzunEzY")  # Mật khẩu hợp lệ
        login_page.click_login()  # Nhấn nút đăng nhập
        error_message = login_page.get_error_message()  # Lấy thông báo lỗi
        assert error_message == "User or Password is not valid", f"Lỗi không đúng: {error_message}"

    def test_login_wrong_password(self, setup):
        """Kiểm thử đăng nhập với Password không đúng."""
        login_page = LoginPage(setup)
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("mngr123")  # User ID hợp lệ
        login_page.enter_password("wrongPassword")  # Mật khẩu không đúng
        login_page.click_login()  # Nhấn nút đăng nhập
        error_message = login_page.get_error_message()  # Lấy thông báo lỗi
        assert error_message == "User or Password is not valid", f"Lỗi không đúng: {error_message}"

    def test_login_empty_user_id(self, setup):
        """Kiểm thử đăng nhập với User ID để trống."""
        login_page = LoginPage(setup)
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("")  # Để trống User ID
        login_page.enter_password("uzunEzY")  # Mật khẩu hợp lệ
        login_page.click_login()  # Nhấn nút đăng nhập
        error_message = login_page.get_error_message()  # Lấy thông báo lỗi
        assert error_message == "User or Password is not valid", f"Lỗi không đúng: {error_message}"

    def test_login_empty_password(self, setup):
        """Kiểm thử đăng nhập với Password để trống."""
        login_page = LoginPage(setup)
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("mngr123")  # User ID hợp lệ
        login_page.enter_password("")  # Để trống mật khẩu
        login_page.click_login()  # Nhấn nút đăng nhập
        error_message = login_page.get_error_message()  # Lấy thông báo lỗi
        assert error_message == "User or Password is not valid", f"Lỗi không đúng: {error_message}"

    def test_login_both_empty(self, setup):
        """Kiểm thử đăng nhập với cả hai trường để trống."""
        login_page = LoginPage(setup)
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("")  # Để trống User ID
        login_page.enter_password("")  # Để trống mật khẩu
        login_page.click_login()  # Nhấn nút đăng nhập
        error_message = login_page.get_error_message()  # Lấy thông báo lỗi
        assert error_message == "User or Password is not valid", f"Lỗi không đúng: {error_message}"

    def test_login_long_user_id(self, setup):
        """Kiểm thử đăng nhập với User ID dài hơn quy định."""
        login_page = LoginPage(setup)
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("mngr123456789")  # User ID dài
        login_page.enter_password("uzunEzY")  # Mật khẩu hợp lệ
        login_page.click_login()  # Nhấn nút đăng nhập
        error_message = login_page.get_error_message()  # Lấy thông báo lỗi
        assert error_message == "User or Password is not valid", f"Lỗi không đúng: {error_message}"

    def test_login_special_characters(self, setup):
        """Kiểm thử đăng nhập với ký tự đặc biệt."""
        login_page = LoginPage(setup)
        login_page.open()  # Mở trang đăng nhập
        login_page.enter_username("mngr@123")  # User ID có ký tự đặc biệt
        login_page.enter_password("uzunEzY!1234")  # Mật khẩu có ký tự đặc biệt
        login_page.click_login()  # Nhấn nút đăng nhập
        error_message = login_page.get_error_message()  # Lấy thông báo lỗi
        assert error_message == "User or Password is not valid", f"Lỗi không đúng: {error_message}"
    def test_login_success_with_redirect_failure(self, setup):
        """Kiểm thử đăng nhập thành công nhưng trang không load."""
        login_page = LoginPage(setup)
        login_page.open()
        login_page.enter_username("mngr456")  # Tên người dùng hợp lệ
        login_page.enter_password("password456")  # Mật khẩu hợp lệ
        login_page.click_login()
        
        # Giả định là một điều kiện không thành công khi trang không load
        assert not login_page.is_redirect_successful(), "Trang không load sau khi đăng nhập."