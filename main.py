# main.py
import pytest

def main():
    print("Chọn loại kiểm tra bạn muốn chạy:")
    print("1. Kiểm tra Đăng nhập")
    print("2. Kiểm tra Khách hàng mới")
    print("3. Kiểm tra Tài khoản mới")
    print("4. Kiểm tra Nạp tiền")
    print("5. Kiểm tra Rút tiền")
    print("6. Kiểm tra Chuyển tiền")
    print("7. Kiểm tra Báo cáo Tùy chỉnh")
    print("8. Kiểm tra Đăng xuất")
    
    choice = input("Nhập số tương ứng (1 hoặc 2): ")

    if choice == '1':
        pytest.main(["-v", "-s", "tests/test_login.py::TestLogin"])  # Thay thế bằng tên tệp của bạn
    elif choice == '2':
        pytest.main(["-v", "-s", "tests/test_new_customer.py::TestNewCustomer"])  # Thay thế bằng tên tệp của 
    elif choice == '3':
        pytest.main(["-v", "-s", "tests/test_new_account.py::TestNewAccount"])  # Thay thế bằng tên tệp của     
    elif choice == '4':
        pytest.main(["-v", "-s", "tests/test_deposit.py::TestDeposit"])  # Thay thế bằng tên tệp của  
    elif choice == '5':
        pytest.main(["-v", "-s", "tests/test_widthdraw.py::TestWidthdraw"])  # Thay thế bằng tên tệp của  
    elif choice == '6':
        pytest.main(["-v", "-s", "tests/test_fund_transfer.py::TestFundTransfer"])  # Thay thế bằng tên tệp của  
    elif choice == '7':
        pytest.main(["-v", "-s", "tests/test_customized_statement.py::TestCustomizedStatement"])  # Thay thế bằng tên tệp của  
    elif choice == '8':
        pytest.main(["-v", "-s", "tests/test_logout.py::TestLogout"])  # Thay thế bằng tên tệp của  
    else:
        print("Lựa chọn không hợp lệ. Vui lòng nhập 1 hoặc 2.")

if __name__ == "__main__":
    main()
