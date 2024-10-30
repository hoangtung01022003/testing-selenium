from selenium.webdriver.common.by import By

class NewCustomerPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.demo.guru99.com/V4/manager/addcustomerpage.php"  # URL của trang
        
        # Cập nhật locators theo mã HTML
        self.customer_name_field = (By.NAME, "name")  # Thay đổi ID cho đúng
        self.address_field = (By.NAME, "addr")  # Thay đổi ID cho đúng
        self.city_field = (By.NAME, "city")  # Thay đổi ID cho đúng
        self.pin_field = (By.NAME, "pinno")  # Thay đổi ID cho đúng
        self.phone_field = (By.NAME, "telephoneno")  # Thay đổi ID cho đúng
        self.email_field = (By.NAME, "emailid")  # Thay đổi ID cho đúng
        self.gender_male_radio = (By.XPATH, "//input[@name='rad1' and @value='m']")  # XPath cho giới tính nam
        self.gender_female_radio = (By.XPATH, "//input[@name='rad1' and @value='f']")  # XPath cho giới tính nữ
        self.dob_field = (By.NAME, "dob")  # Thay đổi ID cho đúng
        self.password_field = (By.NAME, "password")  # Thêm trường mật khẩu
        self.submit_button = (By.NAME, "sub")  # Thay đổi ID cho đúng
        
        # Các thông báo lỗi và thành công
        self.error_message = (By.CLASS_NAME, "error-message")  # Thay đổi CLASS_NAME cho đúng nếu cần
        self.success_message = (By.CLASS_NAME, "success-message")  # Thay đổi CLASS_NAME cho đúng nếu cần

    def open(self):
        self.driver.get(self.url)

    def enter_customer_name(self, name):
        self.driver.find_element(*self.customer_name_field).clear()
        self.driver.find_element(*self.customer_name_field).send_keys(name)

    def enter_address(self, address):
        self.driver.find_element(*self.address_field).clear()
        self.driver.find_element(*self.address_field).send_keys(address)

    def enter_city(self, city):
        self.driver.find_element(*self.city_field).clear()
        self.driver.find_element(*self.city_field).send_keys(city)

    def enter_pin(self, pin):
        self.driver.find_element(*self.pin_field).clear()
        self.driver.find_element(*self.pin_field).send_keys(pin)

    def enter_phone(self, phone):
        self.driver.find_element(*self.phone_field).clear()
        self.driver.find_element(*self.phone_field).send_keys(phone)

    def enter_email(self, email):
        self.driver.find_element(*self.email_field).clear()
        self.driver.find_element(*self.email_field).send_keys(email)

    def select_gender(self, gender):
        if gender.lower() == "male":
            self.driver.find_element(*self.gender_male_radio).click()
        elif gender.lower() == "female":
            self.driver.find_element(*self.gender_female_radio).click()

    def enter_date_of_birth(self, dob):
        self.driver.find_element(*self.dob_field).clear()
        self.driver.find_element(*self.dob_field).send_keys(dob)
    def enter_password(self, password):
        self.driver.find_element(*self.password_field).clear()
        self.driver.find_element(*self.password_field).send_keys(password)

    def click_submit(self):
        self.driver.find_element(*self.submit_button).click()

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text

    def get_success_message(self):
        return self.driver.find_element(*self.success_message).text
