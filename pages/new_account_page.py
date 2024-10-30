# pages/new_account_page.py

from selenium.webdriver.common.by import By

class NewAccountPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/addAccount.php"  # Thay đổi thành URL chính xác của trang

    def open(self):
        """Mở trang New Account."""
        self.driver.get(self.url)

    def enter_customer_id(self, customer_id):
        """Nhập Customer ID."""
        self.driver.find_element(By.NAME, "cusid").send_keys(customer_id)

    def select_account_type(self, account_type):
        """Chọn loại tài khoản."""
        account_dropdown = self.driver.find_element(By.NAME, "selaccount")
        for option in account_dropdown.find_elements(By.TAG_NAME, "option"):
            if option.text == account_type:
                option.click()
                break

    def enter_initial_deposit(self, initial_deposit):
        """Nhập Initial Deposit."""
        self.driver.find_element(By.NAME, "inideposit").send_keys(initial_deposit)

    def click_submit(self):
        """Nhấn nút submit."""
        self.driver.find_element(By.NAME, "button2").click()

    def click_reset(self):
        """Nhấn nút reset."""
        self.driver.find_element(By.NAME, "reset").click()

    def get_error_message(self):
        """Lấy thông báo lỗi."""
        return self.driver.find_element(By.ID, "message14").text  # Thay đổi ID nếu cần

    def get_success_message(self):
        """Lấy thông báo thành công."""
        # Giả sử có một phần tử hiển thị thông báo thành công
        return self.driver.find_element(By.ID, "success_message_id").text  # Thay đổi ID nếu cần
