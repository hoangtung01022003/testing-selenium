# pages/fund_transfer_page.py

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class FundTransferPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/FundTransInput.php"  # Thay đổi đường dẫn nếu cần

    def open(self):
        self.driver.get(self.url)

    def enter_payers_account(self, payers_account):
        payers_account_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "payersaccount"))
        )
        payers_account_input.clear()
        payers_account_input.send_keys(payers_account)

    def enter_payees_account(self, payee_account):
        payee_account_input = WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.NAME, "payeeaccount"))
        )
        payee_account_input.clear()
        payee_account_input.send_keys(payee_account)

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
            EC.visibility_of_element_located((By.CSS_SELECTOR, "selector_thong_bao_thanh_cong"))  # Thay thế với selector đúng
        ).text

    def get_error_message(self):
        # Cập nhật theo cách bạn lấy thông báo lỗi
        return WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "selector_thong_bao_loi"))  # Thay thế với selector đúng
        ).text
