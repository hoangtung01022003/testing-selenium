# tests/test_logout.py

import pytest
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from pages.logout_page import LogoutPage
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

class TestLogout:
    @pytest.fixture(scope="module")
    def setup(self):
        """Thiết lập WebDriver Edge."""
        edge_driver_path = "D:\\Ungdung\\edge\\msedgedriver.exe"  # Đường dẫn tới msedgedriver trên Windows
        service = Service(edge_driver_path)
        driver = webdriver.Edge(service=service)
        yield driver
        driver.quit()

    def open_logout_page(self, driver):
        """Mở trang Logout."""
        self.logout_page = LogoutPage(driver)
        self.logout_page.open()
        WebDriverWait(driver, 10).until(EC.visibility_of_element_located((By.LINK_TEXT, "Log out")))

    def test_logout(self, setup):
        """Kiểm thử chức năng đăng xuất."""
        self.open_logout_page(setup)
        self.logout_page.click_logout()
        assert self.logout_page.get_logout_confirmation() == "You have successfully logged out.", "Thông báo không đúng."
