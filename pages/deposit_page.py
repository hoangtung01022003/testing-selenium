# pages/deposit_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class DepositPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/DepositInput.php"  # Thay thế bằng URL thực tế của trang gửi tiền

    def open(self):
        self.driver.get(self.url)

    def enter_account_number(self, account_number):
        account_no_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "accountno"))
        )
        account_no_input.clear()
        account_no_input.send_keys(account_number)

    def enter_amount(self, amount):
        amount_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "ammount"))
        )
        amount_input.clear()
        amount_input.send_keys(amount)

    def enter_description(self, description):
        description_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "desc"))
        )
        description_input.clear()
        description_input.send_keys(description)

    def click_submit(self):
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

    def get_success_message(self):
        # Cập nhật theo cách bạn lấy thông báo thành công
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "selector_chi_tiet_thong_bao_thanh_cong"))  # Thay thế với selector đúng
        ).text

    def get_error_message(self):
        # Cập nhật theo cách bạn lấy thông báo lỗi
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "selector_chi_tiet_thong_bao_loi"))  # Thay thế với selector đúng
        ).text
