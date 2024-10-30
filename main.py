# main.py
import pytest

def main():
    print("Chọn loại kiểm tra bạn muốn chạy:")
    print("1. Kiểm tra Đăng nhập")
    print("2. Kiểm tra Khách hàng mới")
    
    choice = input("Nhập số tương ứng (1 hoặc 2): ")

    if choice == '1':
        pytest.main(["-v", "-s", "tests/test_login.py::TestLogin"])  # Thay thế bằng tên tệp của bạn
    elif choice == '2':
        pytest.main(["-v", "-s", "tests/test_new_customer.py::TestNewCustomer"])  # Thay thế bằng tên tệp của 
    elif choice == '3':
        pytest.main(["-v", "-s", "tests/test_new_account.py::TestNewAccount"])  # Thay thế bằng tên tệp của     
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập 1 hoặc 2.")

if __name__ == "__main__":
    main()
