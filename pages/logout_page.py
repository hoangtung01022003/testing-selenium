# pages/logout_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/Logout.php"  # Địa chỉ trang Logout

    def open(self):
        self.driver.get(self.url)

    def click_logout(self):
        logout_link = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.LINK_TEXT, "Log out"))
        )
        logout_link.click()

    def get_logout_confirmation(self):
        # Cập nhật theo cách bạn lấy thông báo xác nhận đăng xuất
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "selector_thong_bao_xac_nhan"))  # Thay thế với selector đúng
        ).text
