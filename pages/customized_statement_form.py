# pages/customized_statement_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class CustomizedStatementPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/CustomisedStatementInput.php"  # Địa chỉ trang Customized Statement Form

    def open(self):
        self.driver.get(self.url)

    def fill_form(self, account_no, from_date, to_date, min_transaction, num_transaction):
        self.driver.find_element(By.NAME, "accountno").send_keys(account_no)
        self.driver.find_element(By.NAME, "fdate").send_keys(from_date)
        self.driver.find_element(By.NAME, "tdate").send_keys(to_date)
        self.driver.find_element(By.NAME, "amountlowerlimit").send_keys(min_transaction)
        self.driver.find_element(By.NAME, "numtransaction").send_keys(num_transaction)

    def submit_form(self):
        submit_button = self.driver.find_element(By.NAME, "AccSubmit")
        submit_button.click()

    def get_confirmation_message(self):
        # Cập nhật theo cách bạn lấy thông báo xác nhận sau khi gửi biểu mẫu
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "selector_thong_bao_xac_nhan"))  # Thay thế với selector đúng
        ).text
